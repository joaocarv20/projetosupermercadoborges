"""
Acompanhamento da sugestão: para uma semana que já terminou, compara o que o sistema sugeriu,
o que o comprador salvou e o que realmente vendeu.

O motor não usa estoque, então a sugestão é uma previsão de venda: o acerto do sistema é medido
contra a venda real. A quantidade do comprador mostra onde ele discorda (pode ser estoque, promoção...).

Como rodar:  python acompanhamento.py 2026-10-12   (a segunda-feira da semana)
"""
import sys
from datetime import date, timedelta
from statistics import median

from base_local import abrir
from config import ACERTO_MARGEM, ACERTO_UNIDADES


def semanas_fechadas(base):
    """Segundas-feiras com sugestão salva cuja semana já terminou e tem venda na base, da mais nova para a mais antiga."""
    ultimo = base.execute("SELECT MAX(data) FROM vendas_diarias").fetchone()[0]
    if not ultimo:
        return []
    return [date.fromisoformat(s) for (s,) in base.execute(
        "SELECT DISTINCT semana FROM sugestoes WHERE date(semana, '+6 days') <= ? ORDER BY semana DESC", (ultimo,))]


def erro_pct(previsto, vendeu):
    """+20 = previu 20% acima do que vendeu. None quando não vendeu nada (não dá para medir em %)."""
    return (previsto - vendeu) / vendeu * 100 if vendeu else None


def acertou(previsto, vendeu):
    return abs(previsto - vendeu) <= max(ACERTO_MARGEM * vendeu, ACERTO_UNIDADES)


def comparar(base, segunda):
    """Uma linha por família com sugestão salva na semana, do maior erro do sistema para o menor."""
    fim = segunda + timedelta(days=6)
    linhas = base.execute(
        """SELECT s.familia_id, f.nome, MIN(d.nome), MAX(p.unidade), s.qtd_sugerida, s.qtd_final,
                  (SELECT COALESCE(SUM(v.qtd), 0) FROM vendas_diarias v JOIN produtos p2 ON p2.codprod = v.codprod
                   WHERE p2.familia_id = s.familia_id AND v.data BETWEEN ? AND ?)
           FROM sugestoes s JOIN familias f ON f.id = s.familia_id
           JOIN produtos p ON p.familia_id = s.familia_id LEFT JOIN departamentos d ON d.codepto = p.codepto
           WHERE s.semana = ? GROUP BY s.familia_id""",
        (segunda.isoformat(), fim.isoformat(), segunda.isoformat()))
    resultado = []
    for familia, nome, depto, unidade, sugerido, final, vendeu in linhas:
        # Sem quantidade final: o comprador não abriu esse departamento; com ela igual à sugestão: concordou
        alterou = final is not None and final != sugerido
        resultado.append({
            "familia_id": familia, "nome": nome, "departamento": depto or "SEM DEPARTAMENTO", "unidade": unidade,
            "sugerido": sugerido, "final": final, "vendeu": vendeu, "alterou": alterou,
            "erro": erro_pct(sugerido, vendeu), "acertou": acertou(sugerido, vendeu),
            # Quem chegou mais perto da venda, só quando o comprador mudou a sugestão
            "mais_perto": (None if not alterou or abs(final - vendeu) == abs(sugerido - vendeu)
                           else "comprador" if abs(final - vendeu) < abs(sugerido - vendeu) else "sistema"),
        })
    # Sugeriu e não vendeu nada vem primeiro; depois o maior erro em %
    return sorted(resultado, key=lambda r: (r["erro"] is not None, -abs(r["erro"] or 0), r["nome"]))


def resumo(linhas):
    """Números do topo da tela."""
    alteradas = [l for l in linhas if l["alterou"]]
    return {
        "familias": len(linhas),
        "acertos": sum(l["acertou"] for l in linhas),
        "alteradas": len(alteradas),
        "comprador_mais_perto": sum(l["mais_perto"] == "comprador" for l in alteradas),
        "sistema_mais_perto": sum(l["mais_perto"] == "sistema" for l in alteradas),
    }


def por_departamento(linhas):
    """Acerto e erro típico (mediana do erro em %) de cada departamento, do que mais erra para o que menos erra.
    Mediana para um produto muito fora não puxar o departamento inteiro; erro positivo = sugere demais.
    O que foi sugerido e não vendeu nada não tem erro em %: fica contado à parte (sem_venda)."""
    grupos = {}
    for l in linhas:
        grupos.setdefault(l["departamento"], []).append(l)
    deptos = []
    for nome, ls in grupos.items():
        erros = [l["erro"] for l in ls if l["erro"] is not None]
        deptos.append({"departamento": nome, "familias": len(ls), "acertos": sum(l["acertou"] for l in ls),
                       "sem_venda": len(ls) - len(erros),
                       "erro_tipico": median(erros) if erros else None})
    return sorted(deptos, key=lambda d: d["acertos"] / d["familias"])


if __name__ == "__main__":
    base = abrir()
    semana = date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else next(iter(semanas_fechadas(base)), None)
    if not semana:
        sys.exit("Nenhuma semana com sugestão salva já terminou.")
    linhas = comparar(base, semana)
    r = resumo(linhas)
    print(f"Semana de {semana:%d/%m/%Y}: o sistema acertou {r['acertos']} de {r['familias']} famílias "
          f"(margem de {ACERTO_MARGEM:.0%} ou {ACERTO_UNIDADES} un). O comprador alterou {r['alteradas']}.")
    for d in por_departamento(linhas):
        erro = "—" if d["erro_tipico"] is None else f"{d['erro_tipico']:+.0f}%"
        print(f"  {d['departamento'][:30]:30}  acertou {d['acertos']:>4} de {d['familias']:>4}   erro típico {erro}")

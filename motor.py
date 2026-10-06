"""
Motor de sugestão de compra. Não usa estoque: só vendas de semanas equivalentes.

Para a semana-alvo (segunda a domingo), pega as últimas 6 semanas do MESMO TIPO (salário, recarga,
meio do mês, fraca ou feriado), soma as vendas de cada família em cada uma e sugere a mediana.
A sugestão fica na unidade do produto (unidades ou kg), sem arredondar para caixa: o comprador converte.

Como rodar:  python motor.py              sugestão da próxima segunda-feira (a compra de hoje)
             python motor.py 2026-10-12   sugestão de outra semana (a data precisa ser uma segunda)
"""
import math
import sys
from datetime import date, timedelta
from statistics import median

from base_local import abrir
from calendario import tipo_semana
from config import SEMANAS_EQUIVALENTES


def semanas_equivalentes(base, segunda):
    """Até 6 segundas-feiras anteriores com o mesmo tipo de semana, da mais recente para a mais antiga.
    Só entram semanas completas (dentro do período com vendas) e sem dia marcado como atípico."""
    primeiro, ultimo = base.execute("SELECT MIN(data), MAX(data) FROM vendas_diarias").fetchone()
    if not primeiro:
        return []
    primeiro, ultimo = date.fromisoformat(primeiro), date.fromisoformat(ultimo)
    atipicos = [date.fromisoformat(d) for (d,) in base.execute("SELECT data FROM calendario WHERE atipico = 1")]
    tipo, achadas = tipo_semana(segunda), []
    outra = segunda - timedelta(weeks=1)
    while len(achadas) < SEMANAS_EQUIVALENTES and outra >= primeiro:
        fim = outra + timedelta(days=6)
        if fim <= ultimo and tipo_semana(outra) == tipo and not any(outra <= a <= fim for a in atipicos):
            achadas.append(outra)
        outra -= timedelta(weeks=1)
    return achadas


def vendas_da_semana(base, segunda):
    """{(familia_id, codprod): quantidade vendida} de segunda a domingo."""
    linhas = base.execute(
        """SELECT p.familia_id, v.codprod, SUM(v.qtd) FROM vendas_diarias v
           JOIN produtos p ON p.codprod = v.codprod WHERE v.data BETWEEN ? AND ?
           GROUP BY p.familia_id, v.codprod""", (segunda.isoformat(), (segunda + timedelta(days=6)).isoformat()))
    return {(f, c): q for f, c, q in linhas}


def arredondar(qtd, unidade):
    """Unidades: para cima, em inteiros. Quilos: 1 casa decimal. O round tira ruído de soma de decimais."""
    qtd = round(qtd, 6)
    return round(qtd, 1) if unidade == "KG" else math.ceil(qtd)


def gerar(base, segunda):
    """Lista de famílias com a sugestão para a semana que começa em `segunda` (vazia se não há histórico)."""
    semanas = semanas_equivalentes(base, segunda)
    if not semanas:
        return []
    vendas = {s: vendas_da_semana(base, s) for s in semanas}
    passado = {}  # mesma semana do ano passado, somada por família
    for (familia, _), qtd in vendas_da_semana(base, segunda - timedelta(weeks=52)).items():
        passado[familia] = passado.get(familia, 0) + qtd
    primeira_venda = dict(base.execute(
        "SELECT p.familia_id, MIN(v.data) FROM vendas_diarias v JOIN produtos p ON p.codprod = v.codprod GROUP BY p.familia_id"))
    cadastro = {f: (nome, unidade, depto) for f, nome, unidade, depto in base.execute(
        """SELECT f.id, f.nome, MAX(p.unidade), MIN(d.nome) FROM familias f JOIN produtos p ON p.familia_id = f.id
           LEFT JOIN departamentos d ON d.codepto = p.codepto GROUP BY f.id""")}
    descricao = dict(base.execute("SELECT codprod, descricao FROM produtos"))

    por_familia = {}  # {familia_id: {codprod: {semana: qtd}}}
    for semana, v in vendas.items():
        for (familia, codprod), qtd in v.items():
            por_familia.setdefault(familia, {}).setdefault(codprod, {})[semana] = qtd

    resultado = []
    for familia, produtos in por_familia.items():
        # Semanas antes da 1ª venda da família não contam (produto novo não tinha como vender)
        uteis = [s for s in semanas if s >= date.fromisoformat(primeira_venda[familia])]
        if not uteis:
            continue
        mediana = median(sum(p.get(s, 0) for p in produtos.values()) for s in uteis)
        if mediana <= 0:
            continue
        nome, unidade, depto = cadastro[familia]
        medianas = {c: median(p.get(s, 0) for s in uteis) for c, p in produtos.items()}
        soma = sum(medianas.values()) or 1
        resultado.append({
            "familia_id": familia, "nome": nome, "departamento": depto, "unidade": unidade,
            "mediana": round(mediana, 3), "sugestao": arredondar(mediana, unidade),
            "ano_passado": arredondar(passado.get(familia, 0), unidade),
            "semanas_usadas": len(uteis),
            "produtos": [{"codprod": c, "descricao": descricao[c], "qtd": round(m, 3), "pct": m / soma * 100}
                         for c, m in sorted(medianas.items(), key=lambda x: -x[1]) if m > 0]})
    return sorted(resultado, key=lambda r: r["nome"])


def gravar(base, segunda, linhas):
    """Grava a sugestão na tabela sugestoes. A quantidade final que o comprador já digitou é preservada."""
    with base:
        base.execute("DELETE FROM sugestoes WHERE semana = ? AND qtd_final IS NULL", (segunda.isoformat(),))
        base.executemany(
            "INSERT INTO sugestoes (semana, familia_id, qtd_sugerida) VALUES (?, ?, ?) "
            "ON CONFLICT(semana, familia_id) DO UPDATE SET qtd_sugerida = excluded.qtd_sugerida",
            [(segunda.isoformat(), l["familia_id"], l["sugestao"]) for l in linhas])


def proxima_segunda(hoje):
    """A compra é feita na segunda para a semana seguinte: sempre a segunda depois de hoje."""
    return hoje + timedelta(days=7 - hoje.weekday())


if __name__ == "__main__":
    segunda = date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else proxima_segunda(date.today())
    if segunda.weekday() != 0:
        sys.exit("A data precisa ser uma segunda-feira.")
    base = abrir()
    linhas = gerar(base, segunda)
    gravar(base, segunda, linhas)
    print(f"Semana de {segunda:%d/%m/%Y} ({tipo_semana(segunda)}): {len(linhas)} famílias com sugestão.")

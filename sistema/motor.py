"""
Motor de sugestão de compra. Não usa estoque: só vendas de semanas equivalentes.

Para a semana-alvo (segunda a domingo), pega as últimas 6 semanas do MESMO TIPO (salário, recarga,
meio do mês, fraca ou feriado), soma as vendas de cada família em cada uma e sugere a mediana.
A sugestão fica na unidade do produto (unidades ou kg), sem arredondar para caixa: o comprador converte.

Período diferente de uma semana (de qualquer dia a qualquer dia): gerar_periodo() reparte a sugestão de cada
semana que o período toca pelo peso de cada dia da semana na venda.

Como rodar:  python -m sistema.motor              sugestão da próxima segunda-feira (a compra de hoje)
             python -m sistema.motor 2026-10-12   sugestão de outra semana (a data precisa ser uma segunda)
"""
import math
import sys
from datetime import date, timedelta
from statistics import median

from sistema.base_local import abrir
from sistema.calendario import tipo_semana
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


def vendas_entre(base, inicio, fim):
    """{(familia_id, codprod): quantidade vendida} de inicio a fim, os dois incluídos."""
    linhas = base.execute(
        """SELECT p.familia_id, v.codprod, SUM(v.qtd) FROM vendas_diarias v
           JOIN produtos p ON p.codprod = v.codprod WHERE v.data BETWEEN ? AND ?
           GROUP BY p.familia_id, v.codprod""", (inicio.isoformat(), fim.isoformat()))
    return {(f, c): q for f, c, q in linhas}


def arredondar(qtd, unidade):
    """Unidades: para cima, em inteiros. Quilos: 1 casa decimal. O round tira ruído de soma de decimais."""
    qtd = round(qtd, 6)
    return round(qtd, 1) if unidade == "KG" else math.ceil(qtd)


def dividir(total, pesos, unidade):
    """Reparte a compra da família entre os sabores, na proporção da venda de cada um.
    Unidades: inteiros que somam exatamente o total (as sobras vão para quem ficou mais perto da próxima unidade)."""
    soma = sum(pesos)
    if not soma:
        return [0] * len(pesos)
    exatos = [total * p / soma for p in pesos]
    if unidade == "KG":
        return [round(e, 1) for e in exatos]
    partes = [math.floor(round(e, 6)) for e in exatos]
    sobra = round(total) - sum(partes)
    for i in sorted(range(len(pesos)), key=lambda i: partes[i] - exatos[i])[:max(sobra, 0)]:
        partes[i] += 1
    return partes


def gerar(base, segunda):
    """Lista de famílias com a sugestão para a semana que começa em `segunda` (vazia se não há histórico)."""
    semanas = semanas_equivalentes(base, segunda)
    if not semanas:
        return []
    vendas = {s: vendas_entre(base, s, s + timedelta(days=6)) for s in semanas}
    passado = ano_passado(base, segunda, segunda + timedelta(days=6))
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


def ano_passado(base, inicio, fim):
    """{familia_id: venda} nos mesmos dias da semana, 52 semanas antes."""
    passado = {}
    for (familia, _), qtd in vendas_entre(base, inicio - timedelta(weeks=52), fim - timedelta(weeks=52)).items():
        passado[familia] = passado.get(familia, 0) + qtd
    return passado


def peso_dos_dias(base):
    """[segunda, ..., domingo]: quanto cada dia da semana vende, em fração da semana (soma 1).
    Das últimas 12 semanas com venda, o mercado inteiro."""
    # ponytail: um peso só para o mercado todo; se bebida (que pesa mais no fim de semana) errar nos períodos
    # quebrados, calcular por departamento
    ultimo = base.execute("SELECT MAX(data) FROM vendas_diarias").fetchone()[0]
    if not ultimo:
        return [1 / 7] * 7
    ultimo = date.fromisoformat(ultimo)
    venda = [0] * 7
    for dia, qtd in base.execute("SELECT data, SUM(qtd) FROM vendas_diarias WHERE data > ? GROUP BY data",
                                 ((ultimo - timedelta(weeks=12)).isoformat(),)):
        venda[date.fromisoformat(dia).weekday()] += qtd
    total = sum(venda)
    return [v / total for v in venda] if total else [1 / 7] * 7


def partes_do_periodo(base, inicio, fim):
    """{segunda: parte da venda daquela semana que cai no período}. Semana inteira dentro = 1."""
    dias = {}
    for i in range((fim - inicio).days + 1):
        d = inicio + timedelta(days=i)
        dias.setdefault(d - timedelta(days=d.weekday()), []).append(d.weekday())
    peso = peso_dos_dias(base)
    return {s: 1 if len(ds) == 7 else sum(peso[d] for d in ds) for s, ds in dias.items()}


def gerar_periodo(base, inicio, fim, gerar_semana=gerar):
    """Sugestão para vender de `inicio` a `fim` (qualquer dia, os dois incluídos), no formato de gerar().
    Cada semana que o período toca entra com a sua sugestão vezes a parte dela que cai no período: de quarta a
    sexta da semana seguinte = o fim de uma semana + o começo da outra, cada uma com o seu tipo (salário, meio...).
    De segunda a domingo dá o mesmo que gerar(). gerar_semana(base, segunda) permite usar a sugestão guardada."""
    familias = {}
    for segunda, parte in partes_do_periodo(base, inicio, fim).items():
        for l in gerar_semana(base, segunda):
            f = familias.setdefault(l["familia_id"], {**l, "mediana": 0, "qtds": {}})
            f["mediana"] += l["mediana"] * parte
            f["semanas_usadas"] = min(f["semanas_usadas"], l["semanas_usadas"])
            for p in l["produtos"]:
                f["qtds"][(p["codprod"], p["descricao"])] = f["qtds"].get((p["codprod"], p["descricao"]), 0) + p["qtd"] * parte
    passado = ano_passado(base, inicio, fim)
    resultado = []
    for familia, f in familias.items():
        qtds = f.pop("qtds")
        soma = sum(qtds.values()) or 1
        resultado.append({
            **f, "mediana": round(f["mediana"], 3), "sugestao": arredondar(f["mediana"], f["unidade"]),
            "ano_passado": arredondar(passado.get(familia, 0), f["unidade"]),
            "produtos": [{"codprod": c, "descricao": d, "qtd": round(q, 3), "pct": q / soma * 100}
                         for (c, d), q in sorted(qtds.items(), key=lambda x: -x[1])]})
    return sorted(resultado, key=lambda r: r["nome"])


def gravar(base, inicio, fim, linhas):
    """Grava a sugestão do período na tabela sugestoes. Fica um período por dia de início: salvar outro fim
    para o mesmo início troca o anterior. A quantidade final que o comprador já digitou é preservada."""
    with base:
        base.execute("DELETE FROM sugestoes WHERE semana = ? AND (qtd_final IS NULL OR fim IS NOT ?)",
                     (inicio.isoformat(), fim.isoformat()))
        base.executemany(
            "INSERT INTO sugestoes (semana, fim, familia_id, qtd_sugerida) VALUES (?, ?, ?, ?) "
            "ON CONFLICT(semana, familia_id) DO UPDATE SET qtd_sugerida = excluded.qtd_sugerida",
            [(inicio.isoformat(), fim.isoformat(), l["familia_id"], l["sugestao"]) for l in linhas])


def proxima_segunda(hoje):
    """A compra é feita na segunda para a semana seguinte: sempre a segunda depois de hoje."""
    return hoje + timedelta(days=7 - hoje.weekday())


if __name__ == "__main__":
    segunda = date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else proxima_segunda(date.today())
    if segunda.weekday() != 0:
        sys.exit("A data precisa ser uma segunda-feira.")
    base = abrir()
    linhas = gerar(base, segunda)
    gravar(base, segunda, segunda + timedelta(days=6), linhas)
    print(f"Semana de {segunda:%d/%m/%Y} ({tipo_semana(segunda)}): {len(linhas)} famílias com sugestão.")

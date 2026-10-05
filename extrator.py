"""
Extrator: copia do Oracle do Cefas para a base local (SQLite) o cadastro e as vendas.

- Só lê (SELECT) e só traz totais por produto e por dia, nunca cupom ou cliente.
- Vendas = JP.MOVIMENTACAO, operação 'S', sem cancelados (status 'C'), valor = qt x preço.
  É o filtro que bateu com o relatório "Curva ABC Produto" do Cefas (03 a 09/08/2026).
- Departamentos de config.DEPTOS_FORA não entram nas vendas.

Como rodar (no Windows, onde o Oracle é alcançado):
  python extrator.py              1ª vez: carrega tudo desde dez/2023. Depois: só os últimos dias.
  python extrator.py 2026-01-01   refaz as vendas a partir dessa data.
Demora mais na 1ª vez (um mês por vez). Cada consulta tem 300 s; mude com ORA_TIMEOUT_SEG no .env.
"""
import os
import sys
from datetime import date, datetime, timedelta

from base_local import abrir
from config import DEPTOS_FORA, INICIO_HISTORICO
from conferir_vendas import numero, reais
from explorar_banco import carregar_env, conectar, consultar

REPROCESSAR_DIAS = 3  # a carga diária refaz os últimos dias, para pegar cancelamentos feitos depois

FORA = tuple(DEPTOS_FORA)
BINDS_FORA = {f"d{i}": codigo for i, codigo in enumerate(FORA)}
NAO_FORA = f"NVL(p.codepto, '-') NOT IN ({', '.join(':' + chave for chave in BINDS_FORA)})"


def carregar_departamentos(ora, base, schema):
    linhas = consultar(ora, f"SELECT d.codepto, d.departamento FROM {schema}.depto d")
    with base:
        base.executemany(
            "INSERT INTO departamentos (codepto, nome, entra) VALUES (?, ?, ?) "
            "ON CONFLICT(codepto) DO UPDATE SET nome = excluded.nome, entra = excluded.entra",
            [(c, n, 0 if c in DEPTOS_FORA else 1) for c, n in linhas])
    print(f"  {len(linhas)} departamentos ({len(FORA)} marcados como fora da sugestão)")


def carregar_produtos(ora, base, schema):
    linhas = consultar(ora, f"""
        SELECT p.codprod, p.descricao, p.unidade, p.codepto, p.codsec, p.codcat, p.codsubcat,
               p.codbarra, p.dtexclusao
        FROM {schema}.produto p WHERE {NAO_FORA}""", BINDS_FORA)
    with base:
        base.executemany(
            """INSERT INTO produtos (codprod, descricao, unidade, codepto, codsec, codcat, codsubcat, codbarra, dtexclusao)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
               ON CONFLICT(codprod) DO UPDATE SET descricao = excluded.descricao, unidade = excluded.unidade,
                   codepto = excluded.codepto, codsec = excluded.codsec, codcat = excluded.codcat,
                   codsubcat = excluded.codsubcat, codbarra = excluded.codbarra, dtexclusao = excluded.dtexclusao""",
            [(cod, desc or f"PRODUTO {cod}", un, dep, sec, cat, sub, barra,
              dtex.date().isoformat() if dtex else None) for cod, desc, un, dep, sec, cat, sub, barra, dtex in linhas])
        # Produto novo ganha uma família só dele; quem já tem família (ajustada à mão) não é mexido
        base.execute("INSERT OR IGNORE INTO familias (nome) SELECT descricao FROM produtos WHERE familia_id IS NULL")
        base.execute("UPDATE produtos SET familia_id = (SELECT id FROM familias WHERE nome = produtos.descricao) "
                     "WHERE familia_id IS NULL")
    print(f"  {len(linhas)} produtos")


def meses(inicio, fim):
    """Pares (primeiro dia do mês, primeiro dia do mês seguinte) cobrindo de inicio até fim."""
    mes = inicio.replace(day=1)
    while mes <= fim:
        proximo = (mes + timedelta(days=32)).replace(day=1)
        yield mes, proximo
        mes = proximo


def carregar_vendas(ora, base, schema, inicio):
    for mes, proximo in meses(inicio, date.today()):
        ini = max(mes, inicio)  # no 1º mês, começa na data pedida
        linhas = consultar(ora, f"""
            SELECT TRUNC(m.dtmov), m.codprod, SUM(m.qt), SUM(m.qt * m.punit)
            FROM {schema}.movimentacao m JOIN {schema}.produto p ON p.codprod = m.codprod
            WHERE m.dtmov >= :ini AND m.dtmov < :fim AND m.operacao = 'S' AND NVL(m.status, '-') <> 'C'
              AND {NAO_FORA}
            GROUP BY TRUNC(m.dtmov), m.codprod""", {"ini": ini, "fim": proximo, **BINDS_FORA})
        with base:  # apaga e regrava o mês de uma vez: se der erro no meio, nada fica pela metade
            base.execute("DELETE FROM vendas_diarias WHERE data >= ? AND data < ?", (ini.isoformat(), proximo.isoformat()))
            base.executemany("INSERT INTO vendas_diarias (data, codprod, qtd, valor) VALUES (?, ?, ?, ?)",
                             [(dia.date().isoformat(), cod, qtd, valor) for dia, cod, qtd, valor in linhas])
        print(f"  {mes:%m/%Y}: {numero(len(linhas)):>9} linhas, {reais(sum(l[3] for l in linhas)):>18}")


def data_de_inicio(base, argumento):
    """Data pedida na linha de comando; senão, os últimos dias da base; senão, o começo do histórico."""
    if argumento:
        return date.fromisoformat(argumento)
    ultima = base.execute("SELECT MAX(data) FROM vendas_diarias").fetchone()[0]
    if ultima:
        return date.fromisoformat(ultima) - timedelta(days=REPROCESSAR_DIAS)
    return INICIO_HISTORICO


def main():
    try:
        argumento = sys.argv[1] if len(sys.argv) > 1 else None
        if argumento:
            date.fromisoformat(argumento)
    except ValueError:
        sys.exit("Use a data no formato ANO-MÊS-DIA. Ex.: python extrator.py 2026-01-01")
    carregar_env()
    os.environ.setdefault("ORA_TIMEOUT_SEG", "300")
    schema = os.environ.get("ORA_SCHEMA", "JP").upper()
    if not schema.isalnum():
        sys.exit("ORA_SCHEMA inválido no .env")

    ora, _ = conectar()
    base = abrir()
    inicio = data_de_inicio(base, argumento)
    print(f"Extraindo do schema {schema}. Vendas a partir de {inicio:%d/%m/%Y}  ({datetime.now():%d/%m/%Y %H:%M})")
    carregar_departamentos(ora, base, schema)
    carregar_produtos(ora, base, schema)
    carregar_vendas(ora, base, schema, inicio)
    ora.close()
    total, dias, produtos = base.execute("SELECT SUM(valor), COUNT(DISTINCT data), COUNT(DISTINCT codprod) FROM vendas_diarias").fetchone()
    print(f"\nPronto! Base local: {dias} dias, {produtos} produtos com venda, {reais(total)} no total.")
    base.close()


if __name__ == "__main__":
    main()

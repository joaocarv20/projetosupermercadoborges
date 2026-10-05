"""
Conferência das vendas de um período, para comparar com o relatório do ERP.

Lê só TOTAIS (somas por dia, por filial e por tipo de operação). Nenhuma linha
individual, nenhum dado de cliente. Usa a mesma conexão e as mesmas travas do
explorar_banco.py (só SELECT, tempo máximo por consulta).

Precisa de: GRANT SELECT ON JP.MOVIMENTACAO e JP.NFSAID para o usuário do .env.

Como rodar:  python conferir_vendas.py 2026-08-01 2026-08-07
Saída:       conferencia_vendas.md
"""
import os
import sys
from datetime import date, datetime

from explorar_banco import PASTA, carregar_env, conectar, consultar, tabela_md, texto


DIAS = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]


def reais(valor):
    """339123.4 -> 'R$ 339.123,40'."""
    if valor is None:
        return ""
    return "R$ " + f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def numero(valor):
    """Quantidades: sem casas se for inteiro, senão 3 casas (produtos pesados)."""
    if valor is None:
        return ""
    casas = 0 if float(valor).is_integer() else 3
    return f"{valor:,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def main():
    exemplo = "Ex.: python conferir_vendas.py 2026-08-01 2026-08-07"
    if len(sys.argv) < 3:
        sys.exit("Informe a data inicial e a final. " + exemplo)
    try:
        inicio, fim = date.fromisoformat(sys.argv[1]), date.fromisoformat(sys.argv[2])
    except ValueError:
        sys.exit("Use datas no formato ANO-MÊS-DIA. " + exemplo)

    carregar_env()
    schema = os.environ.get("ORA_SCHEMA", "JP").upper()
    if not schema.isalnum():  # o nome vai direto no SQL, então só letras e números
        sys.exit("ORA_SCHEMA inválido no .env")

    conexao, _ = conectar()
    periodo = {"ini": inicio, "fim": fim}
    filtro_m = "m.dtmov >= :ini AND m.dtmov < :fim + 1"
    filtro_n = "n.dtsaida >= :ini AND n.dtsaida < :fim + 1"

    print(f"Conferindo {inicio:%d/%m/%Y} a {fim:%d/%m/%Y} no schema {schema}...")
    partes = [f"# Conferência de vendas – {inicio:%d/%m/%Y} a {fim:%d/%m/%Y}\n",
              f"Schema {schema} · gerado em {datetime.now():%d/%m/%Y %H:%M} · só totais, nenhum dado de cliente.\n",
              "Compare o **total do período** com o relatório de vendas do ERP para as mesmas datas.\n"]

    def secao(titulo, sql, cabecalho, formatar, parametros=periodo):
        print(f"  {titulo}...")
        try:
            linhas = [formatar(l) for l in consultar(conexao, sql, parametros)]
            partes.append(f"\n## {titulo}\n\n" + tabela_md(cabecalho, linhas))
        except Exception as erro:  # ex.: sem permissão (ORA-00942) ou tempo esgotado
            print(f"    erro: {erro}")
            partes.append(f"\n## {titulo}\n\n> ⚠ Não gerado: {texto(erro)}\n")

    def dia(d):
        return f"{d:%d/%m/%Y} ({DIAS[d.weekday()]})"

    # HISTESTOQUE foi descartada: tem meses inteiros faltando (não tem ago/2026, por exemplo).

    # 1) MOVIMENTACAO: itens vendidos. S = venda, status C = cancelado.
    secao("1. MOVIMENTACAO – por tipo de operação",
          f"""SELECT m.operacao, m.status, COUNT(*), SUM(m.qt), SUM(m.qt * m.punit),
                     COUNT(m.numvenda), COUNT(m.nument)
              FROM {schema}.movimentacao m WHERE {filtro_m}
              GROUP BY m.operacao, m.status ORDER BY 5 DESC NULLS LAST""",
          ["Operação", "Status", "Linhas", "Qtd. total", "Valor (qt × preço)", "Com nº de venda", "Com nº de entrada"],
          lambda l: (l[0], l[1], texto(l[2]), numero(l[3]), reais(l[4]), texto(l[5]), texto(l[6])))

    vendas_mov = f"""FROM {schema}.movimentacao m WHERE {filtro_m} AND m.operacao = 'S' AND NVL(m.status, '-') <> 'C'"""
    secao("2. MOVIMENTACAO – vendas por dia",
          f"""SELECT TRUNC(m.dtmov), COUNT(DISTINCT m.numvenda), COUNT(*), SUM(m.qt), SUM(m.qt * m.punit)
              {vendas_mov} GROUP BY TRUNC(m.dtmov) ORDER BY 1""",
          ["Dia", "Vendas (nº)", "Itens", "Qtd.", "Valor (qt × preço)"],
          lambda l: (dia(l[0]), texto(l[1]), texto(l[2]), numero(l[3]), reais(l[4])))

    # 2) NFSAID: cabeçalho de cada venda (cupom/nota), com o total já calculado pelo ERP.
    #    Se o total daqui for maior que o da MOVIMENTACAO, tem venda cujos itens não estão lá.
    secao("3. NFSAID – por espécie, tipo de venda e filial",
          f"""SELECT n.especie, n.tipovenda, n.codfilial, CASE WHEN n.dtcancel IS NULL THEN 'não' ELSE 'sim' END,
                     COUNT(*), SUM(n.vltotal), SUM(n.vldesconto), SUM(n.vldevol)
              FROM {schema}.nfsaid n WHERE {filtro_n}
              GROUP BY n.especie, n.tipovenda, n.codfilial, CASE WHEN n.dtcancel IS NULL THEN 'não' ELSE 'sim' END
              ORDER BY 6 DESC NULLS LAST""",
          ["Espécie", "Tipo de venda", "Filial", "Cancelada", "Vendas (nº)", "Valor total", "Desconto", "Devolução"],
          lambda l: (l[0], l[1], l[2], l[3], texto(l[4]), reais(l[5]), reais(l[6]), reais(l[7])))

    secao("4. NFSAID x MOVIMENTACAO – por dia (só não canceladas)",
          f"""SELECT TRUNC(n.dtsaida), COUNT(*), SUM(n.vltotal),
                     SUM(CASE WHEN m.numvenda IS NULL THEN 1 END),
                     SUM(CASE WHEN m.numvenda IS NULL THEN n.vltotal END)
              FROM {schema}.nfsaid n
              LEFT JOIN (SELECT DISTINCT m.numvenda {vendas_mov}) m ON m.numvenda = n.numvenda
              WHERE {filtro_n} AND n.dtcancel IS NULL
              GROUP BY TRUNC(n.dtsaida) ORDER BY 1""",
          ["Dia", "Vendas (nº)", "Valor total", "Vendas sem itens na MOVIMENTACAO", "Valor dessas vendas"],
          lambda l: (dia(l[0]), texto(l[1]), reais(l[2]), texto(l[3]), reais(l[4])))

    conexao.close()
    saida = PASTA / "conferencia_vendas.md"
    saida.write_text("\n".join(partes), encoding="utf-8")
    print(f"\nPronto! Relatório salvo em: {saida}")


if __name__ == "__main__":
    main()

"""
Conferência das vendas de um período, para comparar com o relatório do ERP.

Lê só TOTAIS (somas por dia, por filial e por tipo de operação). Nenhuma linha
individual, nenhum dado de cliente. Usa a mesma conexão e as mesmas travas do
explorar_banco.py (só SELECT, tempo máximo por consulta).

Precisa de: GRANT SELECT ON JP.HISTESTOQUE e JP.MOVIMENTACAO para o usuário do .env.

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
    filtro_h = "h.data >= :ini AND h.data < :fim + 1"
    filtro_m = "m.dtmov >= :ini AND m.dtmov < :fim + 1"

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

    # 1) HISTESTOQUE: parece ser o resumo diário de vendas por produto e filial
    secao("1. HISTESTOQUE – total do período",
          f"""SELECT COUNT(DISTINCT h.codprod), SUM(h.qtvenda), SUM(h.vlvenda), SUM(h.qtdevol), SUM(h.vldevol)
              FROM {schema}.histestoque h WHERE {filtro_h}""",
          ["Produtos diferentes", "Qtd. vendida", "Valor vendido", "Qtd. devolvida", "Valor devolvido"],
          lambda l: (texto(l[0]), numero(l[1]), reais(l[2]), numero(l[3]), reais(l[4])))

    secao("2. HISTESTOQUE – por dia",
          f"""SELECT TRUNC(h.data), COUNT(DISTINCT h.codprod), SUM(h.qtvenda), SUM(h.vlvenda)
              FROM {schema}.histestoque h WHERE {filtro_h}
              GROUP BY TRUNC(h.data) ORDER BY 1""",
          ["Dia", "Produtos", "Qtd. vendida", "Valor vendido"],
          lambda l: (f"{l[0]:%d/%m/%Y} ({DIAS[l[0].weekday()]})", texto(l[1]), numero(l[2]), reais(l[3])))

    secao("3. HISTESTOQUE – por filial",
          f"""SELECT h.codfilial, SUM(h.qtvenda), SUM(h.vlvenda)
              FROM {schema}.histestoque h WHERE {filtro_h}
              GROUP BY h.codfilial ORDER BY 3 DESC""",
          ["Filial", "Qtd. vendida", "Valor vendido"],
          lambda l: (l[0], numero(l[1]), reais(l[2])))

    # 2) MOVIMENTACAO: descobrir qual código de OPERACAO é venda
    secao("4. MOVIMENTACAO – por tipo de operação",
          f"""SELECT m.operacao, m.status, COUNT(*), SUM(m.qt), SUM(m.qt * m.punit),
                     COUNT(m.numvenda), COUNT(m.nument)
              FROM {schema}.movimentacao m WHERE {filtro_m}
              GROUP BY m.operacao, m.status ORDER BY 5 DESC NULLS LAST""",
          ["Operação", "Status", "Linhas", "Qtd. total", "Valor (qt × preço)", "Com nº de venda", "Com nº de entrada"],
          lambda l: (l[0], l[1], texto(l[2]), numero(l[3]), reais(l[4]), texto(l[5]), texto(l[6])))

    # 3) HISTESTOQUE veio vazia em ago/2026: ver em quais meses ela tem dados (tabela inteira)
    secao("5. HISTESTOQUE – meses com dados (tabela toda)",
          f"""SELECT TRUNC(h.data, 'MM'), COUNT(*), COUNT(DISTINCT h.data), COUNT(DISTINCT h.codprod), SUM(h.vlvenda)
              FROM {schema}.histestoque h GROUP BY TRUNC(h.data, 'MM') ORDER BY 1 DESC""",
          ["Mês", "Linhas", "Dias diferentes", "Produtos", "Valor vendido"],
          lambda l: (f"{l[0]:%m/%Y}", texto(l[1]), texto(l[2]), texto(l[3]), reais(l[4])),
          parametros={})

    # 4) Vendas (operação S) da MOVIMENTACAO em detalhe, para bater dia a dia com o relatório do ERP.
    #    O valor é calculado de 2 jeitos porque ainda não sabemos qual coluna o ERP usa.
    vendas = f"""COUNT(DISTINCT m.numvenda), COUNT(*), SUM(m.qt), SUM(m.qt * m.punit), SUM(m.subtot), SUM(m.vldesc)
              FROM {schema}.movimentacao m WHERE {filtro_m} AND m.operacao = 'S' AND NVL(m.status, '-') <> 'C'"""
    colunas = ["Vendas (nº)", "Itens", "Qtd.", "Valor (qt × preço)", "Valor (SUBTOT)", "Descontos (VLDESC)"]

    def valores(l):
        return (texto(l[0]), texto(l[1]), numero(l[2]), reais(l[3]), reais(l[4]), reais(l[5]))

    secao("6. MOVIMENTACAO – vendas por dia",
          f"SELECT TRUNC(m.dtmov), {vendas} GROUP BY TRUNC(m.dtmov) ORDER BY 1",
          ["Dia"] + colunas, lambda l: (f"{l[0]:%d/%m/%Y} ({DIAS[l[0].weekday()]})",) + valores(l[1:]))
    secao("7. MOVIMENTACAO – vendas por filial",
          f"SELECT m.codfilial, {vendas} GROUP BY m.codfilial ORDER BY 5 DESC NULLS LAST",
          ["Filial"] + colunas, lambda l: (l[0],) + valores(l[1:]))

    conexao.close()
    saida = PASTA / "conferencia_vendas.md"
    saida.write_text("\n".join(partes), encoding="utf-8")
    print(f"\nPronto! Relatório salvo em: {saida}")


if __name__ == "__main__":
    main()

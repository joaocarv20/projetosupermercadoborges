"""
Lista os departamentos do JP com as vendas dos últimos 28 dias e mostra
quantos anos de venda existem na MOVIMENTACAO. Só totais, nenhum dado de cliente.

Serve para decidir quais departamentos ficam de fora (padaria, açougue, hortifrúti)
e para confirmar quanto histórico existe.

Como rodar:  python listar_departamentos.py
Saída:       departamentos.md
"""
import os
from datetime import datetime

from conferir_vendas import numero, reais
from explorar_banco import PASTA, carregar_env, conectar, consultar, tabela_md, texto

VENDA = "m.operacao = 'S' AND NVL(m.status, '-') <> 'C'"  # mesmo filtro validado com o Cefas


def main():
    carregar_env()
    schema = os.environ.get("ORA_SCHEMA", "JP").upper()
    if not schema.isalnum():
        raise SystemExit("ORA_SCHEMA inválido no .env")
    conexao, _ = conectar()

    print("Vendas por ano...")
    anos = consultar(conexao, f"""
        SELECT TO_CHAR(m.dtmov, 'YYYY'), MIN(m.dtmov), MAX(m.dtmov), COUNT(DISTINCT TRUNC(m.dtmov)),
               SUM(m.qt * m.punit)
        FROM {schema}.movimentacao m WHERE {VENDA} GROUP BY TO_CHAR(m.dtmov, 'YYYY') ORDER BY 1""")

    print("Departamentos...")
    deptos = consultar(conexao, f"""
        SELECT d.codepto, d.departamento, v.produtos, v.valor
        FROM {schema}.depto d
        LEFT JOIN (SELECT p.codepto, COUNT(DISTINCT p.codprod) produtos, SUM(m.qt * m.punit) valor
                   FROM {schema}.movimentacao m JOIN {schema}.produto p ON p.codprod = m.codprod
                   WHERE m.dtmov >= TRUNC(SYSDATE) - 28 AND {VENDA} GROUP BY p.codepto) v
               ON v.codepto = d.codepto
        ORDER BY v.valor DESC NULLS LAST, d.codepto""")
    conexao.close()

    md = [f"# Departamentos e histórico – schema {schema}\n", f"Gerado em {datetime.now():%d/%m/%Y %H:%M}\n",
          "## Vendas por ano (MOVIMENTACAO)\n",
          tabela_md(["Ano", "Primeira venda", "Última venda", "Dias com venda", "Valor"],
                    [(a, f"{ini:%d/%m/%Y}", f"{fim:%d/%m/%Y}", texto(dias), reais(valor)) for a, ini, fim, dias, valor in anos]),
          "\n## Departamentos (vendas dos últimos 28 dias)\n",
          tabela_md(["Código", "Departamento", "Produtos vendidos", "Valor"],
                    [(c, nome, texto(prods or 0), reais(valor or 0)) for c, nome, prods, valor in deptos])]
    saida = PASTA / "departamentos.md"
    saida.write_text("\n".join(md), encoding="utf-8")
    print(f"\nPronto! Relatório salvo em: {saida}")


if __name__ == "__main__":
    main()

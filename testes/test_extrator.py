"""Teste do extrator com um Oracle de mentira e uma base SQLite temporária.  Rode:  python -m testes.test_extrator"""
import os
import sqlite3
import sys
import tempfile
from datetime import date, datetime
from pathlib import Path

from sistema import base_local, fornecedores
import extrator
from config import DEPTOS_FORA

d = datetime
VENDAS = [  # (dia, codprod, qtd, valor) que o "Oracle" devolve
    (d(2023, 12, 5), 1, 10.0, 100.0), (d(2026, 9, 30), 1, 5.0, 50.0), (d(2026, 10, 2), 2, 3.0, 30.0)]
ENTREGAS = [(1, 10, 200), (1, 20, 100), (99, 10, 50)]  # (codprod, codfornec, nº da entrada); o 99 não está na base
consultas = []


class Cursor:
    def __enter__(self): return self
    def __exit__(self, *a): pass

    def execute(self, sql, p):
        s = " ".join(sql.split()).upper()
        assert s.startswith("SELECT"), s
        consultas.append((s, p))
        if "FROM JP.DEPTO" in s: self.r = [("102", "MERCEARIA BASICA"), ("200", "ACOUGUE")]
        elif "FROM JP.PRODUTO P WHERE" in s:
            assert set(DEPTOS_FORA) <= set(p.values()), "os departamentos fora precisam ir como parâmetro"
            self.r = [(1, "DETERGENTE YPE LIMAO", "UN", "106", "1", "1", "1", 789, None), (2, None, "KG", "102", None, None, None, None, d(2025, 1, 1))]
        elif "FROM JP.FORNECEDOR" in s: self.r = [(10, " ype  ltda", "ANA", "11999990000", None), (20, None, None, None, None)]
        elif "FROM JP.DADOSTEMPENT" in s: self.r = ENTREGAS
        else: self.r = [l for l in VENDAS if p["ini"] <= l[0].date() < p["fim"]]
    def fetchall(self): return self.r


class Oracle:
    def cursor(self): return Cursor()
    def cancel(self): pass
    def close(self): pass


tmp = Path(tempfile.mkdtemp())
base_local.ARQUIVO_BASE = tmp / "dados" / "teste.db"
extrator.abrir = base_local.abrir
extrator.conectar = lambda: (Oracle(), "thin")
(tmp / ".env").write_text("ORA_USER=x\nORA_PASS=x\nORA_DSN=x\n")
os.environ.update(ORA_USER="x", ORA_PASS="x", ORA_DSN="x")
sys.argv = ["extrator.py"]


def sql(consulta):
    return sqlite3.connect(base_local.ARQUIVO_BASE).execute(consulta).fetchall()


# 1ª carga: tudo desde dez/2023
extrator.main()
assert sql("SELECT COUNT(*), SUM(valor) FROM vendas_diarias") == [(3, 180.0)]
assert sql("SELECT codepto, entra FROM departamentos ORDER BY 1") == [("102", 1), ("200", 0)]
assert sql("SELECT COUNT(*) FROM produtos WHERE familia_id IS NULL") == [(0,)]
assert sql("SELECT nome FROM familias ORDER BY id") == [("DETERGENTE YPE",), ("PRODUTO 2",)]  # tipo + marca; descrição vazia não quebra

assert sql("SELECT f.nome, f.telefone FROM produto_fornecedores pf JOIN fornecedores f ON f.id = pf.fornecedor_id ORDER BY 1") == [
    ("FORNECEDOR 20", None), ("YPE LTDA", "11999990000")]
con = sqlite3.connect(base_local.ARQUIVO_BASE)
escolha, _ = fornecedores.escolhidos(con, date(2026, 10, 5))
assert con.execute("SELECT nome FROM fornecedores WHERE id = ?", (escolha[1],)).fetchone() == ("YPE LTDA",)  # o último que entregou

# Comprador tira o FORNECEDOR 20 do produto 1 e digita outro telefone para a YPE: a próxima carga respeita os dois
con.execute("DELETE FROM produto_fornecedores WHERE fornecedor_id = (SELECT id FROM fornecedores WHERE nome = 'FORNECEDOR 20')")
con.execute("UPDATE fornecedores SET telefone = '123' WHERE nome = 'YPE LTDA'"); con.commit(); con.close()
ENTREGAS.append((2, 10, 300))

# Comprador junta o produto 2 na família do 1; nova carga não pode desfazer isso
con = sqlite3.connect(base_local.ARQUIVO_BASE)
con.execute("UPDATE produtos SET familia_id = 1 WHERE codprod = 2"); con.commit(); con.close()

# 2ª carga (diária): chega uma venda nova e uma antiga é refeita; o mês de 2023 não deve ser consultado de novo
VENDAS.append((d(2026, 10, 3), 2, 4.0, 40.0))
VENDAS[1] = (d(2026, 9, 30), 1, 6.0, 60.0)
consultas.clear()
extrator.main()
datas = [p["ini"] for s, p in consultas if "MOVIMENTACAO" in s]
assert min(datas).isoformat() == "2026-09-29" and len(datas) == 2, datas  # 3 dias antes da última venda (02/10)
assert sql("SELECT COUNT(*), SUM(valor) FROM vendas_diarias") == [(4, 230.0)]  # sem duplicar; 60 no lugar de 50
assert sql("SELECT familia_id FROM produtos WHERE codprod = 2") == [(1,)]
assert sql("SELECT pf.codprod, f.nome, f.telefone FROM produto_fornecedores pf JOIN fornecedores f ON f.id = pf.fornecedor_id ORDER BY 1") == [
    (1, "YPE LTDA", "123"), (2, "YPE LTDA", "123")]
print("OK")

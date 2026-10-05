"""Teste do extrator com um Oracle de mentira e uma base SQLite temporária.  Rode:  python test_extrator.py"""
import os
import sqlite3
import sys
import tempfile
from datetime import datetime
from pathlib import Path

import base_local
import extrator
from config import DEPTOS_FORA

d = datetime
VENDAS = [  # (dia, codprod, qtd, valor) que o "Oracle" devolve
    (d(2023, 12, 5), 1, 10.0, 100.0), (d(2026, 9, 30), 1, 5.0, 50.0), (d(2026, 10, 2), 2, 3.0, 30.0)]
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
assert sql("SELECT nome FROM familias ORDER BY id") == [("DETERGENTE YPE LIMAO",), ("PRODUTO 2",)]  # descrição vazia não quebra

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
print("OK")

"""Teste da lista de alerta com vendas inventadas.  Rode:  python test_alertas.py"""
import tempfile
from datetime import date, timedelta
from pathlib import Path

import alertas
import base_local

FIM = date(2026, 9, 30)  # último dia com venda na base
base_local.ARQUIVO_BASE = Path(tempfile.mkdtemp()) / "teste.db"
base = base_local.abrir()
base.execute("INSERT INTO departamentos VALUES ('106', 'LIMPEZA', 1)")
base.executemany("INSERT INTO produtos (codprod, descricao, codepto, dtexclusao) VALUES (?, ?, '106', ?)",
                 [(c, f"PRODUTO {c}", "2026-01-01" if c == 4 else None) for c in range(1, 11)])


def vender(codprod, de, ate, cada=1):
    """Uma venda a cada `cada` dias, de `de` até `ate` dias antes do FIM."""
    base.executemany("INSERT INTO vendas_diarias VALUES (?, ?, 1, 1)",
                     [((FIM - timedelta(days=d)).isoformat(), codprod) for d in range(ate, de + 1, cada)])


vender(1, 400, 10)        # vendia todo dia, parou há 10 dias: alerta
vender(2, 400, 0)         # vende todo dia: sem alerta
vender(3, 400, 10, 21)    # vende de 3 em 3 semanas: não é "toda semana", sem alerta
vender(4, 400, 10)        # excluído no Cefas: sem alerta
for c in (5, 6, 7, 8):
    vender(c, 400, 10)
vender(9, 40, 10)         # produto novo (vendeu 5 das 6 semanas desde o lançamento) que parou: alerta
vender(10, 24, 10)        # só 3 semanas de venda: pouco histórico, sem alerta
alertas.marcar(base, 5, "descontinuado", FIM - timedelta(days=5))   # marcado depois da parada: some
alertas.marcar(base, 6, "descontinuado", FIM - timedelta(days=20))  # marcado antes de vender de novo: marca vencida
alertas.marcar(base, 7, "comprado", FIM - timedelta(days=2))        # comprado há 2 dias: espera chegar
alertas.marcar(base, 8, "comprado", FIM - timedelta(days=8))        # comprado há 8 dias e nada: volta

lista = {a["codprod"]: a for a in alertas.listar(base)}
assert sorted(lista) == [1, 6, 8, 9], sorted(lista)
assert lista[1]["dias_sem_venda"] == 10 and lista[1]["semanas_total"] == 52 and lista[1]["departamento"] == "LIMPEZA"
assert lista[6]["status"] is None and lista[8]["status"] == "comprado"
assert (lista[9]["semanas_com_venda"], lista[9]["semanas_total"]) == (5, 6)

try:
    alertas.marcar(base, 1, "qualquer")
    raise AssertionError("status inválido deveria dar erro")
except ValueError:
    pass
print("OK")

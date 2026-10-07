"""Teste do acompanhamento (sugerido x comprador x vendeu).  Rode:  python test_acompanhamento.py"""
import tempfile
from datetime import date, timedelta
from pathlib import Path

import base_local

base_local.ARQUIVO_BASE = Path(tempfile.mkdtemp()) / "teste.db"
import acompanhamento as acomp  # noqa: E402

base = base_local.abrir()
base.execute("INSERT INTO departamentos VALUES ('102', 'MERCEARIA', 1)")
base.executemany("INSERT INTO familias (id, nome) VALUES (?, ?)", [(1, "ARROZ"), (2, "FEIJAO"), (3, "SAGU"), (4, "CRAVO")])
base.executemany("INSERT INTO produtos (codprod, descricao, unidade, codepto, familia_id) VALUES (?, ?, 'UN', '102', ?)",
                 [(1, "ARROZ 5KG", 1), (2, "FEIJAO 1KG", 2), (3, "FEIJAO 2KG", 2), (4, "SAGU", 3), (5, "CRAVO", 4)])
semana, aberta = date(2026, 10, 5), date(2026, 10, 12)
dias = [(semana + timedelta(days=i)).isoformat() for i in range(7)]
base.executemany("INSERT INTO vendas_diarias VALUES (?, ?, ?, 0)",
                 [(d, 1, 10) for d in dias] + [(d, 2, 10) for d in dias] + [(d, 3, 4) for d in dias[:5]]
                 + [("2026-10-12", 1, 10)])
base.executemany("INSERT INTO sugestoes VALUES (?, ?, ?, ?)", [
    (semana.isoformat(), 1, 70, 75),     # vendeu 70: sistema acertou, comprador mudou para pior
    (semana.isoformat(), 2, 70, 90),     # vendeu 90 (dois produtos): sistema errou -22%, comprador acertou
    (semana.isoformat(), 3, 10, None),   # não vendeu nada; comprador não revisou
    (semana.isoformat(), 4, 1, None),    # sugeriu 1, não vendeu: dentro de 1 unidade, conta como acerto
    (aberta.isoformat(), 1, 70, None)])  # semana ainda não terminou
base.commit()

assert acomp.semanas_fechadas(base) == [semana]
linhas = {l["nome"]: l for l in acomp.comparar(base, semana)}
assert [l["nome"] for l in acomp.comparar(base, semana)] == ["CRAVO", "SAGU", "FEIJAO", "ARROZ"]  # não vendeu, maior erro, ...
assert linhas["ARROZ"]["acertou"] and linhas["ARROZ"]["erro"] == 0 and linhas["ARROZ"]["mais_perto"] == "sistema"
assert linhas["FEIJAO"]["vendeu"] == 90 and not linhas["FEIJAO"]["acertou"] and linhas["FEIJAO"]["mais_perto"] == "comprador"
assert round(linhas["FEIJAO"]["erro"], 1) == -22.2
assert linhas["CRAVO"]["acertou"] and linhas["CRAVO"]["erro"] is None and not linhas["SAGU"]["acertou"]
assert linhas["SAGU"]["erro"] is None and not linhas["SAGU"]["alterou"] and linhas["SAGU"]["mais_perto"] is None

r = acomp.resumo(list(linhas.values()))
assert r == {"familias": 4, "acertos": 2, "alteradas": 2, "comprador_mais_perto": 1, "sistema_mais_perto": 1}, r
[d] = acomp.por_departamento(list(linhas.values()))
assert d["acertos"] == 2 and d["familias"] == 4 and d["sem_venda"] == 2 and round(d["erro_tipico"], 1) == -11.1  # mediana de 0 e -22,2
print("OK")

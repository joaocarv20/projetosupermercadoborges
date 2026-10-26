"""Teste do motor com vendas inventadas, em que a resposta certa é conhecida.  Rode:  python -m testes.test_motor"""
import tempfile
from datetime import date, timedelta
from pathlib import Path

from sistema import base_local
from sistema import motor
from sistema.calendario import tipo_semana

# --- tipo de cada semana (segunda a domingo) ---
assert tipo_semana(date(2026, 10, 5)) == "salario"      # dias 5, 6 e 7 (5º dia útil) + ...
assert tipo_semana(date(2026, 10, 12)) == "feriado"     # Nossa Senhora Aparecida
assert tipo_semana(date(2026, 10, 19)) == "recarga"     # dia 20
assert tipo_semana(date(2026, 10, 26)) == "salario"     # 30, 31 e 1º: último dia útil + fim de semana
assert tipo_semana(date(2026, 8, 10)) == "meio"
assert tipo_semana(date(2026, 8, 24)) == "fraca"        # 31/08, o último dia útil, cai na semana seguinte

# --- base com 2 anos de vendas: cada tipo de semana vende um valor diferente por dia ---
VENDA_DIA = {"salario": 20, "recarga": 12, "meio": 10, "fraca": 7, "feriado": 8}
base_local.ARQUIVO_BASE = Path(tempfile.mkdtemp()) / "teste.db"
base = base_local.abrir()
base.execute("INSERT INTO departamentos VALUES ('102', 'MERCEARIA BASICA', 1)")
base.executemany("INSERT INTO familias (id, nome) VALUES (?, ?)", [(1, "ARROZ"), (2, "FRANGO KG"), (3, "DETERGENTE"), (4, "NOVO")])
base.executemany("INSERT INTO produtos (codprod, descricao, unidade, codepto, familia_id) VALUES (?, ?, ?, '102', ?)",
                 [(1, "ARROZ 5KG", "UN", 1), (2, "FRANGO KG", "KG", 2), (3, "DETERGENTE LIMAO", "UN", 3),
                  (4, "DETERGENTE COCO", "UN", 3), (7, "PRODUTO NOVO", "UN", 4)])
vendas, dia = [], date(2024, 1, 1)  # uma segunda-feira
while dia <= date(2026, 9, 30):
    vendas += [(dia.isoformat(), 1, VENDA_DIA[tipo_semana(dia - timedelta(days=dia.weekday()))], 0),
               (dia.isoformat(), 2, 1.2, 0), (dia.isoformat(), 3, 10, 0), (dia.isoformat(), 4, 5, 0)]
    if dia >= date(2026, 8, 31):  # produto lançado em 31/08
        vendas.append((dia.isoformat(), 7, 10, 0))
    dia += timedelta(days=1)
base.executemany("INSERT INTO vendas_diarias VALUES (?, ?, ?, ?)", vendas)
base.commit()

# --- sugestão para a semana de salário de 05/10/2026 ---
alvo = date(2026, 10, 5)
equivalentes = motor.semanas_equivalentes(base, alvo)
assert len(equivalentes) == 6 and all(tipo_semana(s) == "salario" and s < alvo for s in equivalentes)

r = {x["nome"]: x for x in motor.gerar(base, alvo)}
assert r["ARROZ"]["sugestao"] == 140 and r["ARROZ"]["semanas_usadas"] == 6   # 20 por dia x 7, sem ruído de decimais
assert r["ARROZ"]["departamento"] == "MERCEARIA BASICA"
assert r["FRANGO KG"]["sugestao"] == 8.4                                      # quilos com 1 casa
assert r["DETERGENTE"]["sugestao"] == 105                                     # sabores somam na família
assert [(p["descricao"], p["qtd"]) for p in r["DETERGENTE"]["produtos"]] == [("DETERGENTE LIMAO", 70), ("DETERGENTE COCO", 35)]
assert r["NOVO"]["sugestao"] == 70 and r["NOVO"]["semanas_usadas"] == 1       # semanas antes do lançamento não contam como zero
tipo_ano_passado = tipo_semana(date(2025, 10, 6))                             # mesma semana, 52 semanas antes
assert r["ARROZ"]["ano_passado"] == 7 * VENDA_DIA[tipo_ano_passado]

# semana com feriado só olha semanas com feriado
r = {x["nome"]: x for x in motor.gerar(base, date(2026, 10, 12))}
assert r["ARROZ"]["sugestao"] == 56 and r["ARROZ"]["semanas_usadas"] >= 3

# dia atípico tira a semana inteira da comparação
base.execute("INSERT INTO calendario (data, tipo, atipico) VALUES (?, 'meio', 1)", ((equivalentes[0] + timedelta(days=2)).isoformat(),))
depois = motor.semanas_equivalentes(base, alvo)
assert equivalentes[0] not in depois and len(depois) == 6

# --- período de qualquer dia a qualquer dia ---
peso = motor.peso_dos_dias(base)
assert len(peso) == 7 and round(sum(peso), 9) == 1
semana_toda = {x["nome"]: x for x in motor.gerar_periodo(base, alvo, alvo + timedelta(days=6))}
for x in motor.gerar(base, alvo):                                             # de segunda a domingo = a semana de sempre
    y = semana_toda[x["nome"]]
    assert (y["sugestao"], y["mediana"], y["ano_passado"], y["semanas_usadas"]) == (
        x["sugestao"], x["mediana"], x["ano_passado"], x["semanas_usadas"]), x["nome"]
    assert [(p["codprod"], p["qtd"]) for p in y["produtos"]] == [(p["codprod"], p["qtd"]) for p in x["produtos"]]
# de sábado 10/10 (semana de salário, 140 por semana) a terça 13/10 (semana do feriado, 56): cada uma com a sua parte
import math
r = {x["nome"]: x for x in motor.gerar_periodo(base, date(2026, 10, 10), date(2026, 10, 13))}
assert r["ARROZ"]["sugestao"] == math.ceil(round(140 * (peso[5] + peso[6]) + 56 * (peso[0] + peso[1]), 6))
assert r["ARROZ"]["ano_passado"] == sum(VENDA_DIA[tipo_semana(d - timedelta(days=d.weekday()))]
                                        for d in (date(2025, 10, 11) + timedelta(days=i) for i in range(4)))
assert [p["descricao"] for p in r["DETERGENTE"]["produtos"]] == ["DETERGENTE LIMAO", "DETERGENTE COCO"]
assert round(r["DETERGENTE"]["produtos"][0]["pct"], 6) == round(200 / 3, 6)  # 10 de 15 por dia
assert motor.partes_do_periodo(base, alvo, alvo + timedelta(days=13)) == {alvo: 1, alvo + timedelta(weeks=1): 1}

# gravar: o que o comprador digitou (qtd_final) sobrevive a uma nova sugestão do mesmo período
fim = alvo + timedelta(days=6)
linhas = motor.gerar(base, alvo)
motor.gravar(base, alvo, fim, linhas)
base.execute("UPDATE sugestoes SET qtd_final = 150 WHERE familia_id = 1"); base.commit()
motor.gravar(base, alvo, fim, linhas)
assert base.execute("SELECT qtd_sugerida, qtd_final, fim FROM sugestoes WHERE familia_id = 1").fetchone() == (140, 150, fim.isoformat())
assert base.execute("SELECT COUNT(*) FROM sugestoes").fetchone() == (len(linhas),)
# outro fim para o mesmo início troca o período salvo (fica um período por dia de início)
motor.gravar(base, alvo, alvo + timedelta(days=2), motor.gerar_periodo(base, alvo, alvo + timedelta(days=2)))
assert base.execute("SELECT qtd_final, fim FROM sugestoes WHERE familia_id = 1").fetchone() == (None, "2026-10-07")

# base de antes do período: a coluna fim é criada e preenchida com o domingo da semana
import sqlite3
antiga = Path(tempfile.mkdtemp()) / "antiga.db"
c = sqlite3.connect(antiga)
c.execute("CREATE TABLE sugestoes (semana TEXT NOT NULL, familia_id INTEGER NOT NULL, qtd_sugerida REAL, qtd_final REAL, PRIMARY KEY (semana, familia_id))")
c.execute("INSERT INTO sugestoes VALUES ('2026-10-05', 1, 70, 75)"); c.commit(); c.close()
base_local.ARQUIVO_BASE = antiga
assert base_local.abrir().execute("SELECT fim FROM sugestoes").fetchone() == ("2026-10-11",)
assert base_local.abrir().execute("SELECT fim FROM sugestoes").fetchone() == ("2026-10-11",)   # 2ª vez não quebra

assert motor.proxima_segunda(date(2026, 10, 5)) == date(2026, 10, 12)  # hoje é segunda: a compra é para a semana seguinte
assert motor.proxima_segunda(date(2026, 10, 9)) == date(2026, 10, 12)
print("OK")

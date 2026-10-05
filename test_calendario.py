"""Teste do calendário.  Rode:  python test_calendario.py"""
import sqlite3
import tempfile
from datetime import date
from pathlib import Path

import base_local
import calendario as c

# Outubro/2026: 5º dia útil = 07/10; último dia útil = 30/10; 12/10 é feriado (Aparecida)
assert c.tipos_do_dia(date(2026, 10, 1)) == ["salario", "recarga"]
assert c.tipos_do_dia(date(2026, 10, 7)) == ["salario"] and c.tipos_do_dia(date(2026, 10, 8)) == []
assert c.tipos_do_dia(date(2026, 10, 12)) == ["feriado"]
assert c.tipos_do_dia(date(2026, 10, 20)) == ["recarga"]
assert c.tipos_do_dia(date(2026, 10, 26)) == ["fraca"] and c.tipos_do_dia(date(2026, 10, 30)) == ["salario"]

# Feriados: nacionais, Carnaval, Corpus Christi e Anápolis; funciona para qualquer ano
assert c.feriado(date(2026, 7, 31)) == "Aniversário de Anápolis" and c.feriado(date(2026, 7, 26)) == "Sant'Ana (Anápolis)"
assert c.feriado(date(2026, 2, 16)) == "Carnaval" and c.feriado(date(2026, 6, 4)) == "Corpus Christi"
assert c.feriado(date(2024, 12, 25)) == "Natal" and c.feriado(date(2027, 9, 7)) == "Independência do Brasil"
assert c.feriado(date(2026, 2, 18)) is None  # "Início da Quaresma" não é feriado

# Gravação na base: pode repetir sem duplicar e sem apagar a marca de dia atípico
base_local.ARQUIVO_BASE = Path(tempfile.mkdtemp()) / "teste.db"
base = base_local.abrir()
assert c.preencher(base, date(2026, 10, 1), date(2026, 10, 31)) == 31
base.execute("UPDATE calendario SET atipico = 1 WHERE data = '2026-10-20'"); base.commit()
c.preencher(base, date(2026, 10, 1), date(2026, 10, 31))
assert base.execute("SELECT COUNT(*) FROM calendario").fetchone() == (31,)
assert base.execute("SELECT tipo, feriado, atipico FROM calendario WHERE data = '2026-10-12'").fetchone() == ("meio", "Nossa Senhora Aparecida", 0)
assert base.execute("SELECT tipo, atipico FROM calendario WHERE data = '2026-10-20'").fetchone() == ("recarga", 1)
assert base.execute("SELECT tipo FROM calendario WHERE data = '2026-10-31'").fetchone() == ("salario",)
print("OK")

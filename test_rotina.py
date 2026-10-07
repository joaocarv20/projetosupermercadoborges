"""Teste do backup da rotina noturna.  Rode:  python test_rotina.py"""
import sqlite3
import tempfile
from datetime import date, timedelta
from pathlib import Path

import base_local
import rotina_noturna

pasta = Path(tempfile.mkdtemp())
base_local.ARQUIVO_BASE = pasta / "teste.db"
rotina_noturna.PASTA_BACKUP = pasta / "backups"
base = base_local.abrir()
base.execute("INSERT INTO usuarios VALUES ('paulo', 'x')")
base.commit()  # a base continua aberta, como fica com a tela no ar

dia = date(2026, 10, 1)
for i in range(20):
    destino = rotina_noturna.backup(dia + timedelta(days=i))
assert sqlite3.connect(destino).execute("SELECT usuario FROM usuarios").fetchone() == ("paulo",)
copias = sorted(p.name for p in rotina_noturna.PASTA_BACKUP.iterdir())
assert len(copias) == 14 and copias[0] == "borges-2026-10-07.db", copias  # só as 14 mais novas
print("ok")

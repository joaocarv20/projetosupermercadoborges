"""
Rotina de toda madrugada: copia as vendas do dia anterior do Cefas e faz o backup da base local.
O Agendador de Tarefas do Windows roda o rotina_noturna.bat, que chama este arquivo (ver INSTALACAO.md).

Para rodar na mão:  python rotina_noturna.py
"""
import sqlite3
import sys
from datetime import date
from pathlib import Path

import base_local
import extrator

PASTA_BACKUP = Path(__file__).parent / "backups"
BACKUPS_GUARDADOS = 14  # duas semanas; os mais antigos são apagados


def backup(hoje=None):
    """Cópia segura da base (a API de backup do SQLite funciona mesmo com a tela aberta)."""
    PASTA_BACKUP.mkdir(exist_ok=True)
    destino = PASTA_BACKUP / f"borges-{hoje or date.today():%Y-%m-%d}.db"
    origem, copia = sqlite3.connect(base_local.ARQUIVO_BASE), sqlite3.connect(destino)
    with copia:
        origem.backup(copia)
    origem.close()
    copia.close()
    for antigo in sorted(PASTA_BACKUP.glob("borges-*.db"))[:-BACKUPS_GUARDADOS]:
        antigo.unlink()
    return destino


if __name__ == "__main__":
    sys.argv = sys.argv[:1]  # o extrator só pega os últimos dias
    try:
        extrator.main()
    finally:  # backup mesmo se o Oracle falhar: a base de ontem continua valendo
        print(f"Backup: {backup()}")

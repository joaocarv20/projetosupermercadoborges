"""Base local (SQLite): onde ficam os dados já resumidos. É só um arquivo: o backup é copiá-lo."""
import sqlite3

from config import ARQUIVO_BASE

ESQUEMA = """
CREATE TABLE IF NOT EXISTS departamentos (
    codepto TEXT PRIMARY KEY, nome TEXT, entra INTEGER NOT NULL      -- entra = 1: usado na sugestão
);
-- Toda família tem pelo menos 1 produto. Produto novo ganha uma família só dele (nome = descrição);
-- depois dá para juntar sabores na mesma família sem perder o que o comprador já digitou.
CREATE TABLE IF NOT EXISTS familias (
    id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS produtos (
    codprod INTEGER PRIMARY KEY, descricao TEXT, unidade TEXT,       -- unidade: KG ou UN...
    codepto TEXT, codsec TEXT, codcat TEXT, codsubcat TEXT, codbarra INTEGER,
    dtexclusao TEXT,                                                 -- o Cefas quase nunca preenche
    familia_id INTEGER REFERENCES familias(id)
);
CREATE TABLE IF NOT EXISTS vendas_diarias (                          -- 1 linha por produto por dia
    data TEXT NOT NULL, codprod INTEGER NOT NULL, qtd REAL, valor REAL,
    PRIMARY KEY (data, codprod)
) WITHOUT ROWID;
CREATE TABLE IF NOT EXISTS calendario (
    data TEXT PRIMARY KEY, tipo TEXT, feriado TEXT, data_comercial TEXT, atipico INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS sugestoes (                               -- o que o sistema sugeriu x o que o comprador comprou
    semana TEXT NOT NULL, familia_id INTEGER NOT NULL, qtd_sugerida REAL, qtd_final REAL,
    PRIMARY KEY (semana, familia_id)
);
CREATE TABLE IF NOT EXISTS alertas (                                 -- status: verificar, comprado, descontinuado
    codprod INTEGER PRIMARY KEY, status TEXT NOT NULL, atualizado_em TEXT
);
CREATE TABLE IF NOT EXISTS usuarios (usuario TEXT PRIMARY KEY, senha_hash TEXT NOT NULL);
"""


def abrir():
    ARQUIVO_BASE.parent.mkdir(exist_ok=True)
    base = sqlite3.connect(ARQUIVO_BASE)
    base.executescript(ESQUEMA)
    return base

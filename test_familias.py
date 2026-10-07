"""Teste das famílias (regra, ajuste manual, planilha) e da divisão por sabor.  Rode:  python test_familias.py"""
import tempfile
from datetime import date
from pathlib import Path

import base_local
import motor

base_local.ARQUIVO_BASE = Path(tempfile.mkdtemp()) / "teste.db"
import familias as fam  # noqa: E402

# Regra: tipo + marca + tamanho
for descricao, esperado in [
        ("SAB PALMOLIVE SUAVE HID INTENSIVA 85G", "SAB PALMOLIVE 85G"),
        ("SAB LIQ PROTEX AVEIA 250ML", "SAB LIQ PROTEX 250ML"),         # LIQ não é marca
        ("CREME DE LEITE ITALAC 200G", "CREME DE LEITE ITALAC 200G"),
        ("LIMP PERF CASAFLOR INTUITIVE 1LT", "LIMP PERF CASAFLOR 1L"),   # 1LT = 1L
        ("CAFE 3 CORACOES 500 G", "CAFE 3 500G"),                       # tamanho separado
        ("SAB PROTEX COMPLETE 12 85G", "SAB PROTEX 85G"),               # o 12 não gruda no 85G
        ("PAPEL HIG PERSONAL NEUTRO VIP 4X30M", "PAPEL HIG PERSONAL 4X30M"),
        ("DETERGENTE YPE LIMAO", "DETERGENTE YPE"),
        ("ARROZ", "ARROZ")]:
    assert fam.chave(descricao) == esperado, (descricao, fam.chave(descricao))

base = base_local.abrir()
base.execute("INSERT INTO departamentos VALUES ('106', 'HIGIENE', 1)")
base.executemany("INSERT INTO produtos (codprod, descricao, unidade, codepto) VALUES (?, ?, 'UN', '106')",
                 [(1, "SAB PALMOLIVE LAVANDA 85G"), (2, "SAB PALMOLIVE ROSAS 85G"), (3, "SAB PROTEX ERVA DOCE 85G")])
base.executemany("INSERT INTO vendas_diarias VALUES (?, ?, 1, 1)", [(date.today().isoformat(), c) for c in (1, 2, 3)])
fam.atribuir(base)
nomes = lambda: dict(base.execute("SELECT p.codprod, f.nome FROM produtos p JOIN familias f ON f.id = p.familia_id"))
assert nomes() == {1: "SAB PALMOLIVE 85G", 2: "SAB PALMOLIVE 85G", 3: "SAB PROTEX 85G"}

# Ajuste manual: separa o 2; o extrator (atribuir sem "todos") não desfaz
with base:
    fam.mover(base, [(2, " sab palmolive rosas ")])
fam.atribuir(base)
assert nomes()[2] == "SAB PALMOLIVE ROSAS"

# Planilha: exporta, "edita no Excel" (cp1252, vírgula) juntando o Protex no Palmolive, importa
planilha = fam.exportar(base)
assert planilha.startswith("﻿codigo;produto;departamento;familia") and "SAB PROTEX 85G" in planilha
editada = "codigo,produto,departamento,familia\r\n3,SAB PROTEX ERVA DOCE 85G,HIGIENE,SABONETES ÇA\r\n1,,,\r\n"
assert fam.importar(base, editada.encode("cp1252")) == 1                 # linha sem família é ignorada
assert nomes() == {1: "SAB PALMOLIVE 85G", 2: "SAB PALMOLIVE ROSAS", 3: "SABONETES ÇA"}
assert base.execute("SELECT COUNT(*) FROM familias").fetchone() == (3,)  # a família do Protex, vazia, foi apagada
try:
    fam.importar(base, b"a;b\n1;2\n")
    raise AssertionError("planilha sem as colunas deveria dar erro")
except ValueError:
    pass

# Quanto comprar de cada sabor: soma exatamente a quantidade da família
assert motor.dividir(40, [5, 3, 2, 0.5], "UN") == [19, 11, 8, 2]
assert motor.dividir(7, [1, 1, 1], "UN") == [3, 2, 2]
assert motor.dividir(10, [0, 0], "UN") == [0, 0]
assert motor.dividir(3, [1, 2], "KG") == [1.0, 2.0]
print("OK")

"""
Famílias de produto: os sabores/variações de uma mesma marca e tamanho viram uma linha só na sugestão.

O Cefas não preenche subcategoria, então a família sai da descrição: tipo + marca + tamanho.
    SAB PALMOLIVE SUAVE HID INTENSIVA 85G  ->  SAB PALMOLIVE 85G
    SAB LIQ PROTEX AVEIA 250ML             ->  SAB LIQ PROTEX 250ML   (LIQ não é marca: ver QUALIFICADORES)
O que a regra errar se corrige na tela Famílias ou pela planilha (exportar, editar no Excel, importar).
O extrator só dá família a produto novo: o que foi ajustado à mão não é desfeito.

Como rodar:  python familias.py agrupar              refaz TODAS as famílias pela regra (desfaz ajustes manuais)
             python familias.py exportar familias.csv
             python familias.py importar familias.csv
"""
import csv
import io
import re
import sys
from datetime import date, timedelta

from base_local import abrir
from config import QUALIFICADORES

# 85G, 7,5ML, 1KG, 2L, 96FL, 3PCS, 4X30M, 8X1...
TAMANHO = re.compile(r"^\d+([.,]\d+)?(G|GR|GRS|KG|ML|L|LT|LTS|M|MT|MTS|CM|MM|UN|UND|FL|F|PCS)$|^\d+X\d+[A-Z]*$")


def chave(descricao):
    """Nome da família: tipo (1ª palavra + qualificadores) + marca + tamanho."""
    palavras = descricao.upper().split()
    # "500 ML" separado vira "500ML"
    for i in range(len(palavras) - 1, 0, -1):
        if palavras[i - 1].isdigit() and palavras[i].isalpha() and TAMANHO.match(palavras[i - 1] + palavras[i]):
            palavras[i - 1:i + 1] = [palavras[i - 1] + palavras[i]]
    tamanho = next((p for p in reversed(palavras) if TAMANHO.match(p)), None)
    if tamanho:  # 1LT = 1L, 85GR = 85G
        tamanho = re.sub(r"(?<=\d)(GRS|GR|LTS|LT|MTS|MT|UND)$", lambda m: {"UND": "UN"}.get(m[1], m[1][0]), tamanho)
    nome = [p for p in palavras if not TAMANHO.match(p)]
    i = 1
    while i < len(nome) and nome[i] in QUALIFICADORES:
        i += 1
    return " ".join(nome[:i + 1] + ([tamanho] if tamanho else [])) or descricao


def mover(base, codprods_nomes):
    """[(codprod, nome da família)]: cria a família se não existe e apaga as que ficaram vazias. Sem commit."""
    pares = [(c, n.strip().upper()) for c, n in codprods_nomes if n and n.strip()]
    base.executemany("INSERT OR IGNORE INTO familias (nome) VALUES (?)", sorted({(n,) for _, n in pares}))
    base.executemany("UPDATE produtos SET familia_id = (SELECT id FROM familias WHERE nome = ?) WHERE codprod = ?",
                     [(n, c) for c, n in pares])
    base.execute("DELETE FROM familias WHERE id NOT IN (SELECT familia_id FROM produtos WHERE familia_id IS NOT NULL)")
    return len(pares)


def atribuir(base, todos=False):
    """Família pela regra para os produtos sem família (ou para todos, desfazendo os ajustes manuais)."""
    filtro = "" if todos else " WHERE familia_id IS NULL"
    produtos = base.execute("SELECT codprod, descricao FROM produtos" + filtro).fetchall()
    with base:
        return mover(base, [(c, chave(d)) for c, d in produtos])


def ativos(base):
    """Produtos que entram na sugestão e venderam no último ano: os que vale a pena revisar."""
    desde = (date.today() - timedelta(days=365)).isoformat()
    return base.execute(
        """SELECT p.codprod, p.descricao, d.nome, f.nome FROM produtos p
           JOIN departamentos d ON d.codepto = p.codepto JOIN familias f ON f.id = p.familia_id
           -- IN numa leitura só: vendas_diarias é ordenada por data, buscar produto a produto varre a tabela toda
           WHERE d.entra = 1 AND p.codprod IN (SELECT codprod FROM vendas_diarias WHERE data >= ?)
           ORDER BY d.nome, f.nome, p.descricao""", (desde,)).fetchall()


def exportar(base):
    """Planilha (CSV) dos produtos ativos com a família de cada um."""
    saida = io.StringIO()
    # Ponto e vírgula: é o separador que o Excel em português abre direto em colunas
    escrita = csv.writer(saida, delimiter=";")
    escrita.writerow(["codigo", "produto", "departamento", "familia"])
    escrita.writerows(ativos(base))
    return "\ufeff" + saida.getvalue()  # BOM: o Excel reconhece os acentos


def importar(base, dados):
    """Lê a planilha editada (bytes): só as colunas codigo e familia importam. Família vazia é ignorada."""
    try:
        texto = dados.decode("utf-8-sig")
    except UnicodeDecodeError:  # "CSV (separado por vírgulas)" do Excel no Windows grava em cp1252
        texto = dados.decode("cp1252")
    linhas = list(csv.DictReader(io.StringIO(texto), delimiter=";" if ";" in texto.split("\n", 1)[0] else ","))
    if not linhas or not {"codigo", "familia"} <= set(linhas[0]):
        raise ValueError("A planilha precisa das colunas 'codigo' e 'familia' (como sai no botão Baixar planilha).")
    pares = [(int(l["codigo"]), l["familia"]) for l in linhas if (l["codigo"] or "").strip().isdigit()]
    with base:
        return mover(base, pares)


if __name__ == "__main__":
    comando = sys.argv[1] if len(sys.argv) > 1 else ""
    base = abrir()
    if comando == "agrupar":
        print(f"{atribuir(base, todos=True)} produtos agrupados em "
              f"{base.execute('SELECT COUNT(*) FROM familias').fetchone()[0]} famílias.")
    elif comando == "exportar" and len(sys.argv) == 3:
        with open(sys.argv[2], "w", encoding="utf-8", newline="") as f:
            f.write(exportar(base))
        print(f"Planilha gravada em {sys.argv[2]}. Edite a coluna 'familia' e rode: python familias.py importar {sys.argv[2]}")
    elif comando == "importar" and len(sys.argv) == 3:
        try:
            print(f"{importar(base, open(sys.argv[2], 'rb').read())} produtos lidos da planilha.")
        except ValueError as erro:
            sys.exit(str(erro))
    else:
        sys.exit(__doc__)

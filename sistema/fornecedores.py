"""
Quem fornece cada produto. Um produto pode ter mais de um fornecedor: o Paulo escolhe na hora do pedido.

Por enquanto a ligação é feita à mão, na tela Fornecedores > Produtos ou pela planilha
(uma linha por produto e fornecedor; produto com 2 fornecedores aparece em 2 linhas).
"""
import csv
import io

from sistema.familias import ativos, ler_planilha


def nome_limpo(nome):
    return " ".join((nome or "").upper().split())


def ligar(base, codprods, nome):
    """Liga os produtos ao fornecedor cadastrado com esse nome. Sem commit."""
    linha = base.execute("SELECT id FROM fornecedores WHERE nome = ?", (nome_limpo(nome),)).fetchone()
    if not linha:
        raise ValueError(f"O fornecedor {nome_limpo(nome)} não está cadastrado. Cadastre antes na aba Cadastro.")
    base.executemany("INSERT OR IGNORE INTO produto_fornecedores VALUES (?, ?)", [(c, linha[0]) for c in codprods])


def por_produto(base):
    """{codprod: [(id do fornecedor, nome)]}, em ordem de nome."""
    resultado = {}
    for codprod, fid, nome in base.execute("""SELECT pf.codprod, f.id, f.nome FROM produto_fornecedores pf
                                              JOIN fornecedores f ON f.id = pf.fornecedor_id ORDER BY f.nome"""):
        resultado.setdefault(codprod, []).append((fid, nome))
    return resultado


def exportar(base):
    """Planilha (CSV) dos produtos ativos: uma linha por fornecedor; sem fornecedor, a coluna fica vazia."""
    ligados = por_produto(base)
    saida = io.StringIO()
    escrita = csv.writer(saida, delimiter=";")
    escrita.writerow(["codigo", "produto", "departamento", "familia", "fornecedor"])
    for codprod, descricao, depto, familia in ativos(base):
        for _, nome in ligados.get(codprod) or [(None, "")]:
            escrita.writerow([codprod, descricao, depto, familia, nome])
    return "﻿" + saida.getvalue()


def importar(base, dados):
    """Para cada produto da planilha, os fornecedores passam a ser exatamente os das linhas dele.
    Nome que não está cadastrado dá erro e nada é gravado (evita fornecedor duplicado por erro de digitação)."""
    linhas = ler_planilha(dados, ["codigo", "fornecedor"])
    novos = {}
    for l in linhas:
        if (l["codigo"] or "").strip().isdigit():
            nomes = novos.setdefault(int(l["codigo"]), set())
            if nome_limpo(l["fornecedor"]):
                nomes.add(nome_limpo(l["fornecedor"]))
    cadastrados = dict(base.execute("SELECT nome, id FROM fornecedores"))
    faltando = sorted({n for nomes in novos.values() for n in nomes} - set(cadastrados))
    if faltando:
        raise ValueError("Fornecedor não cadastrado: " + ", ".join(faltando[:5]) + (" ..." if len(faltando) > 5 else "")
                         + ". Cadastre antes ou corrija o nome na planilha. Nada foi gravado.")
    with base:
        base.executemany("DELETE FROM produto_fornecedores WHERE codprod = ?", [(c,) for c in novos])
        base.executemany("INSERT INTO produto_fornecedores SELECT codprod, ? FROM produtos WHERE codprod = ?",
                         [(cadastrados[n], c) for c, nomes in novos.items() for n in nomes])
    return len(novos)

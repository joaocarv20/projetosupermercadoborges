"""
Exploração da ESTRUTURA do banco Oracle do ERP (Cefas).

O que este script faz:
  - Conecta no Oracle com as credenciais do arquivo .env
  - Lê APENAS o dicionário de dados do Oracle (nomes de tabelas, colunas,
    chaves e views). NÃO lê nenhuma linha das tabelas do ERP.
  - Gera o relatório mapa_banco.md

Segurança:
  - Toda consulta passa pela função consultar(), que recusa qualquer comando
    que não comece com SELECT. Nenhum commit é feito.
  - Cada consulta tem tempo máximo (ORA_TIMEOUT_SEG no .env, padrão 60 s).

Como rodar:  python explorar_banco.py
Só as colunas de algumas tabelas (gera mapa_tabelas.md):
             python explorar_banco.py JP.PRODUTO JP.DEPTO SECAO
             (sem o "SCHEMA." procura a tabela em todos os schemas do ERP)
"""
import os
import sys
import threading
from datetime import datetime
from pathlib import Path

import oracledb

PASTA = Path(__file__).parent
ARQUIVO_SAIDA = PASTA / "mapa_banco.md"

# Schemas internos do Oracle, que não interessam (o ERP fica nos outros)
SCHEMAS_DO_SISTEMA = (
    "SYS", "SYSTEM", "OUTLN", "DBSNMP", "APPQOSSYS", "XDB", "CTXSYS", "MDSYS", "MDDATA",
    "ORDSYS", "ORDDATA", "ORDPLUGINS", "SI_INFORMTN_SCHEMA", "OLAPSYS", "WMSYS", "EXFSYS",
    "DVSYS", "DVF", "LBACSYS", "ANONYMOUS", "AUDSYS", "GSMADMIN_INTERNAL", "GSMCATUSER",
    "GSMUSER", "OJVMSYS", "SYSMAN", "MGMT_VIEW", "SPATIAL_CSW_ADMIN_USR",
    "SPATIAL_WFS_ADMIN_USR", "ORACLE_OCM", "XS$NULL", "DIP", "SYSBACKUP", "SYSDG", "SYSKM",
    "SYSRAC", "REMOTE_SCHEDULER_AGENT", "DBSFWUSER", "GGSYS", "OWBSYS", "OWBSYS_AUDIT",
    "TSMSYS", "PUBLIC", "SYS$UMF", "SCOTT",
)

# Palavras procuradas nos nomes de tabelas e colunas, por tema
TEMAS = {
    "Vendas": ["VENDA", "CUPOM", "PDV", "MOVIMENTO", "ITEM", "NFCE", "CAIXA"],
    "Produtos": ["PRODUTO", "EAN", "MERCADORIA", "ITEM", "DESCRICAO"],
    "Departamentos": ["DEPARTAMENTO", "SECAO", "GRUPO", "CATEGORIA", "FAMILIA"],
    "Fornecedores": ["FORNECEDOR", "PARCEIRO"],
}
MAX_CANDIDATAS_POR_TEMA = 40  # as mais prováveis primeiro; o resto é cortado


# ---------------------------------------------------------------------------
# Configuração e conexão
# ---------------------------------------------------------------------------
def carregar_env():
    """Lê o arquivo .env (linhas CHAVE=valor) para as variáveis de ambiente."""
    arquivo = PASTA / ".env"
    if not arquivo.exists():
        sys.exit("Arquivo .env não encontrado. Copie o .env.example para .env e preencha os dados.")
    for linha in arquivo.read_text(encoding="utf-8").splitlines():
        linha = linha.strip()
        if linha and not linha.startswith("#") and "=" in linha:
            chave, valor = linha.split("=", 1)
            os.environ.setdefault(chave.strip(), valor.strip().strip('"').strip("'"))
    faltando = [c for c in ("ORA_USER", "ORA_PASS", "ORA_DSN") if not os.environ.get(c)]
    if faltando:
        sys.exit(f"Preencha no .env: {', '.join(faltando)}")


def conectar():
    """Tenta o modo thin (sem instalar nada). Se o banco exigir, usa o modo thick."""
    dados = dict(user=os.environ["ORA_USER"], password=os.environ["ORA_PASS"],
                 dsn=os.environ["ORA_DSN"], tcp_connect_timeout=20)
    try:
        conexao = oracledb.connect(**dados)
        modo = "thin"
    except oracledb.Error as erro:
        # DPY-3010: versão do Oracle antiga demais para o thin (ex.: 11g)
        # DPY-3015: senha em formato antigo (10G)   DPY-3001: recurso só do thick
        if not any(codigo in str(erro) for codigo in ("DPY-3010", "DPY-3015", "DPY-3001")):
            raise
        print("\nO modo thin não funciona com este banco:")
        print(f"  {erro}")
        print("É preciso o Oracle Instant Client (modo thick).")
        pasta_client = os.environ.get("ORA_CLIENT_DIR")
        if not pasta_client:
            sys.exit("\nBaixe o Oracle Instant Client em\n"
                     "  https://www.oracle.com/database/technologies/instant-client/downloads.html\n"
                     "descompacte numa pasta e informe o caminho em ORA_CLIENT_DIR no .env.")
        print(f"Ativando o modo thick com o Instant Client em: {pasta_client}")
        # Obs.: no Linux o caminho deve estar também no LD_LIBRARY_PATH
        try:
            oracledb.init_oracle_client(lib_dir=pasta_client)
        except oracledb.Error as erro_client:
            sys.exit(f"Não consegui carregar o Instant Client em {pasta_client}:\n  {erro_client}")
        dados.pop("tcp_connect_timeout")  # parâmetro só existe no modo thin
        conexao = oracledb.connect(**dados)
        modo = "thick"

    return conexao, modo


def consultar(conexao, sql, parametros=None):
    """Executa uma consulta e devolve as linhas. Recusa tudo que não for SELECT."""
    if not sql.lstrip().upper().startswith("SELECT"):
        raise RuntimeError("Bloqueado: este script só executa SELECT.")
    # Tempo máximo: um cronômetro cancela a consulta se passar de ORA_TIMEOUT_SEG.
    # (call_timeout do oracledb não serve: no modo thick exige Instant Client 18+,
    #  e um Oracle 10g só aceita Instant Client 11.2 ou 12.1)
    cronometro = threading.Timer(int(os.environ.get("ORA_TIMEOUT_SEG", "60")), conexao.cancel)
    cronometro.start()
    try:
        with conexao.cursor() as cursor:
            cursor.execute(sql, parametros or {})
            return cursor.fetchall()
    except oracledb.DatabaseError as erro:
        if "ORA-01013" in str(erro):  # cancelada pelo cronômetro
            raise RuntimeError(f"Consulta cancelada: passou de {os.environ.get('ORA_TIMEOUT_SEG', '60')} segundos.") from erro
        raise
    finally:
        cronometro.cancel()


def escolher_dicionario(conexao):
    """Usa as views DBA_* (veem o banco todo) se houver permissão; senão ALL_*."""
    try:
        consultar(conexao, "SELECT 1 FROM dba_tables WHERE ROWNUM = 1")
        return "DBA"
    except oracledb.DatabaseError:  # ORA-00942 / ORA-01031: sem permissão
        return "ALL"


def filtro_owner(apelido):
    """Trecho SQL que exclui os schemas do sistema e a lixeira do Oracle."""
    lista = ", ".join(f"'{s}'" for s in SCHEMAS_DO_SISTEMA)
    return (f"{apelido}.owner NOT IN ({lista}) AND {apelido}.owner NOT LIKE 'APEX%' "
            f"AND {apelido}.owner NOT LIKE 'FLOWS%'")


# ---------------------------------------------------------------------------
# Formatação do Markdown
# ---------------------------------------------------------------------------
def texto(valor):
    if valor is None:
        return ""
    if isinstance(valor, datetime):
        return valor.strftime("%d/%m/%Y %H:%M")
    if isinstance(valor, float) and valor.is_integer():
        valor = int(valor)
    if isinstance(valor, int):
        return f"{valor:,}".replace(",", ".")  # 1.234.567
    return str(valor).replace("|", "\\|").replace("\n", " ")


def tabela_md(cabecalho, linhas):
    if not linhas:
        return "_Nada encontrado._\n"
    saida = ["| " + " | ".join(cabecalho) + " |", "|" + "---|" * len(cabecalho)]
    saida += ["| " + " | ".join(texto(v) for v in linha) + " |" for linha in linhas]
    return "\n".join(saida) + "\n"


def tipo_coluna(tipo, tamanho, precisao, escala):
    """Ex.: VARCHAR2(40), NUMBER(10,2), DATE."""
    if tipo == "NUMBER" and precisao is not None:
        return f"NUMBER({precisao},{escala})" if escala else f"NUMBER({precisao})"
    if tipo in ("VARCHAR2", "NVARCHAR2", "CHAR", "NCHAR", "RAW"):
        return f"{tipo}({tamanho})"
    return tipo


def temas_do_nome(nome):
    return ", ".join(tema for tema, palavras in TEMAS.items() if any(p in nome for p in palavras))


# ---------------------------------------------------------------------------
# Seções do relatório (cada uma devolve um trecho de Markdown)
# ---------------------------------------------------------------------------
def secao_versao(conexao, dic):
    try:
        linhas = consultar(conexao, "SELECT banner FROM v$version")
        return "\n".join(f"- {l[0]}" for l in linhas) + "\n"
    except oracledb.DatabaseError:
        linhas = consultar(conexao, "SELECT product, version, status FROM product_component_version")
        return tabela_md(["Produto", "Versão", "Status"], linhas)


def secao_schemas(conexao, dic):
    linhas = consultar(conexao, f"""
        SELECT t.owner, COUNT(*) FROM {dic}_tables t
        WHERE {filtro_owner('t')} AND t.table_name NOT LIKE 'BIN$%'
        GROUP BY t.owner ORDER BY COUNT(*) DESC""")
    return tabela_md(["Schema (owner)", "Qtd. de tabelas"], linhas)


def buscar_maiores_tabelas(conexao, dic):
    # ROWNUM em vez de FETCH FIRST para funcionar também no Oracle 11g
    return consultar(conexao, f"""
        SELECT * FROM (
            SELECT t.owner, t.table_name, t.num_rows, t.last_analyzed, c.comments
            FROM {dic}_tables t
            LEFT JOIN {dic}_tab_comments c ON c.owner = t.owner AND c.table_name = t.table_name
            WHERE {filtro_owner('t')} AND t.table_name NOT LIKE 'BIN$%' AND t.num_rows IS NOT NULL
            ORDER BY t.num_rows DESC
        ) WHERE ROWNUM <= 50""")


def secao_maiores(maiores):
    texto_md = ("NUM_ROWS é a quantidade de linhas estimada na última coleta de estatísticas "
                "(não é contagem em tempo real). Tabelas sem estatística não aparecem.\n\n")
    return texto_md + tabela_md(["#", "Owner", "Tabela", "Linhas (aprox.)", "Última estatística", "Tema provável"],
                                [(i, o, t, n, d, temas_do_nome(t)) for i, (o, t, n, d, _) in enumerate(maiores, 1)])


def buscar_tabelas_pedidas(conexao, dic, nomes):
    """Mesmo formato de buscar_maiores_tabelas, para as tabelas pedidas na linha de comando."""
    tabelas = []
    for nome in nomes:
        dono, _, tabela = nome.upper().rpartition(".")
        tabelas += consultar(conexao, f"""
            SELECT t.owner, t.table_name, t.num_rows, t.last_analyzed, c.comments
            FROM {dic}_tables t
            LEFT JOIN {dic}_tab_comments c ON c.owner = t.owner AND c.table_name = t.table_name
            WHERE {filtro_owner('t')} AND t.table_name = :tabela AND t.owner = NVL(:dono, t.owner)
            ORDER BY t.owner""", {"tabela": tabela, "dono": dono or None})
    return tabelas


def secao_colunas(conexao, dic, maiores):
    partes = []
    for owner, tabela, num_rows, _, comentario in maiores:
        linhas = consultar(conexao, f"""
            SELECT c.column_name, c.data_type, c.data_length, c.data_precision, c.data_scale,
                   c.nullable, cc.comments
            FROM {dic}_tab_columns c
            LEFT JOIN {dic}_col_comments cc
                   ON cc.owner = c.owner AND cc.table_name = c.table_name AND cc.column_name = c.column_name
            WHERE c.owner = :dono AND c.table_name = :tabela
            ORDER BY c.column_id""", {"dono": owner, "tabela": tabela})
        partes.append(f"### {owner}.{tabela} ({texto(num_rows)} linhas)\n")
        if comentario:
            partes.append(f"_Comentário: {texto(comentario)}_\n")
        partes.append(tabela_md(
            ["Coluna", "Tipo", "Aceita nulo", "Comentário"],
            [(nome, tipo_coluna(tp, tam, prec, esc), "sim" if nulo == "Y" else "não", com)
             for nome, tp, tam, prec, esc, nulo, com in linhas]))
    return "\n".join(partes)


def buscar_candidatas(conexao, dic):
    """Devolve {tema: [candidatas ordenadas]} procurando palavras-chave em nomes de tabelas e colunas."""
    todas = sorted({p for palavras in TEMAS.values() for p in palavras})
    cond_tabela = " OR ".join(f"t.table_name LIKE '%{p}%'" for p in todas)
    cond_coluna = " OR ".join(f"c.column_name LIKE '%{p}%'" for p in todas)

    por_nome = consultar(conexao, f"""
        SELECT t.owner, t.table_name, t.num_rows FROM {dic}_tables t
        WHERE {filtro_owner('t')} AND t.table_name NOT LIKE 'BIN$%' AND ({cond_tabela})""")
    por_coluna = consultar(conexao, f"""
        SELECT c.owner, c.table_name, c.column_name, t.num_rows
        FROM {dic}_tab_columns c
        JOIN {dic}_tables t ON t.owner = c.owner AND t.table_name = c.table_name
        WHERE {filtro_owner('c')} AND t.table_name NOT LIKE 'BIN$%' AND ({cond_coluna})""")

    resultado = {}
    for tema, palavras in TEMAS.items():
        achadas = {}  # (owner, tabela) -> dados da candidata
        for owner, tabela, num_rows in por_nome:
            if any(p in tabela for p in palavras):
                achadas[(owner, tabela)] = {"nome_bate": True, "colunas": [], "num_rows": num_rows}
        for owner, tabela, coluna, num_rows in por_coluna:
            if any(p in coluna for p in palavras):
                item = achadas.setdefault((owner, tabela), {"nome_bate": False, "colunas": [], "num_rows": num_rows})
                item["colunas"].append(coluna)
        # Mais provável primeiro: nome da tabela bate > mais colunas batem > mais linhas
        ordem = sorted(achadas.items(), key=lambda kv: (kv[1]["nome_bate"], len(kv[1]["colunas"]),
                                                        kv[1]["num_rows"] or 0), reverse=True)
        resultado[tema] = ordem
    return resultado


def secao_candidatas(candidatas):
    partes = [f"Busca por palavras-chave nos nomes das tabelas e das colunas. Ordem: primeiro as tabelas "
              f"cujo NOME bate, depois as com mais colunas que batem, depois as maiores. "
              f"Até {MAX_CANDIDATAS_POR_TEMA} por tema.\n"]
    for tema, ordem in candidatas.items():
        partes.append(f"### {tema}\n")
        partes.append(f"Palavras: {', '.join(TEMAS[tema])} — {len(ordem)} tabelas encontradas.\n")
        linhas = []
        for (owner, tabela), d in ordem[:MAX_CANDIDATAS_POR_TEMA]:
            colunas = ", ".join(d["colunas"][:6]) + (" …" if len(d["colunas"]) > 6 else "")
            linhas.append((owner, tabela, "sim" if d["nome_bate"] else "não", d["num_rows"], colunas))
        partes.append(tabela_md(["Owner", "Tabela", "Nome bate?", "Linhas (aprox.)", "Colunas que batem"], linhas))
    return "\n".join(partes)


def secao_chaves(conexao, dic, candidatas):
    conjunto = {chave for ordem in candidatas.values() for chave, _ in ordem[:MAX_CANDIDATAS_POR_TEMA]}
    linhas = consultar(conexao, f"""
        SELECT c.owner, c.table_name, cc.column_name, r.owner, r.table_name, rc.column_name, c.constraint_name
        FROM {dic}_constraints c
        JOIN {dic}_cons_columns cc ON cc.owner = c.owner AND cc.constraint_name = c.constraint_name
        JOIN {dic}_constraints r ON r.owner = c.r_owner AND r.constraint_name = c.r_constraint_name
        JOIN {dic}_cons_columns rc ON rc.owner = r.owner AND rc.constraint_name = r.constraint_name
                                   AND rc.position = cc.position
        WHERE c.constraint_type = 'R' AND {filtro_owner('c')}
        ORDER BY c.owner, c.table_name, c.constraint_name, cc.position""")
    # Mantém as chaves em que pelo menos uma das pontas é tabela candidata
    linhas = [l for l in linhas if (l[0], l[1]) in conjunto or (l[3], l[4]) in conjunto]
    aviso = ("Chaves estrangeiras em que pelo menos uma das tabelas é candidata.\n\n"
             "Se aparecer pouca coisa: muitos ERPs não declaram chaves estrangeiras no banco. "
             "Nesse caso, os relacionamentos aparecem por colunas com o mesmo nome "
             "(ex.: COD_PRODUTO em várias tabelas) — veja a seção 4.\n\n")
    return aviso + tabela_md(["Owner", "Tabela", "Coluna", "→ Owner", "→ Tabela", "→ Coluna", "Nome da chave"], linhas)


def secao_views(conexao, dic):
    linhas = consultar(conexao, f"""
        SELECT v.owner, v.view_name FROM {dic}_views v
        WHERE {filtro_owner('v')} ORDER BY v.owner, v.view_name""")
    return (f"{len(linhas)} views encontradas. A coluna \"Tema provável\" usa as mesmas palavras-chave.\n\n"
            + tabela_md(["Owner", "View", "Tema provável"], [(o, v, temas_do_nome(v)) for o, v in linhas]))


# ---------------------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------------------
def main():
    carregar_env()
    print(f"Conectando em {os.environ['ORA_DSN']} como {os.environ['ORA_USER']}...")
    try:
        conexao, modo = conectar()
    except oracledb.Error as erro:
        sys.exit(f"Falha ao conectar no Oracle:\n  {erro}\nConfira usuário, senha e ORA_DSN no .env.")
    dic = escolher_dicionario(conexao)
    print(f"Conectado (modo {modo}). Usando as views {dic}_*.")

    # Modo "só algumas tabelas": python explorar_banco.py JP.PRODUTO JP.DEPTO ...
    if len(sys.argv) > 1:
        tabelas = buscar_tabelas_pedidas(conexao, dic, sys.argv[1:])
        saida = PASTA / "mapa_tabelas.md"
        saida.write_text(f"# Colunas das tabelas pedidas\n\nGerado em {datetime.now():%d/%m/%Y %H:%M}\n\n"
                         + (secao_colunas(conexao, dic, tabelas) or "_Nenhuma tabela encontrada._\n"),
                         encoding="utf-8")
        conexao.close()
        print(f"\nPronto! {len(tabelas)} tabelas. Relatório salvo em: {saida}")
        return

    relatorio = [
        "# Mapa do banco Oracle – ERP Cefas\n",
        f"Gerado em {datetime.now():%d/%m/%Y %H:%M} · usuário {os.environ['ORA_USER']} · modo {modo}\n",
        f"**Dicionário usado: {dic}_\\*** — "
        + ("vê todos os schemas do banco." if dic == "DBA" else
           "o usuário não tem acesso às views DBA_\\*, então só aparece o que ele tem permissão de ver."),
        "\nSó metadados (estrutura). Nenhuma linha de dados do ERP foi lida.\n",
    ]

    def adicionar(titulo, funcao, *args):
        """Gera uma seção; se der erro (ex.: tempo esgotado), registra e continua."""
        print(f"  {titulo}...")
        try:
            corpo = funcao(*args)
        except (oracledb.Error, RuntimeError) as erro:
            corpo = f"> ⚠ Seção não gerada: {texto(erro)}\n"
            print(f"    erro: {erro}")
        relatorio.append(f"\n## {titulo}\n\n{corpo}")

    adicionar("1. Versão do Oracle", secao_versao, conexao, dic)
    adicionar("2. Schemas do ERP", secao_schemas, conexao, dic)

    # As seções 4 e 6 usam o resultado das seções 3 e 5 (ficam vazias se elas falharem)
    maiores, candidatas = [], {}

    def secao_3():
        maiores.extend(buscar_maiores_tabelas(conexao, dic))
        return secao_maiores(maiores)

    def secao_5():
        candidatas.update(buscar_candidatas(conexao, dic))
        return secao_candidatas(candidatas)

    adicionar("3. As 50 maiores tabelas", secao_3)
    adicionar("4. Colunas das 50 maiores tabelas", secao_colunas, conexao, dic, maiores)
    adicionar("5. Tabelas candidatas por tema", secao_5)
    adicionar("6. Chaves estrangeiras", secao_chaves, conexao, dic, candidatas)
    adicionar("7. Views", secao_views, conexao, dic)

    conexao.close()  # fecha sem commit (nada foi alterado)
    ARQUIVO_SAIDA.write_text("\n".join(relatorio), encoding="utf-8")
    print(f"\nPronto! Relatório salvo em: {ARQUIVO_SAIDA}")


if __name__ == "__main__":
    main()

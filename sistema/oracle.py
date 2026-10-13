"""
Conexão com o Oracle do Cefas, usada pelo extrator e pelas ferramentas.
Só executa SELECT, com tempo máximo por consulta (ORA_TIMEOUT_SEG no .env, padrão 60 s).
"""
import os
import sys
import threading
from pathlib import Path

import oracledb

ARQUIVO_ENV = Path(__file__).parent.parent / ".env"


def carregar_env():
    """Lê o arquivo .env (linhas CHAVE=valor) para as variáveis de ambiente."""
    arquivo = ARQUIVO_ENV
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


def reais(valor):
    """339123.4 -> 'R$ 339.123,40'."""
    if valor is None:
        return ""
    return "R$ " + f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def numero(valor):
    """Quantidades: sem casas se for inteiro, senão 3 casas (produtos pesados)."""
    if valor is None:
        return ""
    casas = 0 if float(valor).is_integer() else 3
    return f"{valor:,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".")

"""
Compras Inteligentes – Supermercado Borges. Lê a base local (SQLite) que o extrator preenche.

Para testar:  python app.py   e abra  http://127.0.0.1:5000
No mercado:   python app.py servir   (waitress, aberto na rede: http://IP-DO-COMPUTADOR:8000)
Criar ou trocar a senha de um usuário:  python app.py usuario paulo
"""
import calendar
import getpass
import os
import secrets
import sqlite3
import sys
import unicodedata
from datetime import date, timedelta
from functools import lru_cache

from flask import Flask, Response, abort, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from sistema import acompanhamento as acomp
from sistema import alertas as lista_alerta
from sistema import familias as fam
from sistema import fornecedores as forn
from sistema import base_local
from sistema import motor
from sistema.base_local import abrir
from sistema.calendario import feriado, tipo_semana, tipos_do_dia
from config import ACERTO_MARGEM, ACERTO_UNIDADES

app = Flask(__name__)
# Sem SECRET_KEY no ambiente, cada reinício do servidor pede login de novo
app.secret_key = os.environ.get("SECRET_KEY") or secrets.token_hex()

MESES = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho",
         "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

TIPOS_SEMANA = {
    "salario": {"nome": "Semana de salário", "cor": "vermelho"},
    "recarga": {"nome": "Recarga do cartão alimentação", "cor": "laranja"},
    "meio":    {"nome": "Meio do mês", "cor": "azul"},
    "fraca":   {"nome": "Semana fraca", "cor": "cinza"},
    "feriado": {"nome": "Semana com feriado", "cor": "roxo"},
}

STATUS_ALERTA = {"verificar": "Verificando", "comprado": "Já comprei", "descontinuado": "Descontinuado"}


# ---------------------------------------------------------------------------
# Formatação brasileira (usada nos templates)
# ---------------------------------------------------------------------------
@app.template_filter("br")
def numero_br(valor, casas=0):
    """1234.5 -> '1.234' (casas=0) ou '1.234,50' (casas=2)."""
    texto = f"{valor:,.{casas}f}"
    return texto.replace(",", "X").replace(".", ",").replace("X", ".")


@app.template_filter("data_br")
def data_br(d):
    """date(2026, 10, 5) -> '05/10/2026'."""
    return d.strftime("%d/%m/%Y")


def sem_acento(texto):
    """Para a busca achar 'acucar' quando o produto é 'Açúcar'."""
    return unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode().lower()


def variacao_pct(atual, anterior):
    """None quando não há base de comparação (a tela mostra um traço)."""
    return (atual - anterior) / anterior * 100 if anterior else None


@lru_cache(maxsize=16)
def _guardado(funcao, versao, *args):
    return funcao(abrir(), *args)


def com_cache(funcao, *args):
    """funcao(base, *args), guardada até a base mudar (extrator, quantidade salva, alerta marcado).
    O motor e a lista de alerta levam segundos com a base real; assim só a 1ª tela depois da mudança espera."""
    return _guardado(funcao, base_local.ARQUIVO_BASE.stat().st_mtime_ns, *args)


def rotulo_semana(segunda):
    return f"{segunda:%d/%m} a {segunda + timedelta(days=6):%d/%m/%Y}"


# ---------------------------------------------------------------------------
# Login
# ---------------------------------------------------------------------------
@app.before_request
def exigir_login():
    if request.endpoint not in ("login", "static") and "usuario" not in session:
        return redirect(url_for("login"))


@app.context_processor
def contador_alertas():
    """Número de alertas mostrado no menu lateral, em todas as telas."""
    if "usuario" not in session:
        return {}
    return {"total_alertas": len(com_cache(lista_alerta.listar))}


@app.route("/")
def inicio():
    return redirect(url_for("sugestao"))


@app.route("/login", methods=["GET", "POST"])
def login():
    erro = None
    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip().lower()
        linha = abrir().execute("SELECT senha_hash FROM usuarios WHERE usuario = ?", (usuario,)).fetchone()
        if linha and check_password_hash(linha[0], request.form.get("senha", "")):
            session["usuario"] = usuario
            return redirect(url_for("sugestao"))
        erro = "Usuário ou senha incorretos."
    return render_template("login.html", erro=erro)


@app.route("/sair")
def sair():
    session.clear()
    return redirect(url_for("login"))


# ---------------------------------------------------------------------------
# Telas
# ---------------------------------------------------------------------------
@app.route("/sugestao", methods=["GET", "POST"])
def sugestao():
    # Semanas do seletor: a da compra de hoje e as 3 seguintes
    primeira = motor.proxima_segunda(date.today())
    semanas = [primeira + timedelta(weeks=i) for i in range(4)]
    try:
        semana = date.fromisoformat(request.args.get("semana", ""))
    except ValueError:
        semana = primeira
    if semana.weekday() != 0:
        semana = primeira
    if semana not in semanas:
        semanas.append(semana)

    base = abrir()
    linhas = com_cache(motor.gerar, semana)

    if request.method == "POST":  # "Salvar": grava a sugestão e as quantidades finais digitadas
        motor.gravar(base, semana, linhas)
        finais = []
        for l in linhas:
            texto = request.form.get(f"qtd_{l['familia_id']}", "").strip().replace(",", ".")
            if not texto:
                continue
            try:
                qtd = float(texto)
            except ValueError:
                continue
            if qtd >= 0:
                finais.append((qtd, semana.isoformat(), l["familia_id"]))
        # Fornecedor escolhido, para os produtos com mais de um
        escolhas = [(p["codprod"], int(request.form[f"forn_{p['codprod']}"])) for l in linhas for p in l["produtos"]
                    if request.form.get(f"forn_{p['codprod']}", "").isdigit()]
        with base:
            base.executemany("UPDATE sugestoes SET qtd_final = ? WHERE semana = ? AND familia_id = ?", finais)
            forn.gravar_escolhas(base, semana, escolhas)
        if request.form.get("enviar", "").isdigit():  # "Mandar pedido": já salvou, agora abre o WhatsApp
            return mandar_pedido(base, semana, linhas, int(request.form["enviar"])) or redirect(request.full_path)
        return redirect(request.full_path)

    salvas = quantidades_salvas(base, semana)
    # Um departamento por vez: a lista inteira passa de 5 mil famílias e trava o navegador.
    # A busca procura em todos os departamentos.
    departamentos = sorted({l["departamento"] or "SEM DEPARTAMENTO" for l in linhas})
    departamento = request.args.get("departamento", "")
    if departamento not in departamentos:
        departamento = departamentos[0] if departamentos else ""
    busca = request.args.get("busca", "").strip()
    escolha, ligados = forn.escolhidos(base, semana)
    lista_fornecedores = base.execute("SELECT id, nome, telefone FROM fornecedores ORDER BY nome").fetchall()
    try:
        fornecedor = int(request.args.get("fornecedor", ""))
    except ValueError:
        fornecedor = None

    familias = []
    for l in linhas:
        # A busca e o fornecedor procuram em todos os departamentos (o pedido de um fornecedor passa por vários)
        if not (busca or fornecedor) and (l["departamento"] or "SEM DEPARTAMENTO") != departamento:
            continue
        if busca and sem_acento(busca) not in sem_acento(" ".join([l["nome"], *(p["descricao"] for p in l["produtos"])])):
            continue
        if fornecedor and fornecedor not in (escolha.get(p["codprod"]) for p in l["produtos"]):
            continue
        kg = l["unidade"] == "KG"
        final = salvas.get(l["familia_id"], l["sugestao"])
        # Quanto comprar de cada sabor: a quantidade final repartida pela venda de cada um
        comprar = motor.dividir(final, [p["qtd"] for p in l["produtos"]], l["unidade"])
        familias.append({
            **l, "un": "kg" if kg else "un", "casas": 1 if kg else 0,
            "produtos": [{**p, "comprar": c, "fornecedores": ligados.get(p["codprod"], []), "escolhido": escolha.get(p["codprod"])}
                         for p, c in zip(l["produtos"], comprar)],
            # Fornecedores escolhidos na família (mostrado na linha da família quando ela tem vários sabores)
            "de": sorted({n for p in l["produtos"] for fid, n in ligados.get(p["codprod"], []) if fid == escolha.get(p["codprod"])}),
            "qtd_final": int(final) if final == int(final) else final,  # 75 em vez de 75.0 no campo
            # Se um produto tem 80% ou mais da venda da família, provavelmente o caixa registra tudo nele
            "concentrado": len(l["produtos"]) > 1 and max(p["pct"] for p in l["produtos"]) >= 80,
        })

    dias = [semana + timedelta(days=i) for i in range(7)]
    obs = ", ".join(f"{feriado(d)} em {d:%d/%m}" for d in dias if feriado(d))
    return render_template(
        "sugestao.html", semana=semana, rotulo=rotulo_semana(semana), tipo=TIPOS_SEMANA[tipo_semana(semana)],
        obs=obs, semanas=[(s, rotulo_semana(s), TIPOS_SEMANA[tipo_semana(s)]["nome"]) for s in semanas],
        familias=familias, departamentos=departamentos, departamento=departamento, busca=busca,
        fornecedores=lista_fornecedores, fornecedor=fornecedor,
        escolhido=next((f for f in lista_fornecedores if f[0] == fornecedor), None))


def quantidades_salvas(base, semana):
    """{familia_id: quantidade final que o comprador salvou}."""
    return dict(base.execute("SELECT familia_id, qtd_final FROM sugestoes WHERE semana = ? AND qtd_final IS NOT NULL",
                             (semana.isoformat(),)))


def mandar_pedido(base, semana, linhas, fornecedor):
    """Redireciona para o WhatsApp com o que vai para o fornecedor: a quantidade salva de cada família,
    repartida pelos sabores como na tela, só dos sabores em que ele é o escolhido. None se não há nada a pedir."""
    linha = base.execute("SELECT telefone FROM fornecedores WHERE id = ?", (fornecedor,)).fetchone()
    if not linha:
        return None
    salvas, (escolha, _) = quantidades_salvas(base, semana), forn.escolhidos(base, semana)
    itens = []
    for l in linhas:
        final = salvas.get(l["familia_id"], l["sugestao"])
        casas, un = (1, "kg") if l["unidade"] == "KG" else (0, "un")
        for p, qtd in zip(l["produtos"], motor.dividir(final, [p["qtd"] for p in l["produtos"]], l["unidade"])):
            if qtd > 0 and escolha.get(p["codprod"]) == fornecedor:
                itens.append((p["descricao"], f"{numero_br(qtd, casas)} {un}"))
    return redirect(forn.link_pedido(linha[0], rotulo_semana(semana), sorted(itens))) if itens else None


@app.route("/alertas", methods=["GET", "POST"])
def alertas():
    base = abrir()
    if request.method == "POST":
        try:
            lista_alerta.marcar(base, int(request.form["codprod"]), request.form["status"])
        except (KeyError, ValueError):
            abort(400)
        return redirect(url_for("alertas"))
    return render_template("alertas.html", alertas=com_cache(lista_alerta.listar), status=STATUS_ALERTA)


@app.route("/familias", methods=["GET", "POST"])
def familias():
    base, erro = abrir(), None
    if request.method == "POST" and "planilha" in request.files:
        try:
            lidos = fam.importar(base, request.files["planilha"].read())
            return redirect(url_for("familias", importados=lidos))
        except ValueError as e:  # mostra o erro na própria tela
            erro = str(e)
    elif request.method == "POST":
        try:
            with base:
                fam.mover(base, [(int(request.form["codprod"]), request.form["familia"])])
        except (KeyError, ValueError):
            abort(400)
        return redirect(request.full_path)

    # Um departamento por vez; a busca procura em todos
    produtos = fam.ativos(base)
    departamentos = sorted({d for _, _, d, _ in produtos})
    departamento = request.args.get("departamento", "")
    if departamento not in departamentos:
        departamento = departamentos[0] if departamentos else ""
    busca = request.args.get("busca", "").strip()
    grupos = {}
    for codprod, descricao, depto, familia in produtos:
        if (sem_acento(busca) in sem_acento(f"{descricao} {familia}")) if busca else depto == departamento:
            grupos.setdefault(familia, []).append((codprod, descricao))
    return render_template("familias.html", grupos=grupos, departamentos=departamentos, departamento=departamento,
                           busca=busca, erro=erro, importados=request.args.get("importados"))


@app.route("/familias.csv")
def familias_planilha():
    return Response(fam.exportar(abrir()), mimetype="text/csv",
                    headers={"Content-Disposition": f"attachment; filename=familias-{date.today()}.csv"})


@app.route("/fornecedores", methods=["GET", "POST"])
def fornecedores():
    base, erro = abrir(), None
    if request.method == "POST" and "excluir" in request.form:
        with base:
            base.execute("DELETE FROM produto_fornecedores WHERE fornecedor_id = ?", (request.form["excluir"],))
            base.execute("DELETE FROM fornecedores WHERE id = ?", (request.form["excluir"],))
        return redirect(url_for("fornecedores"))

    if request.method == "POST":  # cadastrar (sem id) ou alterar (com id)
        atual = {c: request.form.get(c, "").strip() for c in ("id", "nome", "contato", "telefone", "email")}
        atual["nome"] = forn.nome_limpo(atual["nome"])
        if not atual["nome"]:
            abort(400)
        try:
            with base:
                dados = (atual["nome"], atual["contato"], atual["telefone"], atual["email"])
                if atual["id"]:
                    base.execute("UPDATE fornecedores SET nome = ?, contato = ?, telefone = ?, email = ? WHERE id = ?",
                                 (*dados, atual["id"]))
                else:
                    base.execute("INSERT INTO fornecedores (nome, contato, telefone, email) VALUES (?, ?, ?, ?)", dados)
            return redirect(url_for("fornecedores"))
        except sqlite3.IntegrityError:  # nome repetido: volta para a tela com o que foi digitado
            erro = f"Já existe um fornecedor chamado {atual['nome']}."
    else:
        linha = base.execute("SELECT id, nome, contato, telefone, email FROM fornecedores WHERE id = ?",
                             (request.args.get("editar"),)).fetchone()
        atual = dict(zip(("id", "nome", "contato", "telefone", "email"), linha or ("",) * 5))

    return render_template(
        "fornecedores.html", editando=atual, erro=erro,
        fornecedores=base.execute("""SELECT f.id, f.nome, f.contato, f.telefone, f.email, COUNT(pf.codprod)
                                     FROM fornecedores f LEFT JOIN produto_fornecedores pf ON pf.fornecedor_id = f.id
                                     GROUP BY f.id ORDER BY f.nome""").fetchall())


@app.route("/fornecedores/produtos", methods=["GET", "POST"])
def fornecedores_produtos():
    base, erro = abrir(), None
    if request.method == "POST":
        try:
            if "planilha" in request.files:
                lidos = forn.importar(base, request.files["planilha"].read())
                return redirect(url_for("fornecedores_produtos", importados=lidos))
            with base:
                if "remover" in request.form:  # tira um fornecedor de um produto
                    base.execute("DELETE FROM produto_fornecedores WHERE codprod = ? AND fornecedor_id = ?",
                                 (int(request.form["codprod"]), int(request.form["remover"])))
                else:  # acrescenta um fornecedor a todos os produtos da família
                    forn.ligar(base, [int(c) for c in request.form["codprods"].split(",")], request.form["fornecedor"])
            return redirect(request.full_path)
        except KeyError:
            abort(400)
        except ValueError as e:  # fornecedor não cadastrado, planilha errada: mostra na própria tela
            erro = str(e)

    # Mesmo filtro da tela de Famílias: um departamento por vez, a busca procura em todos
    produtos = fam.ativos(base)
    ligados = forn.por_produto(base)
    departamentos = sorted({d for _, _, d, _ in produtos})
    departamento = request.args.get("departamento", "")
    if departamento not in departamentos:
        departamento = departamentos[0] if departamentos else ""
    busca = request.args.get("busca", "").strip()
    sem_fornecedor = bool(request.args.get("sem_fornecedor"))
    grupos = {}
    for codprod, descricao, depto, familia in produtos:
        if sem_fornecedor and codprod in ligados:
            continue
        nomes = " ".join(n for _, n in ligados.get(codprod, []))
        if (sem_acento(busca) in sem_acento(f"{descricao} {familia} {nomes}")) if busca else depto == departamento:
            grupos.setdefault(familia, []).append((codprod, descricao, ligados.get(codprod, [])))
    return render_template(
        "fornecedores_produtos.html", grupos=grupos, departamentos=departamentos, departamento=departamento,
        busca=busca, sem_fornecedor=sem_fornecedor, erro=erro, importados=request.args.get("importados"),
        nomes=[n for (n,) in base.execute("SELECT nome FROM fornecedores ORDER BY nome")])


@app.route("/fornecedores-produtos.csv")
def fornecedores_planilha():
    return Response(forn.exportar(abrir()), mimetype="text/csv",
                    headers={"Content-Disposition": f"attachment; filename=fornecedores-{date.today()}.csv"})


@app.route("/acompanhamento")
def acompanhamento():
    base = abrir()
    semanas = acomp.semanas_fechadas(base)
    try:
        semana = date.fromisoformat(request.args.get("semana", ""))
    except ValueError:
        semana = None
    if semana not in semanas:
        semana = semanas[0] if semanas else None
    linhas = acomp.comparar(base, semana) if semana else []

    # Mesmo filtro da sugestão: um departamento por vez, a busca procura em todos
    departamentos = sorted({l["departamento"] for l in linhas})
    departamento = request.args.get("departamento", "")
    if departamento not in departamentos:
        departamento = departamentos[0] if departamentos else ""
    busca = request.args.get("busca", "").strip()
    familias = [{**l, "un": "kg" if l["unidade"] == "KG" else "un", "casas": 1 if l["unidade"] == "KG" else 0}
                for l in linhas
                if (sem_acento(busca) in sem_acento(l["nome"]) if busca else l["departamento"] == departamento)]

    return render_template(
        "acompanhamento.html", semana=semana, rotulo=semana and rotulo_semana(semana),
        tipo=semana and TIPOS_SEMANA[tipo_semana(semana)], semanas=[(s, rotulo_semana(s)) for s in semanas],
        resumo=acomp.resumo(linhas), deptos=acomp.por_departamento(linhas), familias=familias,
        departamentos=departamentos, departamento=departamento, busca=busca, margem=ACERTO_MARGEM * 100, unidades=ACERTO_UNIDADES)


def vendas_por_departamento(base, inicio, fim):
    """{departamento: valor vendido} entre as duas datas (inclusive)."""
    return dict(base.execute(
        """SELECT COALESCE(d.nome, 'SEM DEPARTAMENTO'), SUM(v.valor) FROM vendas_diarias v
           JOIN produtos p ON p.codprod = v.codprod LEFT JOIN departamentos d ON d.codepto = p.codepto
           WHERE v.data BETWEEN ? AND ? GROUP BY 1""", (inicio.isoformat(), fim.isoformat())))


@app.route("/analise")
def analise():
    base = abrir()
    # Datas escolhidas (padrão: as 4 semanas até o último dia com venda). Data inválida volta para o padrão.
    try:
        inicio = date.fromisoformat(request.args.get("inicio", ""))
        fim = date.fromisoformat(request.args.get("fim", ""))
    except ValueError:
        ultimo = base.execute("SELECT MAX(data) FROM vendas_diarias").fetchone()[0]
        fim = date.fromisoformat(ultimo) if ultimo else date.today()
        inicio = fim - timedelta(days=27)
    if fim < inicio:
        inicio, fim = fim, inicio

    # Período anterior com o mesmo número de dias, e o mesmo período 52 semanas antes
    # (52 semanas = mesmo dia da semana, o que é mais justo para comparar mercado)
    dias = (fim - inicio).days + 1
    anterior = (inicio - timedelta(days=dias), inicio - timedelta(days=1))
    ano_passado = (inicio - timedelta(weeks=52), fim - timedelta(weeks=52))

    atual = vendas_por_departamento(base, inicio, fim)
    ant = vendas_por_departamento(base, *anterior)
    passado = vendas_por_departamento(base, *ano_passado)
    total = {"atual": sum(atual.values()), "anterior": sum(ant.values()), "ano_passado": sum(passado.values())}
    linhas = [{"departamento": d, "atual": v, "anterior": ant.get(d, 0), "ano_passado": passado.get(d, 0),
               "var": variacao_pct(v, ant.get(d, 0)), "var_ano": variacao_pct(v, passado.get(d, 0)),
               "participacao": v / (total["atual"] or 1) * 100}
              for d, v in sorted(atual.items(), key=lambda x: -x[1])]

    # Semanas inteiras (segunda a domingo) que terminam dentro do período, para o gráfico de barras
    semanas, segunda = [], inicio - timedelta(days=inicio.weekday())
    while segunda + timedelta(days=6) <= fim:
        valor = base.execute("SELECT COALESCE(SUM(valor), 0) FROM vendas_diarias WHERE data BETWEEN ? AND ?",
                             (segunda.isoformat(), (segunda + timedelta(days=6)).isoformat())).fetchone()[0]
        semanas.append({"semana": f"{segunda:%d/%m} a {segunda + timedelta(days=6):%d/%m}",
                        "tipo": tipo_semana(segunda), "valor": valor})
        segunda += timedelta(weeks=1)

    return render_template(
        "analise.html", inicio=inicio, fim=fim, anterior=anterior, ano_passado=ano_passado,
        total=total, var_anterior=variacao_pct(total["atual"], total["anterior"]),
        var_ano=variacao_pct(total["atual"], total["ano_passado"]), linhas=linhas,
        semanas_mes=semanas, maior_semana=max((s["valor"] for s in semanas), default=0) or 1, tipos=TIPOS_SEMANA)


# ---------------------------------------------------------------------------
# Calendário de dias quentes (Fase 2)
# ---------------------------------------------------------------------------
# As regras (salário, recarga, feriados) ficam em calendario.py, que o motor também usa.
@app.route("/calendario")
def calendario():
    try:
        mes = int(request.args.get("mes", 10))
    except ValueError:
        mes = 10
    mes = min(max(mes, 1), 12)  # só 2026 por enquanto

    semanas = []
    for semana in calendar.Calendar(firstweekday=6).monthdatescalendar(2026, mes):  # começa no domingo
        semanas.append([{"data": d, "fora": d.month != mes, "tipos": tipos_do_dia(d),
                         "feriado": feriado(d)} for d in semana])

    return render_template("calendario.html", semanas=semanas, mes=mes, meses=MESES, tipos=TIPOS_SEMANA)


def criar_usuario(usuario):
    senha = getpass.getpass(f"Senha para {usuario}: ")
    if len(senha) < 6 or senha != getpass.getpass("Repita a senha: "):
        sys.exit("Senha diferente ou com menos de 6 caracteres. Nada foi gravado.")
    base = abrir()
    with base:
        base.execute("INSERT INTO usuarios (usuario, senha_hash) VALUES (?, ?) "
                     "ON CONFLICT(usuario) DO UPDATE SET senha_hash = excluded.senha_hash",
                     (usuario.strip().lower(), generate_password_hash(senha)))
    print(f"Usuário {usuario} gravado.")


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "usuario":
        criar_usuario(sys.argv[2])
    elif sys.argv[1:] == ["servir"]:
        from waitress import serve
        # Chave guardada num arquivo: reiniciar o computador não derruba o login de quem está usando
        arquivo = base_local.ARQUIVO_BASE.parent / "chave_sessao.txt"
        if not arquivo.exists():
            arquivo.parent.mkdir(exist_ok=True)
            arquivo.write_text(secrets.token_hex())
        app.secret_key = os.environ.get("SECRET_KEY") or arquivo.read_text()
        print("Sistema no ar: http://<IP deste computador>:8000  (Ctrl+C para parar)")
        serve(app, host="0.0.0.0", port=8000)
    else:
        app.run(debug=True)

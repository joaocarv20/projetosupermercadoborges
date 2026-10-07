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
import sys
import unicodedata
from datetime import date, timedelta
from functools import lru_cache

from flask import Flask, abort, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

import alertas as lista_alerta
import base_local
import motor
from base_local import abrir
from calendario import feriado, tipo_semana, tipos_do_dia

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
        with base:
            base.executemany("UPDATE sugestoes SET qtd_final = ? WHERE semana = ? AND familia_id = ?", finais)
        return redirect(request.full_path)

    salvas = dict(base.execute("SELECT familia_id, qtd_final FROM sugestoes WHERE semana = ? AND qtd_final IS NOT NULL",
                               (semana.isoformat(),)))
    # Um departamento por vez: a lista inteira passa de 5 mil famílias e trava o navegador.
    # A busca procura em todos os departamentos.
    departamentos = sorted({l["departamento"] or "SEM DEPARTAMENTO" for l in linhas})
    departamento = request.args.get("departamento", "")
    if departamento not in departamentos:
        departamento = departamentos[0] if departamentos else ""
    busca = request.args.get("busca", "").strip()

    familias = []
    for l in linhas:
        if not busca and (l["departamento"] or "SEM DEPARTAMENTO") != departamento:
            continue
        if busca and sem_acento(busca) not in sem_acento(" ".join([l["nome"], *(p["descricao"] for p in l["produtos"])])):
            continue
        kg = l["unidade"] == "KG"
        final = salvas.get(l["familia_id"], l["sugestao"])
        familias.append({
            **l, "un": "kg" if kg else "un", "casas": 1 if kg else 0,
            "qtd_final": int(final) if final == int(final) else final,  # 75 em vez de 75.0 no campo
            # Se um produto tem 80% ou mais da venda da família, provavelmente o caixa registra tudo nele
            "concentrado": len(l["produtos"]) > 1 and max(p["pct"] for p in l["produtos"]) >= 80,
        })

    dias = [semana + timedelta(days=i) for i in range(7)]
    obs = ", ".join(f"{feriado(d)} em {d:%d/%m}" for d in dias if feriado(d))
    return render_template(
        "sugestao.html", semana=semana, rotulo=rotulo_semana(semana), tipo=TIPOS_SEMANA[tipo_semana(semana)],
        obs=obs, semanas=[(s, rotulo_semana(s), TIPOS_SEMANA[tipo_semana(s)]["nome"]) for s in semanas],
        familias=familias, departamentos=departamentos, departamento=departamento, busca=busca)


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

"""
Protótipo visual – Compras Inteligentes – Supermercado Borges.

Para rodar:  python app.py   e abra  http://127.0.0.1:5000
Não há banco de dados nem login de verdade: tudo vem de dados_ficticios.py.
"""
import calendar
import math
import unicodedata
from datetime import date, timedelta

from flask import Flask, redirect, render_template, request, url_for

import dados_ficticios as dados
from calendario import feriado, tipos_do_dia

app = Flask(__name__)

MESES = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho",
         "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]


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
    return (atual - anterior) / anterior * 100


@app.context_processor
def contador_alertas():
    """Número de alertas mostrado no menu lateral, em todas as telas."""
    return {"total_alertas": len(dados.ALERTAS)}


# ---------------------------------------------------------------------------
# Telas
# ---------------------------------------------------------------------------
@app.route("/")
def inicio():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    # Login FALSO: qualquer usuário e senha entram.
    if request.method == "POST":
        return redirect(url_for("sugestao"))
    return render_template("login.html")


@app.route("/sugestao")
def sugestao():
    # Semana escolhida no seletor (padrão: a próxima semana de compra)
    semana_id = request.args.get("semana", dados.SEMANAS[0]["id"])
    semana = next((s for s in dados.SEMANAS if s["id"] == semana_id), dados.SEMANAS[0])
    tipo = dados.TIPOS_SEMANA[semana["tipo"]]

    departamento = request.args.get("departamento", "")
    busca = request.args.get("busca", "").strip()

    familias = []
    for f in dados.FAMILIAS:
        sabores = [nome for nome, _ in f.get("variacoes", [])]
        if departamento and f["departamento"] != departamento:
            continue
        if busca and sem_acento(busca) not in sem_acento(" ".join([f["nome"], *sabores])):
            continue

        # No sistema real, a mediana virá do Oracle. Aqui é só base x fator da semana.
        mediana = round(f["mediana_base"] * tipo["fator"])
        fardos = math.ceil(mediana / f["fardo"])  # arredonda para cima, em fardos inteiros

        # Sabores: divide a mediana conforme o peso registrado de cada um
        variacoes = []
        peso_total = sum(p for _, p in f.get("variacoes", []))
        for nome, peso in f.get("variacoes", []):
            variacoes.append({"nome": nome, "qtd": round(mediana * peso / peso_total),
                              "pct": peso / peso_total * 100})
        # Se um sabor tem 80% ou mais da venda, provavelmente o caixa registra tudo nele
        concentrado = bool(variacoes) and max(v["pct"] for v in variacoes) >= 80

        familias.append({
            **f,
            "mediana": mediana,
            "fardos": fardos,
            "sugestao": fardos * f["fardo"],
            "ano_passado": round(f["ano_passado_base"] * tipo["fator"]),
            "variacoes": variacoes,
            "concentrado": concentrado,
        })

    return render_template("sugestao.html", semana=semana, tipo=tipo, semanas=dados.SEMANAS,
                           tipos=dados.TIPOS_SEMANA, familias=familias,
                           departamentos=dados.DEPARTAMENTOS, departamento=departamento, busca=busca)


@app.route("/alertas")
def alertas():
    lista = sorted(dados.ALERTAS, key=lambda a: a["dias_sem_venda"], reverse=True)
    return render_template("alertas.html", alertas=lista)


@app.route("/analise")
def analise():
    # Datas escolhidas (padrão: setembro/2026). Data inválida volta para o padrão.
    try:
        inicio = date.fromisoformat(request.args.get("inicio", ""))
        fim = date.fromisoformat(request.args.get("fim", ""))
    except ValueError:
        inicio, fim = date(2026, 9, 1), date(2026, 9, 30)
    if fim < inicio:
        inicio, fim = fim, inicio

    # Período anterior com o mesmo número de dias, e o mesmo período 52 semanas antes
    # (52 semanas = mesmo dia da semana, o que é mais justo para comparar mercado)
    dias = (fim - inicio).days + 1
    anterior = (inicio - timedelta(days=dias), inicio - timedelta(days=1))
    ano_passado = (inicio - timedelta(weeks=52), fim - timedelta(weeks=52))

    deptos = dados.VENDAS_DEPARTAMENTO
    total = {k: sum(d[k] for d in deptos) for k in ("atual", "anterior", "ano_passado")}
    linhas = [{**d, "var": variacao_pct(d["atual"], d["anterior"]),
               "var_ano": variacao_pct(d["atual"], d["ano_passado"]),
               "participacao": d["atual"] / total["atual"] * 100} for d in deptos]

    return render_template(
        "analise.html", inicio=inicio, fim=fim, anterior=anterior, ano_passado=ano_passado,
        total=total, var_anterior=variacao_pct(total["atual"], total["anterior"]),
        var_ano=variacao_pct(total["atual"], total["ano_passado"]), linhas=linhas,
        semanas_mes=dados.VENDAS_SEMANAS_MES, maior_semana=max(s["valor"] for s in dados.VENDAS_SEMANAS_MES),
        tipos=dados.TIPOS_SEMANA)


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
    mes = min(max(mes, 1), 12)  # só 2026 neste protótipo

    semanas = []
    for semana in calendar.Calendar(firstweekday=6).monthdatescalendar(2026, mes):  # começa no domingo
        semanas.append([{"data": d, "fora": d.month != mes, "tipos": tipos_do_dia(d),
                         "feriado": feriado(d)} for d in semana])

    return render_template("calendario.html", semanas=semanas, mes=mes, meses=MESES, tipos=dados.TIPOS_SEMANA)


if __name__ == "__main__":
    app.run(debug=True)

"""
Calendário comercial: diz se cada dia é de salário, recarga do cartão alimentação, semana fraca ou feriado.
Usado pelo motor de sugestão (para achar semanas equivalentes) e pela tela de dias quentes.

Para gravar na base local (tabela calendario):  python calendario.py
"""
import calendar
from datetime import date, timedelta
from functools import lru_cache

import holidays

from base_local import abrir
from config import INICIO_HISTORICO

# Feriados municipais de Anápolis (mês, dia): nome
ANAPOLIS = {(7, 26): "Sant'Ana (Anápolis)", (7, 31): "Aniversário de Anápolis"}
# Pontos facultativos que a biblioteca separa dos feriados, mas que o mercado sente nas vendas
FACULTATIVOS_QUE_CONTAM = ("Carnaval", "Corpus Christi")

# Sábado NÃO conta como dia útil (é como o banco conta). Mude para True se o mercado conta o sábado
# no "5º dia útil" do pagamento do salário.
SABADO_E_DIA_UTIL = False


@lru_cache(maxsize=None)
def feriados(ano):
    """{data: nome} com os feriados nacionais, Carnaval, Corpus Christi e os de Anápolis."""
    achados = dict(holidays.Brazil(years=ano))
    for dia, nome in holidays.Brazil(years=ano, categories="optional").items():
        if nome in FACULTATIVOS_QUE_CONTAM:
            achados[dia] = nome
    for (mes, d), nome in ANAPOLIS.items():
        achados[date(ano, mes, d)] = nome
    return achados


def feriado(dia):
    """Nome do feriado, ou None."""
    return feriados(dia.year).get(dia)


@lru_cache(maxsize=None)
def dias_uteis(ano, mes):
    """Dias do mês de segunda a sexta que não são feriado."""
    ultimo = calendar.monthrange(ano, mes)[1]
    limite = 6 if SABADO_E_DIA_UTIL else 5  # weekday(): segunda = 0 ... sábado = 5
    return [d for d in range(1, ultimo + 1)
            if date(ano, mes, d).weekday() < limite and date(ano, mes, d) not in feriados(ano)]


def tipos_do_dia(dia):
    """Marcações do dia, da mais importante para a menos importante (um dia pode ter várias)."""
    uteis = dias_uteis(dia.year, dia.month)
    tipos = []
    if feriado(dia):
        tipos.append("feriado")
    # Salário: do último dia útil do mês até o 5º dia útil do mês seguinte
    if dia.day <= uteis[4] or dia.day >= uteis[-1]:
        tipos.append("salario")
    if dia.day in (1, 20):
        tipos.append("recarga")
    if dia.day >= 23 and "salario" not in tipos:
        tipos.append("fraca")
    return tipos


def tipo_principal(dia):
    """Um tipo só por dia, para a base: salário > recarga > fraca > meio. O feriado fica em coluna própria."""
    tipos = tipos_do_dia(dia)
    return next((t for t in ("salario", "recarga", "fraca") if t in tipos), "meio")


def tipo_semana(segunda):
    """Tipo da semana (segunda a domingo): feriado, salario, recarga, fraca ou meio.
    Com um dia de feriado a semana vai "à parte"; senão, 3 ou mais dias de salário ou de semana fraca
    decidem, e um dia 1 ou 20 marca a semana da recarga."""
    dias = [segunda + timedelta(days=i) for i in range(7)]
    if any(feriado(d) for d in dias):
        return "feriado"
    tipos = [tipos_do_dia(d) for d in dias]
    if sum("salario" in t for t in tipos) >= 3:
        return "salario"
    if any("recarga" in t for t in tipos):
        return "recarga"
    if sum("fraca" in t for t in tipos) >= 3:
        return "fraca"
    return "meio"


def preencher(base, inicio, fim):
    """Grava os dias de inicio a fim na tabela calendario. Pode rodar de novo: não mexe na marca 'atípico'."""
    dias = [inicio + timedelta(days=i) for i in range((fim - inicio).days + 1)]
    with base:
        base.executemany(
            "INSERT INTO calendario (data, tipo, feriado) VALUES (?, ?, ?) "
            "ON CONFLICT(data) DO UPDATE SET tipo = excluded.tipo, feriado = excluded.feriado",
            [(d.isoformat(), tipo_principal(d), feriado(d)) for d in dias])
    return len(dias)


if __name__ == "__main__":
    base = abrir()
    fim = date(date.today().year + 1, 12, 31)  # sempre até o fim do ano que vem
    print(f"{preencher(base, INICIO_HISTORICO, fim)} dias gravados ({INICIO_HISTORICO:%d/%m/%Y} a {fim:%d/%m/%Y}).")

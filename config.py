"""Configurações do sistema. Para mudar o que entra na sugestão, edite aqui."""
from datetime import date
from pathlib import Path

ARQUIVO_BASE = Path(__file__).parent / "dados" / "borges.db"

# O JP.MOVIMENTACAO começa em 12/12/2023: não há venda antes disso
INICIO_HISTORICO = date(2023, 12, 1)

# Quantas semanas equivalentes (mesmo tipo de semana) entram na mediana da sugestão
SEMANAS_EQUIVALENTES = 6

# Acompanhamento: a sugestão acertou quando a venda real ficou até 20% acima ou abaixo dela, ou a até
# 1 unidade (ou 1 kg) de diferença: produto de pouca saída oscila entre 0 e 3 por semana e os 20% não servem para ele
ACERTO_MARGEM = 0.2
ACERTO_UNIDADES = 1

# Lista de alerta: produto que vendeu em pelo menos 70% das semanas e está há 7 dias ou mais sem vender
ALERTA_FREQUENCIA = 0.7
ALERTA_DIAS_SEM_VENDA = 7

# Departamentos do Cefas que NÃO entram na sugestão: código -> nome (como está no Cefas)
DEPTOS_FORA = {
    # padaria
    "600": "CONFEITARIA", "601": "PADARIA PROPRIA", "602": "PADARIA FORNECEDOR",
    "997": "USO E CONSUMO PADARIA", "123": "MATERIA PRIMA",
    # açougue (os códigos de carnes sem vendas recentes ficam aqui por segurança)
    "200": "ACOUGUE", "500": "BOVINOS", "501": "AVES", "503": "LINGUICAS", "505": "SUINOS",
    "111": "AVES EM GERAL", "112": "BOVINOS", "125": "SUINOS", "126": "LINGUICAS",
    "124": "PEIXES", "506": "PEIXES",
    # hortifrúti
    "114": "HORTIFRUIT - FLV",
}

# Famílias (familias.py): palavras que, logo depois da 1ª, ainda descrevem o TIPO do produto e não a marca.
# Ex.: em "SAB LIQ PROTEX AVEIA 250ML" a marca é PROTEX, não LIQ. Viu uma família misturando marcas? Inclua aqui.
QUALIFICADORES = {
    "LIQ", "LIQUIDO", "BARRA", "DE", "DO", "DA", "EM", "P/", "C/",
    "DENTAL", "DENT", "HIG", "HID", "INT", "INTIMO", "INF", "INFANTIL", "UMED", "UMEDECIDA",
    "AERO", "AEROSOL", "ROLL", "ROLLON", "ROLL-ON", "CREME", "SPLASH", "CAPILAR", "PENTEAR", "BARBEAR", "CABELO",
    "MINERAL", "VINHO", "VODKA", "LACTEA", "PRONTA", "PRONTO", "RALADO", "PO", "MATINAL", "PAPEL",
    "INST", "MATE", "PERF", "ROL", "ISOTONICO", "LABIAL", "CORPORAL", "AROMAS", "ANIV",
    "LEITE", "CONDENSADO", "SOJA", "TRIGO", "MILHO", "TOMATE", "FRUTA", "FRUTAS",
}

"""Configurações do sistema. Para mudar o que entra na sugestão, edite aqui."""
from datetime import date
from pathlib import Path

ARQUIVO_BASE = Path(__file__).parent / "dados" / "borges.db"

# O JP.MOVIMENTACAO começa em 12/12/2023: não há venda antes disso
INICIO_HISTORICO = date(2023, 12, 1)

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

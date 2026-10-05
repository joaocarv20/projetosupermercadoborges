"""
DADOS FICTÍCIOS do protótipo "Compras Inteligentes – Supermercado Borges".

Tudo aqui é inventado e fixo. Quando o sistema for ligado ao banco Oracle,
é ESTE arquivo que será trocado por consultas reais. As telas (app.py e
templates/) continuam iguais, desde que os dados mantenham o mesmo formato.
"""
from datetime import date

# ---------------------------------------------------------------------------
# Tipos de semana
# "fator" = quanto a semana vende em relação a uma semana de "meio do mês".
# No sistema real isso não existe: a mediana virá direto das vendas históricas.
# ---------------------------------------------------------------------------
TIPOS_SEMANA = {
    "salario": {"nome": "Semana de salário", "cor": "vermelho", "fator": 1.40},
    "recarga": {"nome": "Recarga do cartão alimentação", "cor": "laranja", "fator": 1.25},
    "meio":    {"nome": "Meio do mês", "cor": "azul", "fator": 1.00},
    "fraca":   {"nome": "Semana fraca", "cor": "cinza", "fator": 0.70},
    "feriado": {"nome": "Semana com feriado", "cor": "roxo", "fator": 1.15},
}

# Semanas que aparecem no seletor da tela de sugestão (compra feita na segunda anterior)
SEMANAS = [
    {"id": "2026-10-05", "rotulo": "05/10 a 11/10/2026", "tipo": "salario"},
    {"id": "2026-10-12", "rotulo": "12/10 a 18/10/2026", "tipo": "feriado",
     "obs": "Feriado em 12/10 – Nossa Senhora Aparecida"},
    {"id": "2026-10-19", "rotulo": "19/10 a 25/10/2026", "tipo": "recarga"},
    {"id": "2026-10-26", "rotulo": "26/10 a 01/11/2026", "tipo": "fraca"},
]

DEPARTAMENTOS = ["Mercearia", "Limpeza", "Higiene", "Bebidas", "Frios"]

# ---------------------------------------------------------------------------
# Famílias de produto
#   mediana_base     = venda mediana (unidades) numa semana de "meio do mês"
#   ano_passado_base = venda da semana equivalente do ano passado (meio do mês)
#   fardo            = quantas unidades vêm em cada fardo/caixa/pacote
#   variacoes        = (sabor/fragrância, peso da venda registrada) – o peso
#                      vira unidades proporcionais à mediana da semana
# ---------------------------------------------------------------------------
FAMILIAS = [
    # --- Mercearia ---
    {"nome": "Arroz Tipo 1 Tio Jorge 5kg", "departamento": "Mercearia", "embalagem": "fardo", "fardo": 6,
     "mediana_base": 180, "ano_passado_base": 165},
    {"nome": "Feijão Carioca Kicaldo 1kg", "departamento": "Mercearia", "embalagem": "fardo", "fardo": 10,
     "mediana_base": 260, "ano_passado_base": 240},
    {"nome": "Óleo de Soja Soya 900ml", "departamento": "Mercearia", "embalagem": "caixa", "fardo": 20,
     "mediana_base": 300, "ano_passado_base": 310},
    {"nome": "Açúcar Cristal Itajá 5kg", "departamento": "Mercearia", "embalagem": "fardo", "fardo": 6,
     "mediana_base": 150, "ano_passado_base": 140},
    {"nome": "Café Pilão 500g", "departamento": "Mercearia", "embalagem": "caixa", "fardo": 10,
     "mediana_base": 140, "ano_passado_base": 120,
     "variacoes": [("Tradicional", 105), ("Extraforte", 35)]},
    {"nome": "Creme de Leite Piracanjuba 200g", "departamento": "Mercearia", "embalagem": "caixa", "fardo": 27,
     "mediana_base": 220, "ano_passado_base": 190},
    {"nome": "Leite Condensado Moça 395g", "departamento": "Mercearia", "embalagem": "caixa", "fardo": 27,
     "mediana_base": 130, "ano_passado_base": 120},
    {"nome": "Macarrão Instantâneo Nissin Miojo 80g", "departamento": "Mercearia", "embalagem": "fardo", "fardo": 50,
     "mediana_base": 420, "ano_passado_base": 380,
     "variacoes": [("Galinha Caipira", 150), ("Carne", 110), ("Galinha", 80), ("Legumes", 50), ("Tomate Picante", 30)]},
    {"nome": "Macarrão Espaguete Galo 500g", "departamento": "Mercearia", "embalagem": "fardo", "fardo": 20,
     "mediana_base": 200, "ano_passado_base": 185},
    {"nome": "Leite Integral Piracanjuba 1L", "departamento": "Mercearia", "embalagem": "caixa", "fardo": 12,
     "mediana_base": 600, "ano_passado_base": 560},
    {"nome": "Molho de Tomate Quero 300g (sachê)", "departamento": "Mercearia", "embalagem": "caixa", "fardo": 24,
     "mediana_base": 240, "ano_passado_base": 230,
     "variacoes": [("Tradicional", 150), ("Manjericão", 55), ("Pizza", 35)]},
    {"nome": "Sal Refinado Cisne 1kg", "departamento": "Mercearia", "embalagem": "fardo", "fardo": 10,
     "mediana_base": 70, "ano_passado_base": 75},

    # --- Limpeza ---
    # Exemplo do ERRO DO CAIXA: quase tudo registrado como "Limão"
    {"nome": "Detergente Ypê 500ml", "departamento": "Limpeza", "embalagem": "caixa", "fardo": 24,
     "mediana_base": 432, "ano_passado_base": 400,
     "variacoes": [("Limão", 410), ("Neutro", 9), ("Coco", 6), ("Maçã", 4), ("Clear", 2), ("Laranja", 1)]},
    {"nome": "Sabão em Pó Tixan Ypê 1,6kg", "departamento": "Limpeza", "embalagem": "fardo", "fardo": 10,
     "mediana_base": 110, "ano_passado_base": 105,
     "variacoes": [("Primavera", 55), ("Maciez", 35), ("Antibac", 20)]},
    {"nome": "Água Sanitária Qboa 2L", "departamento": "Limpeza", "embalagem": "caixa", "fardo": 6,
     "mediana_base": 160, "ano_passado_base": 150},
    {"nome": "Amaciante Ypê 2L", "departamento": "Limpeza", "embalagem": "caixa", "fardo": 6,
     "mediana_base": 95, "ano_passado_base": 90},
    {"nome": "Esponja Dupla Face Bettanin (4 un)", "departamento": "Limpeza", "embalagem": "fardo", "fardo": 30,
     "mediana_base": 70, "ano_passado_base": 65},

    # --- Higiene ---
    {"nome": "Papel Higiênico Neve Folha Dupla 12 rolos", "departamento": "Higiene", "embalagem": "fardo", "fardo": 4,
     "mediana_base": 120, "ano_passado_base": 115},
    {"nome": "Creme Dental Colgate 90g", "departamento": "Higiene", "embalagem": "caixa", "fardo": 12,
     "mediana_base": 180, "ano_passado_base": 170,
     "variacoes": [("Máxima Proteção Anticáries", 110), ("Tripla Ação", 50), ("Total 12", 20)]},
    {"nome": "Sabonete Lux 85g", "departamento": "Higiene", "embalagem": "caixa", "fardo": 12,
     "mediana_base": 260, "ano_passado_base": 250},
    {"nome": "Desodorante Rexona Aerosol 150ml", "departamento": "Higiene", "embalagem": "caixa", "fardo": 12,
     "mediana_base": 60, "ano_passado_base": 55},
    {"nome": "Absorvente Always (8 un)", "departamento": "Higiene", "embalagem": "caixa", "fardo": 12,
     "mediana_base": 50, "ano_passado_base": 48},

    # --- Bebidas ---
    {"nome": "Refrigerante Coca-Cola 2L", "departamento": "Bebidas", "embalagem": "fardo", "fardo": 6,
     "mediana_base": 480, "ano_passado_base": 450,
     "variacoes": [("Original", 400), ("Sem Açúcar", 80)]},
    {"nome": "Refrigerante Guaraná Antarctica 2L", "departamento": "Bebidas", "embalagem": "fardo", "fardo": 6,
     "mediana_base": 240, "ano_passado_base": 230},
    {"nome": "Cerveja Skol Lata 350ml", "departamento": "Bebidas", "embalagem": "fardo", "fardo": 12,
     "mediana_base": 960, "ano_passado_base": 900},
    {"nome": "Cerveja Brahma Lata 350ml", "departamento": "Bebidas", "embalagem": "fardo", "fardo": 12,
     "mediana_base": 600, "ano_passado_base": 610},
    {"nome": "Suco em Pó Tang 18g", "departamento": "Bebidas", "embalagem": "caixa", "fardo": 15,
     "mediana_base": 300, "ano_passado_base": 280,
     "variacoes": [("Laranja", 120), ("Uva", 80), ("Maracujá", 60), ("Morango", 40)]},

    # --- Frios ---
    {"nome": "Margarina Qualy 500g", "departamento": "Frios", "embalagem": "caixa", "fardo": 12,
     "mediana_base": 200, "ano_passado_base": 190,
     "variacoes": [("Com Sal", 160), ("Sem Sal", 40)]},
    {"nome": "Queijo Muçarela Fatiado 150g", "departamento": "Frios", "embalagem": "caixa", "fardo": 10,
     "mediana_base": 140, "ano_passado_base": 130},
    {"nome": "Presunto Fatiado Seara 200g", "departamento": "Frios", "embalagem": "caixa", "fardo": 10,
     "mediana_base": 120, "ano_passado_base": 115},
    {"nome": "Requeijão Cremoso Piracanjuba 200g", "departamento": "Frios", "embalagem": "caixa", "fardo": 12,
     "mediana_base": 130, "ano_passado_base": 120},
    {"nome": "Salsicha Perdigão 500g", "departamento": "Frios", "embalagem": "caixa", "fardo": 12,
     "mediana_base": 90, "ano_passado_base": 95},
]

# ---------------------------------------------------------------------------
# Lista de alerta: produtos que vendem quase toda semana, mas estão sem venda recente
# ---------------------------------------------------------------------------
FALTA = "Possível falta na prateleira"
ERRO_CAIXA = "Possível erro de registro no caixa"

ALERTAS = [
    {"produto": "Detergente Ypê 500ml Neutro", "departamento": "Limpeza",
     "dias_sem_venda": 34, "semanas_com_venda": 40, "semanas_total": 52, "motivo": ERRO_CAIXA},
    {"produto": "Sabonete Lux 85g Lavanda", "departamento": "Higiene",
     "dias_sem_venda": 30, "semanas_com_venda": 36, "semanas_total": 52, "motivo": ERRO_CAIXA},
    {"produto": "Macarrão Instantâneo Nissin Tomate Picante", "departamento": "Mercearia",
     "dias_sem_venda": 27, "semanas_com_venda": 41, "semanas_total": 52, "motivo": ERRO_CAIXA},
    {"produto": "Shampoo Seda Ceramidas 325ml", "departamento": "Higiene",
     "dias_sem_venda": 21, "semanas_com_venda": 38, "semanas_total": 52, "motivo": FALTA},
    {"produto": "Fermento em Pó Royal 100g", "departamento": "Mercearia",
     "dias_sem_venda": 18, "semanas_com_venda": 46, "semanas_total": 52, "motivo": FALTA},
    {"produto": "Água Tônica Antarctica Lata 350ml", "departamento": "Bebidas",
     "dias_sem_venda": 15, "semanas_com_venda": 44, "semanas_total": 52, "motivo": FALTA},
    {"produto": "Milho Verde Quero 170g", "departamento": "Mercearia",
     "dias_sem_venda": 12, "semanas_com_venda": 50, "semanas_total": 52, "motivo": FALTA},
    {"produto": "Mortadela Sadia Fatiada 200g", "departamento": "Frios",
     "dias_sem_venda": 9, "semanas_com_venda": 51, "semanas_total": 52, "motivo": FALTA},
]

# ---------------------------------------------------------------------------
# Análise de vendas (valores em R$) – fixos, não mudam com as datas escolhidas
# ---------------------------------------------------------------------------
VENDAS_DEPARTAMENTO = [
    {"departamento": "Mercearia", "atual": 412350.80, "anterior": 389120.40, "ano_passado": 371900.10},
    {"departamento": "Bebidas",   "atual": 198740.25, "anterior": 205310.90, "ano_passado": 176420.00},
    {"departamento": "Limpeza",   "atual": 121980.60, "anterior": 115230.15, "ano_passado": 112870.45},
    {"departamento": "Higiene",   "atual": 96410.30,  "anterior": 93880.70,  "ano_passado": 90150.20},
    {"departamento": "Frios",     "atual": 88215.45,  "anterior": 84960.00,  "ano_passado": 85430.80},
]

# Vendas por semana do mês (gráfico de barras)
VENDAS_SEMANAS_MES = [
    {"semana": "31/08 a 06/09", "tipo": "salario", "valor": 268400.00},
    {"semana": "07/09 a 13/09", "tipo": "meio",    "valor": 176900.00},
    {"semana": "14/09 a 20/09", "tipo": "recarga", "valor": 214300.00},
    {"semana": "21/09 a 27/09", "tipo": "fraca",   "valor": 139800.00},
    {"semana": "28/09 a 04/10", "tipo": "salario", "valor": 259700.00},
]

# ---------------------------------------------------------------------------
# Feriados 2026 (nacionais + Anápolis)
# ---------------------------------------------------------------------------
FERIADOS = {
    date(2026, 1, 1): "Confraternização Universal",
    date(2026, 2, 16): "Carnaval",
    date(2026, 2, 17): "Carnaval",
    date(2026, 4, 3): "Sexta-feira Santa",
    date(2026, 4, 21): "Tiradentes",
    date(2026, 5, 1): "Dia do Trabalho",
    date(2026, 6, 4): "Corpus Christi",
    date(2026, 7, 26): "Sant'Ana (Anápolis)",
    date(2026, 7, 31): "Aniversário de Anápolis",
    date(2026, 9, 7): "Independência do Brasil",
    date(2026, 10, 12): "Nossa Senhora Aparecida",
    date(2026, 11, 2): "Finados",
    date(2026, 11, 15): "Proclamação da República",
    date(2026, 11, 20): "Consciência Negra",
    date(2026, 12, 25): "Natal",
}

"""
Lista de alerta: produtos que costumam vender quase toda semana e pararam de vender.
Quando o produto acaba na prateleira ele some das vendas e, com isso, da sugestão: o comprador precisa conferir.

A lista é calculada na hora a partir das vendas do último ano. A tabela alertas guarda só o que o comprador
marcou (verificar, comprado, descontinuado), e a marca perde o efeito quando o produto volta a vender.

Como rodar:  python alertas.py
"""
from datetime import date, timedelta

from base_local import abrir
from config import ALERTA_DIAS_SEM_VENDA, ALERTA_FREQUENCIA

STATUS = ("verificar", "comprado", "descontinuado")


def listar(base):
    """Produtos em alerta, do mais tempo sem venda para o menor. "Hoje" é o último dia com venda na base,
    para um atraso do extrator não jogar todos os produtos na lista."""
    fim = base.execute("SELECT MAX(data) FROM vendas_diarias").fetchone()[0]
    if not fim:
        return []
    fim = date.fromisoformat(fim)
    inicio = fim - timedelta(weeks=52) + timedelta(days=1)
    linhas = base.execute(
        """SELECT p.codprod, p.descricao, d.nome, MIN(v.data), MAX(v.data),
                  COUNT(DISTINCT CAST((julianday(v.data) - julianday(:inicio)) / 7 AS INTEGER)),
                  a.status, a.atualizado_em
           FROM vendas_diarias v JOIN produtos p ON p.codprod = v.codprod
           LEFT JOIN departamentos d ON d.codepto = p.codepto
           LEFT JOIN alertas a ON a.codprod = p.codprod
           WHERE v.data >= :inicio AND v.qtd > 0 AND p.dtexclusao IS NULL
           GROUP BY p.codprod""", {"inicio": inicio.isoformat()})

    resultado = []
    for codprod, produto, depto, primeira, ultima, com_venda, status, marcado_em in linhas:
        primeira, ultima = date.fromisoformat(primeira), date.fromisoformat(ultima)
        dias = (fim - ultima).days
        total = (fim - primeira).days // 7 + 1  # semanas desde a 1ª venda no último ano (produto novo tem menos)
        if dias < ALERTA_DIAS_SEM_VENDA or com_venda < 4 or com_venda < ALERTA_FREQUENCIA * total:
            continue
        if marcado_em and marcado_em < ultima.isoformat():
            status = None  # vendeu depois de marcado: a marca era de outra parada
        if status == "descontinuado":
            continue
        if status == "comprado" and (fim - date.fromisoformat(marcado_em)).days < ALERTA_DIAS_SEM_VENDA:
            continue  # dá uma semana para a mercadoria chegar; se continuar sem vender, volta para a lista
        resultado.append({"codprod": codprod, "produto": produto, "departamento": depto, "ultima_venda": ultima,
                          "dias_sem_venda": dias, "semanas_com_venda": com_venda, "semanas_total": total,
                          "status": status})
    return sorted(resultado, key=lambda a: -a["dias_sem_venda"])


def marcar(base, codprod, status, dia=None):
    """Grava o que o comprador fez com o produto do alerta."""
    if status not in STATUS:
        raise ValueError(f"status inválido: {status}")
    with base:
        base.execute("INSERT INTO alertas (codprod, status, atualizado_em) VALUES (?, ?, ?) "
                     "ON CONFLICT(codprod) DO UPDATE SET status = excluded.status, atualizado_em = excluded.atualizado_em",
                     (codprod, status, (dia or date.today()).isoformat()))


if __name__ == "__main__":
    lista = listar(abrir())
    for a in lista:
        print(f"{a['codprod']:>8}  {a['produto'][:45]:45}  {a['departamento'] or '':25}  "
              f"há {a['dias_sem_venda']:>3} dias  ({a['semanas_com_venda']} de {a['semanas_total']} semanas)"
              f"{'  [' + a['status'] + ']' if a['status'] else ''}")
    print(f"\n{len(lista)} produtos em alerta.")

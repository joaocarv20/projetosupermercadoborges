"""Teste das telas com uma base inventada (login, sugestão, alerta e análise).  Rode:  python test_app.py"""
import io
import tempfile
from datetime import date, timedelta
from pathlib import Path

from werkzeug.security import generate_password_hash

import base_local
import motor

base_local.ARQUIVO_BASE = Path(tempfile.mkdtemp()) / "teste.db"
from app import app  # noqa: E402  (depois de trocar a base)

base = base_local.abrir()
base.execute("INSERT INTO departamentos VALUES ('102', 'MERCEARIA BASICA', 1)")
base.executemany("INSERT INTO familias (id, nome) VALUES (?, ?)", [(1, "ARROZ"), (2, "FEIJAO")])
base.executemany("INSERT INTO produtos (codprod, descricao, unidade, codepto, familia_id) VALUES (?, ?, 'UN', '102', ?)",
                 [(1, "ARROZ 5KG", 1), (2, "FEIJAO 1KG", 2)])
ontem = date.today() - timedelta(days=1)
base.executemany("INSERT INTO vendas_diarias VALUES (?, ?, 10, 50)",
                 [((ontem - timedelta(days=d)).isoformat(), c) for d in range(400) for c in (1, 2) if c == 1 or d >= 10])
base.execute("INSERT INTO usuarios VALUES ('paulo', ?)", (generate_password_hash("segredo1"),))
base.commit()

cliente = app.test_client()
assert cliente.get("/sugestao").location.endswith("/login")                      # sem login: vai para o login
assert "incorretos" in cliente.post("/login", data={"usuario": "paulo", "senha": "errada"}).text
assert cliente.post("/login", data={"usuario": "Paulo", "senha": "segredo1"}).status_code == 302

semana = motor.proxima_segunda(date.today()).isoformat()
pagina = cliente.get(f"/sugestao?semana={semana}").text
assert "ARROZ" in pagina and 'value="70" aria-label="Quantidade final de ARROZ"' in pagina                # 10 por dia x 7

cliente.post(f"/sugestao?semana={semana}", data={"qtd_1": "75", "qtd_2": "abc", "qtd_99": "5"})
assert base.execute("SELECT familia_id, qtd_sugerida, qtd_final FROM sugestoes ORDER BY 1").fetchall() == [
    (1, 70, 75), (2, 70, None)]                                                   # texto inválido e família estranha são ignorados
assert 'value="75" aria-label="Quantidade final de ARROZ"' in cliente.get(f"/sugestao?semana={semana}").text
assert "FEIJAO" not in cliente.get(f"/sugestao?semana={semana}&busca=arroz").text

assert "FEIJAO 1KG" in cliente.get("/alertas").text                               # parou há 10 dias
assert cliente.post("/alertas", data={"codprod": "2", "status": "qualquer"}).status_code == 400
cliente.post("/alertas", data={"codprod": "2", "status": "descontinuado"})
assert "FEIJAO 1KG" not in cliente.get("/alertas").text

assert cliente.get("/analise").status_code == 200
assert cliente.get("/analise?inicio=2020-01-01&fim=2020-01-31").status_code == 200  # período sem vendas
assert cliente.get("/calendario").status_code == 200

assert "Ainda não há semana" in cliente.get("/acompanhamento").text                # a semana salva acima não terminou
fechada = (motor.proxima_segunda(date.today()) - timedelta(weeks=3)).isoformat()
base.execute("INSERT INTO sugestoes VALUES (?, 1, 70, 80)", (fechada,))
base.commit()
pagina = cliente.get("/acompanhamento?semana=lixo").text                          # semana inválida: a mais recente
assert "ARROZ" in pagina and "0 × 1" in pagina                  # vendeu 70: sistema mais perto
# Famílias: mover um produto, baixar e enviar a planilha
assert "ARROZ 5KG" in cliente.get("/familias").text
cliente.post("/familias", data={"codprod": "2", "familia": "graos"})
assert base.execute("SELECT f.nome FROM produtos p JOIN familias f ON f.id = p.familia_id WHERE codprod = 2").fetchone() == ("GRAOS",)
assert "FEIJAO 1KG;MERCEARIA BASICA;GRAOS" in cliente.get("/familias.csv").get_data(as_text=True)
envio = {"planilha": (io.BytesIO("codigo;familia\n2;GRAOS E CIA\n".encode()), "f.csv")}
assert cliente.post("/familias", data=envio, content_type="multipart/form-data").location.endswith("importados=1")
envio = {"planilha": (io.BytesIO(b"x;y\n"), "f.csv")}
assert "colunas" in cliente.post("/familias", data=envio, content_type="multipart/form-data").text

# Sugestão por sabor: o feijão entra na família do arroz e a compra é repartida pela venda de cada um
cliente.post("/familias", data={"codprod": "2", "familia": "ARROZ"})
pagina = cliente.get(f"/sugestao?semana={semana}").text
assert "2 sabores" in pagina and "<strong>38 un</strong>" in pagina and "<strong>37 un</strong>" in pagina  # 75 salvos
cliente.get("/sair")
assert cliente.get("/alertas").status_code == 302
print("OK")

"""Teste das telas com uma base inventada (login, sugestão, alerta e análise).  Rode:  python -m testes.test_app"""
import io
import tempfile
from datetime import date, timedelta
from pathlib import Path

from werkzeug.security import generate_password_hash

from sistema import base_local
from sistema import motor

base_local.ARQUIVO_BASE = Path(tempfile.mkdtemp()) / "teste.db"
from app import app  # noqa: E402  (depois de trocar a base)
from sistema.fornecedores import link_pedido  # noqa: E402

forn_link = lambda telefone: link_pedido(telefone, "", []).split("Pedido")[0]

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
# Fornecedores: cadastrar, nome repetido, editar
cliente.post("/fornecedores", data={"nome": " camil ", "telefone": "11 9999"})
assert base.execute("SELECT id, nome FROM fornecedores").fetchall() == [(1, "CAMIL")]
assert "Já existe" in cliente.post("/fornecedores", data={"nome": "Camil"}).text
assert 'value="11 9999"' in cliente.get("/fornecedores?editar=1").text
cliente.post("/fornecedores", data={"id": "1", "nome": "CAMIL ALIMENTOS"})
cliente.post("/fornecedores", data={"nome": "ATACADO SUL"})
pagina = cliente.get("/fornecedores?busca=camíl").text                                         # busca sem acento
assert "CAMIL ALIMENTOS" in pagina and "ATACADO SUL" not in pagina

# Fornecedor por produto: adicionar à família, fornecedor não cadastrado, tirar de um produto, planilha
ligados = lambda: base.execute("SELECT codprod, f.nome FROM produto_fornecedores JOIN fornecedores f ON f.id = fornecedor_id "
                               "ORDER BY 1, 2").fetchall()
cliente.post("/fornecedores/produtos", data={"codprods": "1,2", "fornecedor": "camil alimentos"})
cliente.post("/fornecedores/produtos", data={"codprods": "2", "fornecedor": "ATACADO SUL"})
assert ligados() == [(1, "CAMIL ALIMENTOS"), (2, "ATACADO SUL"), (2, "CAMIL ALIMENTOS")]
assert "não está cadastrado" in cliente.post("/fornecedores/produtos", data={"codprods": "1", "fornecedor": "XYZ"}).text
cliente.post("/fornecedores/produtos", data={"codprod": "2", "remover": "1"})
assert ligados() == [(1, "CAMIL ALIMENTOS"), (2, "ATACADO SUL")]
assert "ATACADO SUL" in cliente.get("/fornecedores/produtos?busca=atacado").text            # busca pelo fornecedor
planilha = cliente.get("/fornecedores-produtos.csv").get_data(as_text=True)
assert "1;ARROZ 5KG;MERCEARIA BASICA;ARROZ;CAMIL ALIMENTOS" in planilha
envio = {"planilha": (io.BytesIO("codigo;fornecedor\n1;\n2;atacado sul\n2;camil alimentos\n".encode()), "f.csv")}
assert cliente.post("/fornecedores/produtos", data=envio, content_type="multipart/form-data").location.endswith("importados=2")
assert ligados() == [(2, "ATACADO SUL"), (2, "CAMIL ALIMENTOS")]                              # o 1 ficou sem fornecedor
envio = {"planilha": (io.BytesIO("codigo;fornecedor\n1;NOVO\n".encode()), "f.csv")}
assert "NOVO" in cliente.post("/fornecedores/produtos", data=envio, content_type="multipart/form-data").text
assert ligados() == [(2, "ATACADO SUL"), (2, "CAMIL ALIMENTOS")]                              # nada gravado
assert "ARROZ 5KG" in cliente.get("/fornecedores/produtos?sem_fornecedor=1").text

cliente.post("/fornecedores", data={"excluir": "1"})                                          # sai dos produtos também
assert ligados() == [(2, "ATACADO SUL")]

# Sugestão: escolher o fornecedor do sabor que tem dois, filtrar por fornecedor
cliente.post("/fornecedores", data={"nome": "CAMIL"})                                         # id 3
cliente.post("/fornecedores/produtos", data={"codprods": "1,2", "fornecedor": "CAMIL"})
cliente.post("/fornecedores/produtos", data={"codprods": "1", "fornecedor": "ATACADO SUL"})
# produto 1: ATACADO SUL e CAMIL (vem marcado o 1º em ordem alfabética); produto 2: ATACADO SUL e CAMIL também
pagina = cliente.get(f"/sugestao?semana={semana}").text
assert 'name="forn_1"' in pagina and '<option value="2" selected>ATACADO SUL</option>' in pagina
cliente.post(f"/sugestao?semana={semana}", data={"qtd_1": "75", "forn_1": "3", "forn_2": "99"})       # 99 não é fornecedor do 2
assert base.execute("SELECT codprod, fornecedor_id FROM escolha_fornecedor").fetchall() == [(1, 3)]
assert '<option value="3" selected>CAMIL</option>' in cliente.get(f"/sugestao?semana={semana}").text
seguinte = (date.fromisoformat(semana) + timedelta(weeks=1)).isoformat()
assert '<option value="3" selected>CAMIL</option>' in cliente.get(f"/sugestao?semana={seguinte}").text  # a última escolha vale
assert "ARROZ" in cliente.get(f"/sugestao?semana={semana}&fornecedor=3").text
cliente.post("/fornecedores", data={"nome": "SEM PRODUTO"})
assert "Nenhum produto" in cliente.get(f"/sugestao?semana={semana}&fornecedor=4").text

# Pedido pelo WhatsApp: salva e abre o wa.me com só os sabores em que o fornecedor é o escolhido
cliente.post("/fornecedores", data={"id": "3", "nome": "CAMIL", "telefone": "(11) 98765-4321"})
assert "mandar pedido para CAMIL" in cliente.get(f"/sugestao?semana={semana}&fornecedor=3").text
resposta = cliente.post(f"/sugestao?semana={semana}&fornecedor=3", data={"qtd_1": "75", "forn_1": "3", "enviar": "3"})
link = resposta.location
assert link.startswith("https://wa.me/5511987654321?text=Pedido") and "ARROZ%205KG" in link and "FEIJAO" not in link, link
assert "Total%3A%201%20itens" in link
assert "/sugestao" in cliente.post(f"/sugestao?semana={semana}&fornecedor=4", data={"enviar": "4"}).location  # nada a pedir
assert forn_link("0xx11 3333-4444") == "https://wa.me/551133334444?text="                       # fixo com 0 na frente
assert forn_link("") == "https://wa.me/?text="                                                  # sem telefone

cliente.get("/sair")
assert cliente.get("/alertas").status_code == 302
print("OK")

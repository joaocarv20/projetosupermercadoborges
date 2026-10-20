# Sistema de Sugestão de Compras – Supermercado Borges

Documentação do projeto. **Toda mudança no sistema entra aqui**, no [Histórico de mudanças](#histórico-de-mudanças)
e na seção que ela afeta. O passo a passo do computador do mercado está em [INSTALACAO.md](../INSTALACAO.md).

## Resumo

O sistema lê as vendas do Cefas toda noite, sugere a compra da semana por família de produto, avisa produtos que
pararam de vender, mede o próprio acerto e monta o pedido de cada fornecedor pelo WhatsApp. Está instalado no
computador do mercado desde 15/10/2026; agora começa o teste de 2 a 3 semanas com o Paulo.

| Passo da ordem de construção | Situação em 20/10/2026 |
| --- | --- |
| 1. Calendário e motor de cálculo | Pronto |
| 2. Conexão com o Oracle e descoberta das tabelas | Pronto (schema JP, tabela JP.MOVIMENTACAO) |
| 3. Extrator e validação dos totais | Pronto: R$ 244.121,68 em 03 a 09/08/2026, conferido com o Cefas |
| 4. Telas ligadas aos dados reais | Pronto, com login |
| 5. Instalação, agendamento e backup | Pronto: instalado em 15/10, tarefas agendadas em 19/10 |
| 6. 2 a 3 semanas comparando sugestão e compras | Começando (tela de Acompanhamento pronta) |
| Extra: fornecedores e pedido por WhatsApp | Pronto: fornecedores importados do Cefas em 19/10 |

## Arquitetura e arquivos

O Oracle do Cefas é lido uma vez por noite, **só para leitura** (usuário `iacompras`), e todo o resto roda sobre uma
cópia em SQLite (`dados/borges.db`). Nada é gravado de volta no Cefas. As telas gravam na base local só o que o
comprador faz: quantidades finais, fornecedor escolhido, marcas da lista de alerta e ajustes de família e de
fornecedor. Sem banco para instalar e sem Docker.

| Arquivo | O que faz |
| --- | --- |
| `extrator.py` | Copia departamentos, produtos, vendas diárias (JP.MOVIMENTACAO, operação S, sem cancelados) e quem entrega cada produto (JP.DADOSTEMPENT + JP.FORNECEDOR). 1ª carga mês a mês desde 12/2023; depois refaz só os últimos 3 dias |
| `rotina_noturna.py` + `.bat` | Extrator + backup da base, toda madrugada às 3h |
| `iniciar_servidor.bat` | Liga o servidor quando o computador liga |
| `atualizar.bat` | Baixa a versão nova do GitHub (`git pull`) e reinicia o servidor |
| `app.py` + `templates/` + `static/` | Telas (Flask), login e servidor de produção (waitress, porta 8000) |
| `config.py` | Parâmetros: departamentos fora, semanas equivalentes, alerta, acerto, qualificadores das famílias |
| `sistema/base_local.py` | Cria a base SQLite (tabelas abaixo) |
| `sistema/oracle.py` | Conexão com o Oracle; recusa tudo que não for SELECT; tempo máximo por consulta |
| `sistema/calendario.py` | Classifica cada dia e semana: salário, recarga, meio do mês, fraca, feriado |
| `sistema/motor.py` | Calcula a sugestão por família e reparte entre os sabores |
| `sistema/familias.py` | Agrupa os produtos em famílias (tipo + marca + tamanho); exporta e importa a planilha |
| `sistema/fornecedores.py` | Fornecedores de cada produto, escolha na sugestão, link do WhatsApp, importação do Cefas, planilha |
| `sistema/alertas.py` | Lista os produtos que costumam vender e pararam |
| `sistema/acompanhamento.py` | Compara sugerido, comprado e vendido numa semana fechada |
| `ferramentas/` | Descoberta e conferência do Oracle: `explorar_banco`, `conferir_vendas`, `listar_departamentos` |
| `testes/` | Um teste por peça: `python -m testes.test_app` e os demais |
| `docs/` | Esta documentação e os mapas do banco do Cefas (`mapa_banco.md`, `mapa_tabelas.md`) |

### Tabelas da base local

| Tabela | Conteúdo | Origem |
| --- | --- | --- |
| `departamentos` | Código, nome, se entra na sugestão | Cefas + `config.py` |
| `produtos` | Código, descrição, unidade, departamento, seção, código de barras, família | Cefas |
| `familias` | Nome da família (ex.: SAB PALMOLIVE 85G) | Regra automática + ajuste manual |
| `vendas_diarias` | Data, produto, quantidade, valor (1 linha por produto por dia) | Cefas, resumido |
| `calendario` | Tipo do dia, feriado, marca de dia atípico | Gerado pelo sistema |
| `sugestoes` | Semana, família, quantidade sugerida, quantidade final do comprador | Gerado + tela |
| `alertas` | Produto, situação marcada (verificar, comprado, descontinuado) | Tela |
| `fornecedores` | Nome, contato, telefone, e-mail | Cefas + tela |
| `produto_fornecedores` | Quem fornece cada produto (pode ser mais de um) | Cefas + tela + planilha |
| `escolha_fornecedor` | De quem o comprador pediu cada produto em cada semana | Tela |
| `cefas_fornecedores` | Pares produto-fornecedor já vistos no Cefas e o nº da última entrada | Cefas |
| `usuarios` | Usuário e senha criptografada | `python app.py usuario <nome>` |

### Tabelas do Cefas que o sistema lê

`JP.PRODUTO`, `JP.DEPTO`, `JP.MOVIMENTACAO`, `JP.FORNECEDOR` e `JP.DADOSTEMPENT`. Cada tabela nova precisa de
`GRANT SELECT ... TO IACOMPRAS`, dado pelo SQL Navigator conectado como JP (ver [INSTALACAO.md](../INSTALACAO.md),
passo 8). Sem a permissão, o Oracle responde `ORA-00942: a tabela ou view não existe`.

## Telas

O Paulo usa o sistema pelo navegador, em qualquer computador da rede (`http://192.168.0.108:8000`), depois de entrar
com usuário e senha. A tela principal é a Sugestão de compra, aberta toda segunda.

| Tela | Para quê | O que o comprador faz nela |
| --- | --- | --- |
| Sugestão de compra | Quanto comprar de cada família para a semana seguinte, e de quem | Escolhe a semana; filtra por departamento, busca ou fornecedor; abre a família para ver quanto comprar de cada sabor; corrige a quantidade final; escolhe o fornecedor de cada produto; salva, imprime ou **manda o pedido do fornecedor pelo WhatsApp** |
| Lista de alerta | Produtos que costumam vender e pararam (provável falta na prateleira) | Marca cada um como "Verificando", "Já comprei" ou "Descontinuado" |
| Famílias de produto | Conferir e corrigir como os sabores foram agrupados | Move um produto para outra família ou para uma nova; baixa a planilha, corrige no Excel e envia de volta |
| Fornecedores > Cadastro | Fornecedores, contato e telefone do WhatsApp | Cadastra, edita, exclui; busca por nome, contato ou telefone (sem busca, mostra os 50 que fornecem mais produtos) |
| Fornecedores > Produtos | Quem fornece cada produto | Acrescenta um fornecedor à família inteira; tira de um produto com o ×; filtra "só sem fornecedor"; ajusta pela planilha |
| Acompanhamento | Medir se a sugestão acerta | Escolhe uma semana já fechada; vê o acerto geral, por departamento e família por família |
| Análise de vendas | Vendas por departamento num período | Escolhe as datas; compara com o período anterior e com o ano passado; gráfico por semana |
| Calendário de dias quentes | Ver os dias de salário, recarga, semana fraca e feriado | Navega pelos meses (por enquanto só 2026) |

Na impressão da sugestão saem só o cabeçalho, a tabela com os sabores de cada família e um campo para assinatura.
As telas grandes mostram **um departamento por vez**; a busca procura em todos.

## Regras de negócio

Os números ficam em `config.py` ou `sistema/calendario.py` e podem ser ajustados.

### Calendário comercial

| Tipo de dia | Regra |
| --- | --- |
| Salário | Do último dia útil do mês até o 5º dia útil do mês seguinte (sábado não conta) |
| Recarga do cartão alimentação | Dias 1 e 20 |
| Semana fraca | Do dia 23 em diante, fora do salário |
| Feriado | Nacionais, Carnaval, Corpus Christi, Sant'Ana (26/07) e aniversário de Anápolis (31/07) |

A semana (segunda a domingo) recebe um tipo só: com feriado, é "feriado"; com 3 dias ou mais de salário, "salário";
com dia 1 ou 20, "recarga"; com 3 dias ou mais fracos, "fraca"; senão, "meio do mês".

### Cálculo da sugestão

1. Acha as 6 últimas semanas completas do mesmo tipo da semana-alvo, pulando as que têm dia marcado como atípico.
2. Soma o que cada família vendeu em cada uma delas.
3. Sugere a mediana dessas 6 somas. Semanas antes da 1ª venda de um produto novo não contam.
4. Arredonda: unidades para cima, quilos com 1 casa.
5. Mostra ao lado a mediana sem arredondar e a venda da mesma semana do ano passado.

O cálculo é guardado até a base mudar (extrator, quantidade salva, alerta marcado): só a 1ª tela depois de uma
mudança espera alguns segundos.

### Famílias e sabores

- Regra: tipo + marca + tamanho, lidos da descrição. SAB PALMOLIVE SUAVE HID INTENSIVA 85G vira SAB PALMOLIVE 85G.
- Palavras que não são marca (LIQ, DENTAL, AERO, DE, LEITE…) ficam em `QUALIFICADORES`: SAB LIQ PROTEX 250ML não se
  mistura com SAB LIQ NIVEA 250ML.
- Tamanhos iguais se juntam: 1LT = 1L, 85GR = 85G, 500 G = 500G.
- Ajuste manual vale mais que a regra: o extrator só dá família a produto novo; `python -m sistema.familias agrupar`
  refaz tudo e **desfaz os ajustes**.
- Por sabor: a quantidade final da família é repartida pela venda de cada sabor nas mesmas 6 semanas, e a soma fecha o
  total exato. Sabor que não vendeu fica com zero.

### Fornecedores e pedido

- Um produto pode ter **mais de um fornecedor**; fornecedor não é por departamento (decisão do Paulo, 14/10).
- **Importação do Cefas, toda noite:** `JP.DADOSTEMPENT` tem uma linha por entrada de mercadoria; o par
  (produto, fornecedor que entregou) vira uma ligação, com nome, contato e telefone de `JP.FORNECEDOR`.
  - Cada par só é ligado na 1ª vez que aparece (`cefas_fornecedores`): o que o Paulo tira na tela não volta.
  - Fornecedor com o mesmo nome de um já cadastrado é o mesmo; contato e telefone digitados à mão não são trocados.
  - Vem o histórico inteiro de entregas: pode aparecer fornecedor que não entrega mais. Tira-se pela tela.
  - Se faltar permissão no Oracle, a rotina avisa no log e as vendas são importadas do mesmo jeito.
- **Escolha na sugestão:** vale a escolha da semana; sem ela, a última que o comprador fez para o produto; sem essa, o
  **último fornecedor que entregou** no Cefas; sem esse, o 1º em ordem alfabética.
- **Pedido pelo WhatsApp:** com a sugestão filtrada por fornecedor, "Salvar e mandar pedido" salva e abre o WhatsApp
  (`wa.me`) com a lista de produtos e quantidades já escrita, para o telefone do cadastro.
- `CODFORNECPRINC` (fornecedor principal em JP.PRODUTO) não é usado: nunca foi conferido se está preenchido.

### Lista de alerta

Entra o produto que vendeu em pelo menos 70% das semanas do último ano (no mínimo 4 semanas) e está há 7 dias ou mais
sem vender. "Já comprei" tira da lista por 7 dias; "Descontinuado" tira até o produto voltar a vender.

### Acompanhamento

A sugestão acertou quando a venda real ficou até 20% acima ou abaixo dela, ou a até 1 unidade de diferença (margem
mantida pelo Paulo em 14/10). Numa semana simulada com os dados reais (28/09 a 04/10/2026), o acerto foi de 52%, e o
sistema sugeriu 19.263 unidades para 18.790 vendidas: 2,5% acima, sem tendência a errar para um lado. O erro se
concentra nos produtos de 1 a 5 unidades por semana.

## Instalação e operação

O sistema roda no computador Windows do mercado (`192.168.0.108`), ligado pelo Agendador de Tarefas. A manutenção é
feita pelo AnyDesk. Passo a passo completo, problemas comuns e como atualizar: [INSTALACAO.md](../INSTALACAO.md).

| Quando | O que acontece |
| --- | --- |
| Ao ligar o computador | Sobe o servidor das telas (tarefa "Borges - servidor" → `iniciar_servidor.bat`) |
| Todo dia às 3h | Vendas de ontem, produtos, fornecedores e backup (tarefa "Borges - rotina noturna" → `rotina_noturna.bat`) |
| Segunda de manhã | O Paulo abre a sugestão; o cálculo é feito na hora |
| Uma vez por semana (manual) | Copiar o backup mais novo para fora da máquina |
| Depois de cada mudança | No mercado, dois cliques no `atualizar.bat` |

O backup guarda as 14 últimas cópias em `backups\`. Os registros ficam em `logs\rotina.log` e `logs\servidor.log`.

**Como uma mudança chega ao mercado:** é feita e testada no notebook, enviada ao GitHub (`main`) e baixada lá pelo
`atualizar.bat`. Nunca se edita o código direto no computador do mercado, e a base de lá (`dados\borges.db`) é a de
verdade: não vai para o GitHub.

### Comandos úteis

Todos rodam da pasta principal do projeto (no mercado: `.venv\Scripts\python` no lugar de `python`).

| Comando | Para quê |
| --- | --- |
| `python app.py servir` | Liga o sistema na rede (porta 8000) |
| `python app.py usuario <nome>` | Cria um usuário ou troca a senha |
| `python extrator.py [AAAA-MM-DD]` | Carrega vendas e fornecedores (vendas a partir da data, se informada) |
| `python -m sistema.familias agrupar` | Refaz todas as famílias pela regra (desfaz ajustes manuais) |
| `python -m sistema.familias exportar arquivo.csv` / `importar arquivo.csv` | Famílias pela planilha |
| `python -m sistema.motor AAAA-MM-DD` | Sugestão de uma semana no terminal |
| `python -m sistema.acompanhamento AAAA-MM-DD` | Acerto de uma semana no terminal |
| `python -m ferramentas.conferir_vendas AAAA-MM-DD AAAA-MM-DD` | Total de um período, para conferir com o Cefas |
| `python -m testes.test_app` (e os demais `testes/test_*.py`) | Testes automáticos |

## Decisões

- **Subcategoria do Cefas não serve para famílias:** vazia em todos os 23.436 produtos; a família sai da descrição.
- **O total de conferência era outro:** os R$ 339 mil citados para a 1ª semana de agosto foram erro de transcrição; o
  extrator deu R$ 244.121,68 para 03 a 09/08/2026.
- **Histórico começa em 12/12/2023:** é quando o JP.MOVIMENTACAO começa.
- **Departamentos fora da sugestão:** padaria, confeitaria, açougue, peixes, matéria-prima e hortifrúti (`config.py`).
- **Sem estoque no cálculo:** a sugestão é uma previsão de venda em unidades ou kg; o comprador desconta o estoque e
  converte em caixas.
- **Acerto com tolerância** de 20% ou 1 unidade, porque produto de pouca saída oscila entre 0 e 3 por semana.
- **Sábado não conta** como dia útil no 5º dia útil do salário (configurável em `sistema/calendario.py`).
- **14/10, com o Paulo:** famílias por tipo + marca + tamanho mantidas; margem de acerto mantida; quer ver a quantidade
  por sabor; pedido aos fornecedores por WhatsApp; um produto pode ter 2 fornecedores.
- **19/10:** fornecedores vêm das entregas (JP.DADOSTEMPENT), não do fornecedor principal do cadastro; a casa entre
  Cefas e base local é pelo nome do fornecedor.

## Melhorias pendentes

Em ordem de prioridade.

| # | Melhoria | Por quê | Esforço |
| --- | --- | --- | --- |
| 1 | Conferir com o Paulo os fornecedores de cada produto | Vem o histórico inteiro de entregas; tirar quem não entrega mais | Pequeno (é uso da tela) |
| 2 | Liberar 2027 na tela do calendário | A tela só mostra 2026; em dezembro as compras já serão para janeiro (o cálculo já funciona em qualquer ano) | Pequeno |
| 3 | Revisar as famílias com o Paulo | Sandálias não têm tamanho na descrição (SAND HAV juntou 231 produtos); alguns tipos, como FEIJAO CARIOCA, ficaram como se fossem marca | Médio |
| 4 | Descontar o estoque da sugestão | Hoje o Paulo desconta o estoque de cabeça | Médio, se o estoque do Cefas for confiável |
| 5 | Converter a sugestão em caixas | O pedido é feito em caixas; o Cefas tem a embalagem master | Pequeno |
| 6 | Marcar semana atípica e promoção pela tela | A base já tem a marca de dia atípico, mas sem tela; promoção infla a mediana das semanas seguintes | Pequeno |
| 7 | Tratar falta de produto na prateleira | Semana sem venda por ruptura puxa a sugestão para baixo; cruzar com a lista de alerta | Médio |
| 8 | Evolução do acerto semana a semana | Depois de algumas semanas de uso, mostra se os ajustes estão melhorando a sugestão | Pequeno |
| 9 | Produtos sazonais (Páscoa, Natal, festa junina) | A mediana de 6 semanas não enxerga o pico do ano; usar a mesma semana do ano passado | Médio |
| 10 | Backup semanal fora da máquina automático | Hoje depende de alguém copiar | Pequeno |
| 11 | Guardar o código do Cefas no fornecedor | Se o Paulo renomear um fornecedor do Cefas, o próximo produto novo dele recria o nome antigo | Pequeno |
| 12 | IA para explicar variações e responder perguntas sobre as vendas (fase 3) | Previsto na arquitetura; sempre sobre os números do motor | Grande |

## Perguntas para o dono do mercado

**Instalação**
- [x] Em qual computador o sistema roda? No computador `192.168.0.108` da rede do mercado.
- [x] Quem libera o usuário somente leitura e o acesso remoto? Feitos por nós: `iacompras` pelo SQL Navigator; AnyDesk.
- [ ] Quem além do Paulo vai usar o sistema? Cada um precisa de um usuário.
- [ ] Pode nos passar o total de vendas de uma semana tirado de um relatório do Cefas, para conferir a carga no computador do mercado?

**Calendário**
- [ ] O salário da região cai até o 5º dia útil? O sábado conta nessa contagem?
- [ ] A recarga do cartão alimentação cai nos dias 1 e 20? De quais cartões ou empresas?
- [ ] Tem outros dias que vendem muito ou pouco: eventos da cidade, feiras, pagamento de alguma empresa grande?

**Compra e fornecedores**
- [ ] A compra é feita só na segunda, para a semana seguinte? Quanto tempo o fornecedor leva para entregar?
- [x] Cada produto vem de um fornecedor só? Não: pode ter 2 ou mais (14/10).
- [x] O pedido vai por e-mail, WhatsApp ou pelo vendedor? WhatsApp (14/10).
- [ ] O Paulo escolhe o fornecedor por família ou por produto? (a tela de Produtos serve aos dois)
- [ ] O pedido é feito em caixas? A quantidade por caixa do cadastro do Cefas está certa?

**Estoque e promoções**
- [ ] O estoque que aparece no Cefas bate com a prateleira? Fazem inventário, com que frequência?
- [ ] Fazem encarte ou promoção? Onde ficam registradas as datas e os produtos?

**Famílias e departamentos**
- [x] Juntar os sabores de uma mesma marca e tamanho numa linha só é como ele compra? Sim, mantido (14/10).
- [ ] E sandália: por modelo ou por tamanho?
- [ ] Padaria, açougue, peixes e hortifrúti devem continuar fora da sugestão?

**Validação**
- [x] Quanto de diferença entre sugestão e venda é aceitável? Até 20%, ou 1 unidade nos pequenos: mantido (14/10).
- [ ] Depois das 2 a 3 semanas de teste, o que precisa acontecer para ele adotar o sistema?

## Histórico de mudanças

Mais recente primeiro. Cada mudança no sistema ganha uma linha aqui.

| Data | Mudança | Detalhe |
| --- | --- | --- |
| 20/10 | Documentação em Markdown | Este arquivo substitui o `.docx` de 07/10 e passa a ser atualizado a cada mudança |
| 19/10 | Cadastro de fornecedores com busca | Com os ~600 fornecedores do Cefas a tela ficou lenta: sem busca, mostra os 50 que fornecem mais produtos |
| 19/10 | Rotina não para sem permissão | Se faltar `GRANT SELECT` nos fornecedores, o log avisa e as vendas seguem |
| 19/10 | Permissões no Oracle | `GRANT SELECT` em JP.FORNECEDOR e JP.DADOSTEMPENT para o `iacompras`, pelo SQL Navigator (estava dando ORA-00942) |
| 19/10 | Fornecedores importados do Cefas | O extrator liga cada produto a quem já o entregou (JP.DADOSTEMPENT); padrão na sugestão = último que entregou |
| 19/10 | Tarefas agendadas no mercado | "Borges - servidor" e "Borges - rotina noturna" criadas; até aí a rotina da noite não tinha rodado nenhuma vez |
| 19/10 | Instalação confirmada | Sistema no ar no computador do mercado; manutenção pelo AnyDesk; INSTALACAO.md com problemas comuns (janela "Selecionar", como saber se o `atualizar.bat` deu certo) |
| 15/10 | Roteiro de instalação e `atualizar.bat` | Instalação no computador do mercado; atualizar com dois cliques |
| 14/10 | Pedido pelo WhatsApp | "Salvar e mandar pedido" abre o WhatsApp com o pedido do fornecedor já escrito |
| 14/10 | Fornecedor por produto na sugestão | Escolha do fornecedor de cada produto e filtro por fornecedor |
| 14/10 | Produto ↔ fornecedores | Mais de um fornecedor por produto, tela e planilha; sai a ligação por departamento |
| 14/10 | Reunião com o Paulo | Branch `relatorio` aprovada e juntada na `main`; decisões em [Decisões](#decisões) |
| 13/10 | Projeto em pastas | `sistema/`, `ferramentas/`, `testes/`, `docs/` |
| 13/10 | Cadastro de fornecedores | Tela de cadastro (a ligação por departamento foi trocada em 14/10) |
| 07/10 | Tela de famílias mais rápida | Travava com a base real |
| 07/10 | Acompanhamento da sugestão | Compara sugerido, comprado e vendido numa semana fechada |
| 07/10 | Famílias e sabores | Família = tipo + marca + tamanho; tela e planilha; quanto comprar de cada sabor |
| 07/10 | Preparação da instalação | Servidor waitress na porta 8000, rotina noturna, backup diário (14 cópias), INSTALACAO.md |
| 06/10 | Tela de sugestão mais rápida | Um departamento por vez e cálculo guardado até a base mudar |
| 06/10 | Telas na base real + login | Fim dos dados fictícios; senha criptografada por usuário |
| 06/10 | Lista de alerta | Produtos que vendem em 70% das semanas e estão há 7 dias ou mais sem vender |
| 06/10 | Motor de sugestão | Mediana das 6 últimas semanas do mesmo tipo |
| 05/10 | Base, extrator e calendário | SQLite, extrator do Cefas, regras de salário, recarga e feriados |
| 05/10 | Exploração do Oracle | Mapa das tabelas do Cefas; vendas em JP.MOVIMENTACAO |
| 03/10 | Arquitetura | Documento inicial em `docs/Arquitetura do Sistema ... .docx` |

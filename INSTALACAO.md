# Instalação no Supermercado Borges (Windows)

Etapa 5 da ordem de construção. O sistema está instalado no computador do mercado:

| Item | Valor |
| --- | --- |
| Pasta do projeto | `C:\Users\Administrador\Documents\projeto\projetosupermercadoborges` |
| Endereço para o Paulo | `http://192.168.0.108:8000` |
| Oracle do Cefas | `192.168.0.250:1521/orcl`, schema JP, usuário `iacompras` (senha só no `.env`) |
| Python | 3.14 |

## Situação em 19/10/2026

- [x] Python, Git e bibliotecas instalados; `.env` preenchido; conexão com o Oracle testada
- [x] Base local trazida do notebook e atualizada pelo extrator (12/12/2023 a 15/10/2026, R$ 21,1 milhões)
- [x] Usuário `paulo` criado; telas abrindo em `http://localhost:8000`
- [x] Porta 8000 liberada no firewall
- [x] Tarefas agendadas criadas (passo 4), em 19/10: até aí a rotina da noite nunca tinha rodado
- [x] AnyDesk instalado: a manutenção é feita a distância
- [x] Fornecedores importados do Cefas (passo 8), depois de liberar a leitura de 2 tabelas para o `iacompras`
- [ ] Testar do computador do Paulo
- [ ] Reservar o IP 192.168.0.108 para este computador no roteador
- [ ] No dia seguinte, conferir `logs\rotina.log` e a pasta `backups\`
- [ ] Revisar as famílias com o Paulo antes da primeira segunda de uso
- [ ] Conferir com o Paulo se os fornecedores de cada produto fazem sentido (tirar os que não entregam mais)

## Antes de começar: como rodar os comandos

- **Um comando por vez:** cole uma linha, aperte Enter e espere terminar. Várias linhas coladas juntas viram um comando só e dão erro.
- **Terminal do VS Code** (PowerShell): os programas da pasta precisam de `.\` na frente: `.\.venv\Scripts\python ...`.
  No Prompt de Comando (cmd) funciona sem: `.venv\Scripts\python ...`. Os comandos abaixo estão no jeito do PowerShell.
- **Abra o VS Code como administrador** e com a pasta do projeto aberta (File → Open Folder): o firewall e as tarefas agendadas exigem administrador.
- **Nunca mande print do `.env` aberto:** ele tem a senha do Oracle.
- **Abrir o cmd já na pasta do projeto:** no Explorador de Arquivos, abra a pasta, clique na barra de endereço,
  digite `cmd` e aperte Enter.
- **Não clique dentro da janela preta enquanto ela trabalha.** O título vira `Selecionar ...` e o Windows **pausa o
  programa** até você apertar **Esc**. Parece travado, mas está só pausado.

## 1. Preparar o computador

1. Instale o Python (python.org): marque **"Add Python to PATH"**, clique em **Customize installation** e marque
   **"Install Python for all users"** (as tarefas agendadas rodam como SYSTEM e precisam enxergar o Python).
2. Instale o Git (git-scm.com, opções padrão): é por ele que o código chega e se atualiza.
3. Baixe o código, crie o ambiente e preencha o `.env`, um comando por vez:

```powershell
git clone https://github.com/joaocarv20/projetosupermercadoborges.git C:\Users\Administrador\Documents\projeto\projetosupermercadoborges
cd C:\Users\Administrador\Documents\projeto\projetosupermercadoborges
python -m venv .venv
.\.venv\Scripts\pip install -r requirements.txt
copy .env.example .env
notepad .env
```

No `.env`, preencha o usuário **somente leitura** do Oracle, a senha e o `ORA_DSN`. Teste a conexão (lista os
departamentos e não pesa no Oracle):

```powershell
.\.venv\Scripts\python -m ferramentas.listar_departamentos
```

## 2. Base de vendas e usuário

Há dois caminhos:

- **Reaproveitar uma base pronta** (foi o que fizemos): crie a pasta `dados` e copie para ela o `borges.db` de outra
  instalação. O extrator continua de onde a base parou, em poucos minutos.
- **Começar do zero:** sem `dados\borges.db`, o extrator copia o histórico inteiro mês a mês. Rode à noite ou no
  domingo, porque pesa no Oracle.

```powershell
.\.venv\Scripts\python extrator.py
.\.venv\Scripts\python app.py usuario paulo
```

O extrator termina com `Pronto! Base local: ...`. A senha do usuário não aparece enquanto é digitada. Para conferir
um total de período com o relatório do Cefas: `.\.venv\Scripts\python -m ferramentas.conferir_vendas`.

O extrator já junta os sabores em famílias (tipo + marca + tamanho). Antes da primeira segunda de uso, revise as
famílias com o Paulo na tela **Famílias de produto** (ou pela planilha): mudar famílias depois que ele começa a salvar
sugestões desencontra o histórico do Acompanhamento.

## 3. Testar e abrir para a rede

1. Ligue o sistema na mão e teste neste computador em `http://localhost:8000`:

   ```powershell
   .\.venv\Scripts\python app.py servir
   ```

2. Descubra o IP, num **segundo terminal** (o **+** do painel), para não desligar o servidor:

   ```powershell
   ipconfig
   ```

   Vale o **Endereço IPv4** do adaptador que tem **Gateway Padrão** (aqui, 192.168.0.108). Ignore os adaptadores do
   VMware. Peça a quem cuida da rede para **reservar esse IP** no roteador, senão ele pode mudar.

3. Libere a porta 8000 no firewall (deve responder `Ok.`):

   ```powershell
   netsh advfirewall firewall add rule name="Compras Borges" dir=in action=allow protocol=TCP localport=8000
   ```

4. Teste de outro computador da rede: `http://192.168.0.108:8000`.
5. Desligue o servidor manual com **Ctrl+C** antes do passo 4.

## 4. Deixar automático

Servidor das telas, ao ligar o computador, e rotina noturna (vendas de ontem + backup) às 3h, um comando por vez:

```powershell
schtasks /Create /TN "Borges - servidor" /TR "C:\Users\Administrador\Documents\projeto\projetosupermercadoborges\iniciar_servidor.bat" /SC ONSTART /RU SYSTEM
schtasks /Create /TN "Borges - rotina noturna" /TR "C:\Users\Administrador\Documents\projeto\projetosupermercadoborges\rotina_noturna.bat" /SC DAILY /ST 03:00 /RU SYSTEM
schtasks /Run /TN "Borges - servidor"
```

Abra `http://192.168.0.108:8000` de novo: agora quem liga o sistema é a tarefa. A sugestão da semana não precisa de
tarefa própria: é calculada quando a tela abre.

Sem as tarefas, o sistema só fica no ar com dois cliques no `iniciar_servidor.bat`, e **cai quando essa janela é
fechada** ou o computador reinicia. A janela fica vazia de propósito: as mensagens vão para `logs\servidor.log`.
Se a pasta `logs` não existe, nem o servidor nem a rotina da noite rodaram nenhuma vez pelo `.bat`.

## 5. Backup

- Toda madrugada: `backups\borges-AAAA-MM-DD.db` (guarda os 14 últimos).
- **Uma vez por semana**, copie o backup mais novo para fora da máquina (pen drive ou nuvem).
- Para restaurar: pare o servidor, copie o backup para `dados\borges.db` e ligue de novo.

## 6. Conferir se está rodando

- `logs\rotina.log`: a última linha de cada noite deve ser `Backup: ...`, com o `Pronto!` do extrator antes.
- `logs\servidor.log`: erros do servidor.

## 7. Atualizar o sistema

As mudanças são feitas e testadas no notebook e enviadas ao GitHub (`main`). Para trazê-las para cá, dê dois
cliques em **`atualizar.bat`** (ou rode-o pelo AnyDesk): ele baixa a versão nova, instala o que faltar e reinicia o
servidor. Se o `git pull` falhar, nada é reiniciado e o sistema continua na versão anterior.

Ele termina parado em `Pressione qualquer tecla para continuar...`. Deu certo se aparecer, nessa ordem:

- `Already up to date.` ou a lista de arquivos baixados;
- `ÊXITO: Tentativa de executar a tarefa agendada "Borges - servidor".`;
- `Sistema atualizado.`

Se aparecer `ERRO: O sistema não pode encontrar o arquivo especificado.` antes de `Sistema atualizado.`, a tarefa
"Borges - servidor" não existe: o sistema foi desligado e não voltou. Ligue com o `iniciar_servidor.bat` e crie as
tarefas (passo 4). Uns 1 a 2 minutos são normais (o `pip install` confere os pacotes).

- **Nunca edite o código direto neste computador:** o `git pull` falha se houver arquivo alterado aqui.
- **Cópia antiga, sem o `atualizar.bat`:** rode `git pull` uma vez no cmd da pasta; o arquivo aparece e serve
  daí em diante.
- **A base (`dados\borges.db`) não vai para o GitHub:** a deste computador é a de verdade, com o que o Paulo salva.

## 8. Permissões no Oracle e fornecedores do Cefas

O usuário `iacompras` só lê (`SELECT`) as tabelas que receberam permissão. Tabela sem permissão dá
`ORA-00942: a tabela ou view não existe`, mesmo existindo. Ele lê hoje: `JP.PRODUTO`, `JP.DEPTO`, `JP.MOVIMENTACAO`,
`JP.FORNECEDOR` e `JP.DADOSTEMPENT`.

Para liberar uma tabela nova: abra o **SQL Navigator** deste servidor conectado como **JP** (o dono das tabelas) e rode,
por exemplo:

```sql
GRANT SELECT ON JP.FORNECEDOR TO IACOMPRAS;
GRANT SELECT ON JP.DADOSTEMPENT TO IACOMPRAS;
```

Deve aparecer `SQL statement executed`; vale na hora, sem COMMIT. Ao fechar, o SQL Navigator pergunta se quer salvar o
script: **Clear All** e **OK** (não precisa salvar).

**Fornecedores:** toda noite o extrator lê em `JP.DADOSTEMPENT` (uma linha por entrada de mercadoria) quem já entregou
cada produto, e liga o produto a esse fornecedor, trazendo o nome e o telefone de `JP.FORNECEDOR`. No log aparece
`... pares produto-fornecedor com entrada no Cefas (... ligações novas)`.

- Cada par produto-fornecedor só é ligado na 1ª vez: o que o Paulo tira na tela **não volta** na noite seguinte.
- Fornecedor com o mesmo nome de um já cadastrado é o mesmo; telefone e contato digitados à mão não são trocados.
- Na sugestão, o fornecedor que já vem marcado é o último que entregou (até o Paulo escolher outro).
- Vem o histórico inteiro de entregas: um produto pode aparecer com fornecedores que já não entregam. Tire pela tela.
- Se faltar permissão, o log mostra `Fornecedores não importados (as vendas foram): ...` e o resto da rotina segue.
- Com ~600 fornecedores, a tela **Fornecedores > Cadastro** mostra só os 50 que fornecem mais produtos; os outros,
  pela busca (nome, contato ou telefone).

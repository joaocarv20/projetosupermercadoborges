# Instalação no Supermercado Borges (Windows)

Etapa 5 da ordem de construção. O sistema está instalado no computador do mercado:

| Item | Valor |
| --- | --- |
| Pasta do projeto | `C:\Users\Administrador\Documents\projeto\projetosupermercadoborges` |
| Endereço para o Paulo | `http://192.168.0.108:8000` |
| Oracle do Cefas | `192.168.0.250:1521/orcl`, schema JP (usuário e senha só no `.env`) |
| Python | 3.14 |

## Situação em 15/10/2026

- [x] Python, Git e bibliotecas instalados; `.env` preenchido; conexão com o Oracle testada
- [x] Base local trazida do notebook e atualizada pelo extrator (12/12/2023 a 15/10/2026, R$ 21,1 milhões)
- [x] Usuário `paulo` criado; telas abrindo em `http://localhost:8000`
- [x] Porta 8000 liberada no firewall
- [ ] Testar do computador do Paulo
- [ ] Reservar o IP 192.168.0.108 para este computador no roteador
- [ ] Criar as tarefas agendadas (passo 4)
- [ ] No dia seguinte, conferir `logs\rotina.log` e a pasta `backups\`
- [ ] Instalar AnyDesk ou Tailscale para manutenção a distância
- [ ] Revisar as famílias com o Paulo antes da primeira segunda de uso

## Antes de começar: como rodar os comandos

- **Um comando por vez:** cole uma linha, aperte Enter e espere terminar. Várias linhas coladas juntas viram um comando só e dão erro.
- **Terminal do VS Code** (PowerShell): os programas da pasta precisam de `.\` na frente: `.\.venv\Scripts\python ...`.
  No Prompt de Comando (cmd) funciona sem: `.venv\Scripts\python ...`. Os comandos abaixo estão no jeito do PowerShell.
- **Abra o VS Code como administrador** e com a pasta do projeto aberta (File → Open Folder): o firewall e as tarefas agendadas exigem administrador.
- **Nunca mande print do `.env` aberto:** ele tem a senha do Oracle.

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

- **Nunca edite o código direto neste computador:** o `git pull` falha se houver arquivo alterado aqui.
- **A base (`dados\borges.db`) não vai para o GitHub:** a deste computador é a de verdade, com o que o Paulo salva.

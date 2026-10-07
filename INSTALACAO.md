# Instalação no Supermercado Borges (Windows)

Etapa 5 da ordem de construção. Exemplo com o projeto em `C:\compras-borges`; abra o **Prompt de Comando como administrador**.

## 1. Preparar o computador

1. Instale o Python 3.13 (python.org), marcando **"Add Python to PATH"**.
2. Copie a pasta do projeto para `C:\compras-borges` (sem `.venv`, `dados` e `__pycache__`).
3. Dê um **IP fixo** a este computador no roteador (ex.: 192.168.0.50); é o endereço que o Paulo vai usar.

```bat
cd C:\compras-borges
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
copy .env.example .env
notepad .env
```

No `.env`, preencha o usuário **somente leitura** do Oracle, a senha e o `ORA_DSN`.

## 2. Carga inicial e usuário

Rode fora do horário de funcionamento (à noite ou no domingo): copia todo o histórico mês a mês.

```bat
.venv\Scripts\python extrator.py
.venv\Scripts\python app.py usuario paulo
```

Confira um total de período com o relatório do Cefas antes de seguir (`conferir_vendas.py`).

O extrator já junta os sabores em famílias (tipo + marca + tamanho). Antes da primeira segunda de uso, revise as
famílias com o Paulo na tela **Famílias de produto** (ou pela planilha): mudar famílias depois que ele começa a salvar
sugestões desencontra o histórico do Acompanhamento.

## 3. Agendar as tarefas

Servidor das telas, ao ligar o computador, e rotina noturna (vendas de ontem + backup) às 3h:

```bat
schtasks /Create /TN "Borges - servidor" /TR "C:\compras-borges\iniciar_servidor.bat" /SC ONSTART /RU SYSTEM
schtasks /Create /TN "Borges - rotina noturna" /TR "C:\compras-borges\rotina_noturna.bat" /SC DAILY /ST 03:00 /RU SYSTEM
schtasks /Run /TN "Borges - servidor"
```

Liberar a porta 8000 no firewall para os outros computadores da rede:

```bat
netsh advfirewall firewall add rule name="Compras Borges" dir=in action=allow protocol=TCP localport=8000
```

Teste em outro computador: `http://192.168.0.50:8000`.

A sugestão da semana não precisa de tarefa própria: é calculada quando a tela abre (só a primeira abertura depois da rotina noturna demora alguns segundos).

## 4. Backup

- Toda madrugada: `backups\borges-AAAA-MM-DD.db` (guarda os 14 últimos).
- **Uma vez por semana**, copie o backup mais novo para fora da máquina (pen drive ou nuvem).
- Para restaurar: pare o servidor, copie o backup para `dados\borges.db` e ligue de novo.

## 5. Conferir se está rodando

- `logs\rotina.log`: a última linha de cada noite deve ser `Backup: ...`, com o `Pronto!` do extrator antes.
- `logs\servidor.log`: erros do servidor.
- Acesso remoto para manutenção: AnyDesk ou Tailscale.

# Compras Inteligentes – Supermercado Borges

Sugestão de compra semanal a partir das vendas do Cefas. Documentação: [docs/DOCUMENTACAO.md](docs/DOCUMENTACAO.md).
Instalação no mercado: [INSTALACAO.md](INSTALACAO.md).

```
app.py              abre o sistema (telas)          python app.py
extrator.py         copia vendas e fornecedores     python extrator.py
                    do Cefas
rotina_noturna.py   extrator + backup, de madrugada
config.py           o que dá para ajustar (margens, departamentos fora, qualificadores)
*.bat               chamados pelo Agendador de Tarefas do Windows

sistema/            as peças: base local, motor da sugestão, famílias, alertas, acompanhamento,
                    calendário e conexão com o Oracle (oracle.py)
ferramentas/        investigação do Cefas, uso raro:  python -m ferramentas.conferir_vendas 2026-08-01 2026-08-07
testes/             um teste por peça:                python -m testes.test_app
docs/               DOCUMENTACAO.md (atualizar a cada mudança) e mapas do banco
templates/, static/ telas
dados/              a base local (fora do Git)
```

Todos os comandos rodam da pasta principal do projeto.

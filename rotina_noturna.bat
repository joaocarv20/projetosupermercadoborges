@echo off
rem Chamado pelo Agendador de Tarefas toda madrugada (ver INSTALACAO.md)
cd /d "%~dp0"
if not exist logs mkdir logs
.venv\Scripts\python.exe rotina_noturna.py >> logs\rotina.log 2>&1

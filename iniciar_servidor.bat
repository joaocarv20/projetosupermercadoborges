@echo off
rem Chamado pelo Agendador de Tarefas ao ligar o computador (ver INSTALACAO.md)
cd /d "%~dp0"
if not exist logs mkdir logs
.venv\Scripts\python.exe -u app.py servir >> logs\servidor.log 2>&1

@echo off
rem Baixa a versao nova do GitHub e reinicia o sistema. Rode no computador do mercado (ver INSTALACAO.md).
cd /d "%~dp0"
git pull || (echo Falhou o git pull. Nada foi reiniciado. & pause & exit /b 1)
.venv\Scripts\pip install -q -r requirements.txt
rem Para o servidor que esta na porta 8000 e liga de novo pela tarefa agendada
for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":8000 " ^| findstr LISTENING') do taskkill /F /PID %%a >nul
timeout /t 3 >nul
schtasks /Run /TN "Borges - servidor"
echo.
echo Sistema atualizado.
pause

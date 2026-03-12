@echo off
echo Iniciando la Web App de Tiempo...
:: Se para en la carpeta donde esta este archivo
cd /d %~dp0
:: Activa el entorno virtual
call venv\Scripts\activate
:: Corre la aplicacion
python app.py
pause

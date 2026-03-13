@echo off
echo Iniciando la Web App de Tiempo...
cd /d %~dp0
:: Activa el entorno virtual
call venv\Scripts\activate
:: Usamos 'python -m streamlit' para evitar errores de rutas fijas en el ejecutable
python -m streamlit run app.py
pause

@echo off
cd /d "%~dp0"

call karyanaenv\Scripts\activate.bat

python -m streamlit run app.py
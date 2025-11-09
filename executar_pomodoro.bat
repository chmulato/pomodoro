@echo off
chcp 65001 >nul
title Pomodoro Timer

echo ====================================
echo   Pomodoro Timer / Cronômetro Pomodoro
echo ====================================
echo.

REM Verifica se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERRO: Python não encontrado!
    echo ERROR: Python non trovato!
    echo.
    echo Instale Python 3.7+ de / Installa Python 3.7+ da:
    echo https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✓ Python encontrado / Python trovato
echo.

REM Verifica se as dependências estão instaladas
echo Verificando dependências / Verifica delle dipendenze...
python -c "import tkinter; from PIL import Image" >nul 2>&1
if errorlevel 1 (
    echo.
    echo Instalando dependências / Installazione delle dipendenze...
    python -m pip install -r requirements.txt
    echo.
)

echo ✓ Dependências OK / Dipendenze OK
echo.

REM Executa o aplicativo
echo Iniciando aplicativo / Avvio dell'applicazione...
echo.
python pomodoro.py

if errorlevel 1 (
    echo.
    echo ERRO ao executar / ERRORE durante l'esecuzione
    pause
)

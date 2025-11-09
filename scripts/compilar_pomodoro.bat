@echo off
chcp 65001 >nul
title Compilar Pomodoro Timer

echo ====================================
echo   Compilar Pomodoro Timer
echo   Compilare Cronômetro Pomodoro
echo ====================================
echo.

REM Verifica se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERRO: Python não encontrado!
    echo ERROR: Python non trovato!
    pause
    exit /b 1
)

echo Executando script de compilação...
echo Esecuzione dello script di compilazione...
echo.

python pomodoro_exe.py

if errorlevel 1 (
    echo.
    echo ERRO na compilação / ERRORE nella compilazione
    pause
    exit /b 1
)

echo.
echo ====================================
echo   Compilação Concluída!
echo   Compilazione Completata!
echo ====================================
pause

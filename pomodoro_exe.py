"""
Script para compilar o Pomodoro Timer em executável Windows

Este script utiliza PyInstaller para criar um executável standalone
do aplicativo Pomodoro Timer, incluindo todos os recursos necessários.

Autor: Christian Vladimir Uhdre Mulato
Data: 09 de Novembro de 2025
"""

import os
import subprocess
import sys
import shutil

def print_header():
    """Imprime cabeçalho"""
    print("=" * 60)
    print("Compilador Pomodoro Timer / Compilatore Cronômetro Pomodoro")
    print("=" * 60)
    print()

def check_pyinstaller():
    """Verifica se PyInstaller está instalado"""
    try:
        import PyInstaller
        print("✓ PyInstaller encontrado")
        return True
    except ImportError:
        print("✗ PyInstaller não encontrado")
        print()
        print("Instalando PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller>=6.0.0"])
        print("✓ PyInstaller instalado com sucesso")
        return True

def check_files():
    """Verifica arquivos necessários"""
    required_files = [
        "pomodoro.py",
        "pomodoro.ico",
        "pomodoro.gif"
    ]
    
    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file} encontrado")
        else:
            print(f"✗ {file} NÃO encontrado")
            missing_files.append(file)
    
    if missing_files:
        print()
        print(f"ERRO: Arquivos faltando: {', '.join(missing_files)}")
        return False
    
    return True

def compile_exe():
    """Compila o executável"""
    print()
    print("Iniciando compilação...")
    print()
    
    # Comando PyInstaller
    cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name", "pomodoro",
        "--icon", "pomodoro.ico",
        "--add-data", "pomodoro.gif;.",
        "--clean",
        "pomodoro.py"
    ]
    
    try:
        subprocess.check_call(cmd)
        print()
        print("✓ Compilação concluída com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print()
        print(f"✗ Erro na compilação: {e}")
        return False

def copy_resources():
    """Copia recursos para a pasta dist"""
    print()
    print("Copiando recursos para dist/...")
    
    resources = ["pomodoro.gif", "pomodoro.ico"]
    
    if not os.path.exists("dist"):
        os.makedirs("dist")
    
    for resource in resources:
        if os.path.exists(resource):
            shutil.copy2(resource, "dist/")
            print(f"✓ {resource} copiado")
    
    print()
    print("✓ Recursos copiados com sucesso!")

def cleanup():
    """Remove arquivos temporários"""
    print()
    print("Limpando arquivos temporários...")
    
    temp_dirs = ["build", "__pycache__"]
    temp_files = ["pomodoro.spec"]
    
    for dir_name in temp_dirs:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"✓ Pasta {dir_name} removida")
    
    for file_name in temp_files:
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"✓ Arquivo {file_name} removido")

def show_result():
    """Mostra resultado final"""
    print()
    print("=" * 60)
    print("COMPILAÇÃO CONCLUÍDA / COMPILAZIONE COMPLETATA")
    print("=" * 60)
    print()
    print("Arquivos gerados / File generati:")
    print()
    
    if os.path.exists("dist/pomodoro.exe"):
        size = os.path.getsize("dist/pomodoro.exe") / (1024 * 1024)
        print(f"  ✓ dist/pomodoro.exe ({size:.2f} MB)")
    
    if os.path.exists("dist/pomodoro.gif"):
        print(f"  ✓ dist/pomodoro.gif")
    
    if os.path.exists("dist/pomodoro.ico"):
        print(f"  ✓ dist/pomodoro.ico")
    
    print()
    print("Para distribuir / Per distribuire:")
    print("  1. Copie toda a pasta dist/")
    print("     Copia tutta la cartella dist/")
    print("  2. Execute pomodoro.exe")
    print("     Esegui pomodoro.exe")
    print()

def main():
    """Função principal"""
    print_header()
    
    # Verifica PyInstaller
    if not check_pyinstaller():
        return 1
    
    print()
    
    # Verifica arquivos
    if not check_files():
        return 1
    
    # Compila
    if not compile_exe():
        return 1
    
    # Copia recursos
    copy_resources()
    
    # Limpeza opcional
    response = input("\nRemover arquivos temporários? (S/n): ").strip().lower()
    if response in ['s', 'sim', 'si', 'yes', 'y', '']:
        cleanup()
    
    # Mostra resultado
    show_result()
    
    return 0

if __name__ == "__main__":
    try:
        exit_code = main()
        input("\nPressione Enter para sair / Premi Invio per uscire...")
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\nOperação cancelada pelo usuário / Operazione annullata dall'utente")
        sys.exit(130)
    except Exception as e:
        print(f"\n\nErro inesperado / Errore imprevisto: {e}")
        input("\nPressione Enter para sair / Premi Invio per uscire...")
        sys.exit(1)

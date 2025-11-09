#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testes End-to-End Manuais para Pomodoro Timer
Roteiro de testes para validação manual da interface gráfica
"""

import sys
import os

def print_test_header(title):
    """Imprime cabeçalho de teste"""
    print("\n" + "=" * 70)
    print(f"🧪 {title}")
    print("=" * 70)

def print_step(number, description):
    """Imprime passo do teste"""
    print(f"\n{number}. {description}")

def wait_confirmation():
    """Aguarda confirmação do usuário"""
    input("   ⏸️  Pressione ENTER para continuar...")

def test_interface_inicial():
    """Teste 1: Interface Inicial"""
    print_test_header("TESTE 1: INTERFACE INICIAL")
    
    print_step(1, "Verificar que a janela abre corretamente")
    print("   ✓ Janela deve ter título 'Pomodoro Timer'")
    print("   ✓ Timer deve mostrar '25:00'")
    print("   ✓ Status deve mostrar 'Trabalhe por 25 minutos'")
    print("   ✓ Contador de tomates deve estar vazio")
    print("   ✓ GIF do tomate deve estar animando")
    wait_confirmation()
    
    print_step(2, "Verificar botões disponíveis")
    print("   ✓ Botão 'Iniciar' deve estar visível")
    print("   ✓ Botão 'Resetar' deve estar visível")
    wait_confirmation()

def test_iniciar_timer():
    """Teste 2: Iniciar Timer"""
    print_test_header("TESTE 2: INICIAR TIMER")
    
    print_step(1, "Clicar no botão 'Iniciar' ou pressionar ESPAÇO")
    print("   ✓ Botão deve mudar para 'Pausar'")
    print("   ✓ Timer deve começar a contar regressivamente")
    print("   ✓ Timer deve mudar de 25:00 para 24:59, 24:58...")
    wait_confirmation()
    
    print_step(2, "Aguardar alguns segundos e verificar contagem")
    print("   ✓ Contagem deve ser contínua e suave")
    print("   ✓ Status deve permanecer 'Trabalhe por 25 minutos'")
    wait_confirmation()

def test_pausar_retomar():
    """Teste 3: Pausar e Retomar"""
    print_test_header("TESTE 3: PAUSAR E RETOMAR")
    
    print_step(1, "Com o timer rodando, clicar em 'Pausar' ou pressionar ESPAÇO")
    print("   ✓ Timer deve parar a contagem")
    print("   ✓ Tempo deve congelar no valor atual")
    print("   ✓ Botão deve mudar para 'Retomar'")
    wait_confirmation()
    
    print_step(2, "Clicar em 'Retomar' ou pressionar ESPAÇO novamente")
    print("   ✓ Timer deve continuar de onde parou")
    print("   ✓ Botão deve voltar para 'Pausar'")
    wait_confirmation()

def test_resetar():
    """Teste 4: Resetar Timer"""
    print_test_header("TESTE 4: RESETAR TIMER")
    
    print_step(1, "Com o timer rodando ou pausado, pressionar 'R' ou clicar em 'Resetar'")
    print("   ✓ Timer deve voltar para 25:00")
    print("   ✓ Status deve voltar para 'Trabalhe por 25 minutos'")
    print("   ✓ Botão deve voltar para 'Iniciar'")
    print("   ✓ Timer deve parar")
    wait_confirmation()

def test_completar_pomodoro():
    """Teste 5: Completar Pomodoro (Acelerado)"""
    print_test_header("TESTE 5: COMPLETAR POMODORO")
    
    print("\n⚠️  ATENÇÃO: Este teste requer modificação temporária do código!")
    print("   Para testar rapidamente, altere no pomodoro.py:")
    print("   WORK_TIME = 5  # 5 segundos ao invés de 1500")
    print("   SHORT_BREAK = 3  # 3 segundos ao invés de 300")
    wait_confirmation()
    
    print_step(1, "Iniciar timer e aguardar completar (5 segundos se modificado)")
    print("   ✓ Ao chegar em 00:00, deve tocar um som/beep")
    print("   ✓ Deve aparecer uma mensagem: 'Pomodoro Completo!'")
    print("   ✓ Contador de tomates deve incrementar: 🍅")
    print("   ✓ Timer deve trocar para pausa curta (05:00 ou 3s)")
    print("   ✓ Status deve mudar para 'Pausa curta - 5 minutos'")
    wait_confirmation()

def test_ciclo_completo():
    """Teste 6: Ciclo Completo de 4 Pomodoros"""
    print_test_header("TESTE 6: CICLO COMPLETO (4 POMODOROS)")
    
    print("\n⚠️  ATENÇÃO: Use tempos reduzidos para este teste!")
    
    print_step(1, "Completar 1º Pomodoro")
    print("   ✓ Contador: 🍅")
    print("   ✓ Próximo: Pausa curta (5 min)")
    wait_confirmation()
    
    print_step(2, "Completar 2º Pomodoro")
    print("   ✓ Contador: 🍅 🍅")
    print("   ✓ Próximo: Pausa curta (5 min)")
    wait_confirmation()
    
    print_step(3, "Completar 3º Pomodoro")
    print("   ✓ Contador: 🍅 🍅 🍅")
    print("   ✓ Próximo: Pausa curta (5 min)")
    wait_confirmation()
    
    print_step(4, "Completar 4º Pomodoro")
    print("   ✓ Contador: 🍅 🍅 🍅 🍅")
    print("   ✓ Próximo: PAUSA LONGA (30 min)")
    print("   ✓ Status: 'Pausa longa - 30 minutos'")
    wait_confirmation()
    
    print_step(5, "Completar pausa longa")
    print("   ✓ Contador deve resetar para vazio")
    print("   ✓ Volta para trabalho (25 min)")
    wait_confirmation()

def test_atalhos_teclado():
    """Teste 7: Atalhos de Teclado"""
    print_test_header("TESTE 7: ATALHOS DE TECLADO")
    
    print_step(1, "Testar atalho ESPAÇO")
    print("   ✓ Com timer parado: deve iniciar")
    print("   ✓ Com timer rodando: deve pausar")
    print("   ✓ Com timer pausado: deve retomar")
    wait_confirmation()
    
    print_step(2, "Testar atalho R")
    print("   ✓ Em qualquer estado: deve resetar timer")
    print("   ✓ Timer volta para 25:00")
    wait_confirmation()
    
    print_step(3, "Testar atalho ESC")
    print("   ✓ Deve fechar a aplicação")
    print("   ⚠️  NÃO EXECUTE AINDA - Teste por último!")
    wait_confirmation()

def test_logging():
    """Teste 8: Sistema de Log"""
    print_test_header("TESTE 8: SISTEMA DE LOG")
    
    print_step(1, "Executar alguns ciclos do timer")
    print("   ✓ Iniciar, pausar, resetar, completar pomodoro")
    wait_confirmation()
    
    print_step(2, "Fechar aplicação e verificar arquivo pomodoro_log.txt")
    print("   ✓ Arquivo deve existir na pasta do projeto")
    print("   ✓ Deve conter timestamps no formato [YYYY-MM-DD HH:MM:SS]")
    print("   ✓ Deve registrar eventos: INÍCIO, PAUSA, RETOMADA, RESET, COMPLETO")
    wait_confirmation()

def test_animacao_gif():
    """Teste 9: Animações GIF"""
    print_test_header("TESTE 9: ANIMAÇÕES GIF")
    
    print_step(1, "Durante período de trabalho")
    print("   ✓ GIF pomodoro.gif deve estar animando (tomate pulsando)")
    wait_confirmation()
    
    print_step(2, "Durante pausa curta (se implementado)")
    print("   ✓ GIF pode mudar para pomodoro_break.gif")
    wait_confirmation()
    
    print_step(3, "Durante pausa longa (se implementado)")
    print("   ✓ GIF pode mudar para pomodoro_longbreak.gif (com Zzz)")
    wait_confirmation()

def test_bilinguismo():
    """Teste 10: Suporte Bilíngue"""
    print_test_header("TESTE 10: SUPORTE BILÍNGUE (PT/IT)")
    
    print_step(1, "Verificar mensagens em Português")
    print("   ✓ Status: 'Trabalhe por 25 minutos'")
    print("   ✓ Notificação: 'Pomodoro Completo!'")
    wait_confirmation()
    
    print_step(2, "Verificar mensagens em Italiano")
    print("   ✓ Status: 'Lavora per 25 minuti'")
    print("   ✓ Notificação: 'Pomodoro Completato!'")
    print("   ⚠️  Pode estar apenas em PT - verificar código")
    wait_confirmation()

def main():
    """Função principal"""
    print("\n" + "=" * 70)
    print("🍅 ROTEIRO DE TESTES END-TO-END - POMODORO TIMER")
    print("=" * 70)
    print("\n📋 Este roteiro guiará você pelos testes manuais da aplicação.")
    print("   Certifique-se de que a aplicação está rodando antes de começar.")
    print("\n⚠️  DICA: Para testes rápidos, modifique temporariamente os tempos:")
    print("   WORK_TIME = 5  # 5 segundos")
    print("   SHORT_BREAK = 3  # 3 segundos")
    print("   LONG_BREAK = 10  # 10 segundos")
    
    wait_confirmation()
    
    try:
        # Executar todos os testes
        test_interface_inicial()
        test_iniciar_timer()
        test_pausar_retomar()
        test_resetar()
        test_completar_pomodoro()
        test_ciclo_completo()
        test_atalhos_teclado()
        test_logging()
        test_animacao_gif()
        test_bilinguismo()
        
        print("\n" + "=" * 70)
        print("✅ ROTEIRO DE TESTES CONCLUÍDO!")
        print("=" * 70)
        print("\n📝 Próximos passos:")
        print("   1. Revisar pomodoro_log.txt")
        print("   2. Documentar bugs encontrados")
        print("   3. Restaurar tempos originais se modificados")
        print("   4. Testar compilação com pomodoro_exe.py")
        print()
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Testes interrompidos pelo usuário.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

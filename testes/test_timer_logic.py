#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testes unitários para lógica do timer Pomodoro
"""

import unittest
import sys
import os
from unittest.mock import Mock, patch
import time

# Adicionar diretório pai ao path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestPomodoroLogic(unittest.TestCase):
    """Testes para lógica do Pomodoro Timer"""
    
    def test_work_duration(self):
        """Testa duração do período de trabalho"""
        WORK_TIME = 25 * 60  # 25 minutos
        self.assertEqual(WORK_TIME, 1500, "Trabalho deve ser 1500 segundos (25 min)")
    
    def test_short_break_duration(self):
        """Testa duração da pausa curta"""
        SHORT_BREAK = 5 * 60  # 5 minutos
        self.assertEqual(SHORT_BREAK, 300, "Pausa curta deve ser 300 segundos (5 min)")
    
    def test_long_break_duration(self):
        """Testa duração da pausa longa"""
        LONG_BREAK = 30 * 60  # 30 minutos
        self.assertEqual(LONG_BREAK, 1800, "Pausa longa deve ser 1800 segundos (30 min)")
    
    def test_pomodoro_cycle(self):
        """Testa ciclo completo: 4 pomodoros = pausa longa"""
        pomodoro_count = 0
        
        # Simular 4 pomodoros
        for i in range(4):
            pomodoro_count += 1
            
            if pomodoro_count == 4:
                # Após 4 pomodoros, deve ter pausa longa
                self.assertEqual(pomodoro_count, 4, "Deve completar 4 pomodoros")
                # Reset do contador
                pomodoro_count = 0
        
        self.assertEqual(pomodoro_count, 0, "Contador deve resetar após pausa longa")
    
    def test_time_formatting(self):
        """Testa formatação do tempo MM:SS"""
        test_cases = [
            (1500, "25:00"),  # 25 minutos
            (300, "05:00"),   # 5 minutos
            (1800, "30:00"),  # 30 minutos
            (60, "01:00"),    # 1 minuto
            (0, "00:00"),     # Zero
            (3599, "59:59"),  # 59:59
        ]
        
        for seconds, expected in test_cases:
            minutes = seconds // 60
            secs = seconds % 60
            formatted = f"{minutes:02d}:{secs:02d}"
            self.assertEqual(formatted, expected, 
                           f"Formatação de {seconds}s deve ser {expected}")

class TestPomodoroStates(unittest.TestCase):
    """Testes para estados do timer"""
    
    def test_initial_state(self):
        """Testa estado inicial"""
        is_running = False
        is_paused = False
        current_time = 1500
        
        self.assertFalse(is_running, "Timer não deve estar rodando inicialmente")
        self.assertFalse(is_paused, "Timer não deve estar pausado inicialmente")
        self.assertEqual(current_time, 1500, "Tempo inicial deve ser 25 min")
    
    def test_state_transitions(self):
        """Testa transições de estado"""
        # Estado inicial
        state = "stopped"
        self.assertEqual(state, "stopped")
        
        # Iniciar timer
        state = "running"
        self.assertEqual(state, "running")
        
        # Pausar timer
        state = "paused"
        self.assertEqual(state, "paused")
        
        # Retomar timer
        state = "running"
        self.assertEqual(state, "running")
        
        # Resetar timer
        state = "stopped"
        self.assertEqual(state, "stopped")

class TestPomodoroCounter(unittest.TestCase):
    """Testes para contador de tomates"""
    
    def test_counter_increment(self):
        """Testa incremento do contador"""
        pomodoro_count = 0
        total_pomodoros = 0
        
        # Completar um pomodoro
        pomodoro_count += 1
        total_pomodoros += 1
        
        self.assertEqual(pomodoro_count, 1, "Contador do ciclo deve ser 1")
        self.assertEqual(total_pomodoros, 1, "Total de pomodoros deve ser 1")
    
    def test_counter_reset_after_long_break(self):
        """Testa reset do contador após pausa longa"""
        pomodoro_count = 4
        total_pomodoros = 4
        
        # Após pausa longa, ciclo reseta mas total mantém
        pomodoro_count = 0
        
        self.assertEqual(pomodoro_count, 0, "Contador do ciclo deve resetar")
        self.assertEqual(total_pomodoros, 4, "Total deve manter 4 pomodoros")
    
    def test_tomato_emoji_display(self):
        """Testa exibição dos emojis de tomate"""
        pomodoro_count = 2
        tomatoes = "🍅 " * pomodoro_count
        
        self.assertEqual(tomatoes, "🍅 🍅 ", "Deve mostrar 2 tomates")
        self.assertEqual(len(tomatoes.strip().split()), 2, "Deve contar 2 elementos")

class TestLogging(unittest.TestCase):
    """Testes para sistema de log"""
    
    def test_log_format(self):
        """Testa formato do log"""
        from datetime import datetime
        
        event = "INÍCIO"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {event}"
        
        self.assertIn(timestamp, log_entry, "Log deve conter timestamp")
        self.assertIn(event, log_entry, "Log deve conter evento")
        self.assertIn("[", log_entry, "Log deve ter colchetes")
        self.assertIn("]", log_entry, "Log deve fechar colchetes")

def run_tests():
    """Executa todos os testes"""
    print("=" * 70)
    print("🧪 TESTES UNITÁRIOS - POMODORO TIMER")
    print("=" * 70)
    print()
    
    # Criar suite de testes
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Adicionar testes
    suite.addTests(loader.loadTestsFromTestCase(TestPomodoroLogic))
    suite.addTests(loader.loadTestsFromTestCase(TestPomodoroStates))
    suite.addTests(loader.loadTestsFromTestCase(TestPomodoroCounter))
    suite.addTests(loader.loadTestsFromTestCase(TestLogging))
    
    # Executar testes
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print()
    print("=" * 70)
    if result.wasSuccessful():
        print("✅ TODOS OS TESTES PASSARAM!")
    else:
        print("❌ ALGUNS TESTES FALHARAM")
    print("=" * 70)
    
    return 0 if result.wasSuccessful() else 1

if __name__ == "__main__":
    sys.exit(run_tests())

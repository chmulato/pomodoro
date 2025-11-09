#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pomodoro Timer - Versão de Teste Rápido
Tempos reduzidos para validação rápida do ciclo completo
"""

import tkinter as tk
from tkinter import messagebox
import threading
import time
import datetime
import os
from PIL import Image, ImageTk

class PomodoroTimerTest:
    def __init__(self, root):
        self.root = root
        self.root.title("🧪 Pomodoro Timer - TESTE RÁPIDO")
        self.root.geometry("500x650")
        self.root.resizable(False, False)
        self.root.configure(bg="#ffffff")
        
        # Estados do timer
        self.is_running = False
        self.is_work_time = True
        self.pomodoro_count = 0
        self.total_pomodoros = 0
        
        # TEMPOS REDUZIDOS PARA TESTE
        self.WORK_TIME = 5  # 5 segundos (ao invés de 1500)
        self.SHORT_BREAK = 3  # 3 segundos (ao invés de 300)
        self.LONG_BREAK = 10  # 10 segundos (ao invés de 1800)
        
        self.time_left = self.WORK_TIME
        self.timer_thread = None
        
        # Garante que o arquivo de log exista
        if not os.path.exists("pomodoro_test_log.txt"):
            with open("pomodoro_test_log.txt", "w", encoding="utf-8") as f:
                f.write("=== POMODORO TIMER - LOG DE TESTES ===\n")
                f.write(f"Iniciado em: {datetime.datetime.now():%Y-%m-%d %H:%M:%S}\n\n")
        
        # Tenta definir o ícone
        try:
            self.root.iconbitmap("img/pomodoro.ico")
        except:
            pass
        
        # Carrega animação do tomate
        self.frames = []
        self.load_gif_animation()
        
        # Interface
        self.setup_ui()
        
        # Inicia animação
        if self.frames:
            self.animate_gif()
        
        # Log de inicialização
        self.log_event("🧪 TESTE INICIADO - Tempos reduzidos: 5s trabalho, 3s pausa curta, 10s pausa longa")
        
        # Bind de atalhos de teclado
        self.root.bind('<space>', lambda e: self.toggle_timer())
        self.root.bind('<r>', lambda e: self.reset_timer())
        self.root.bind('<Escape>', lambda e: self.root.quit())
    
    def load_gif_animation(self):
        """Carrega frames do GIF animado"""
        try:
            gif = Image.open("img/pomodoro.gif")
            for frame in range(0, getattr(gif, "n_frames", 1)):
                gif.seek(frame)
                frame_image = gif.copy().resize((150, 150), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(frame_image)
                self.frames.append(photo)
        except Exception as e:
            print(f"Erro ao carregar img/pomodoro.gif: {e}")
            self.frames = []
    
    def setup_ui(self):
        """Configura a interface gráfica"""
        # Banner de teste
        test_banner = tk.Label(
            self.root,
            text="⚠️ MODO DE TESTE RÁPIDO ⚠️",
            font=("Arial", 12, "bold"),
            bg="#ff9800",
            fg="white",
            pady=5
        )
        test_banner.pack(fill=tk.X)
        
        test_info = tk.Label(
            self.root,
            text="Trabalho: 5s | Pausa curta: 3s | Pausa longa: 10s",
            font=("Arial", 9),
            bg="#fff3e0",
            fg="#e65100"
        )
        test_info.pack(fill=tk.X)
        
        # Frame superior - Animação
        top_frame = tk.Frame(self.root, bg="#ffffff")
        top_frame.pack(pady=10)
        
        self.img_label = tk.Label(top_frame, bg="#ffffff")
        self.img_label.pack()
        self.current_frame = 0
        
        # Status (Trabalho/Pausa)
        self.status_label = tk.Label(
            self.root,
            text="TRABALHO / LAVORO",
            font=("Arial", 16, "bold"),
            fg="#d32f2f",
            bg="#ffffff"
        )
        self.status_label.pack(pady=5)
        
        # Timer display
        self.timer_label = tk.Label(
            self.root,
            text="00:05",
            font=("Arial", 48, "bold"),
            fg="#2e7d32",
            bg="#ffffff"
        )
        self.timer_label.pack(pady=10)
        
        # Contador de pomodoros
        self.pomodoro_display = tk.Label(
            self.root,
            text="🍅 " * self.pomodoro_count,
            font=("Arial", 24),
            bg="#ffffff"
        )
        self.pomodoro_display.pack(pady=5)
        
        self.count_label = tk.Label(
            self.root,
            text=f"Pomodoros: {self.total_pomodoros}",
            font=("Arial", 12),
            bg="#ffffff"
        )
        self.count_label.pack()
        
        # Frame de botões
        button_frame = tk.Frame(self.root, bg="#ffffff")
        button_frame.pack(pady=20)
        
        self.start_button = tk.Button(
            button_frame,
            text="▶ Iniciar / Avvia",
            command=self.toggle_timer,
            font=("Arial", 14, "bold"),
            bg="#4caf50",
            fg="white",
            width=18,
            height=2,
            relief=tk.RAISED,
            cursor="hand2"
        )
        self.start_button.grid(row=0, column=0, padx=5)
        
        self.reset_button = tk.Button(
            button_frame,
            text="⟳ Reiniciar / Riavvia",
            command=self.reset_timer,
            font=("Arial", 14, "bold"),
            bg="#ff9800",
            fg="white",
            width=18,
            height=2,
            relief=tk.RAISED,
            cursor="hand2"
        )
        self.reset_button.grid(row=0, column=1, padx=5)
        
        # Instruções de teste
        test_instructions = tk.Label(
            self.root,
            text="🧪 ROTEIRO DE TESTE:\n" +
                 "1. Pressione Iniciar e aguarde 5s → Notificação de Pomodoro Completo\n" +
                 "2. Aguarde 3s de pausa → Volta para trabalho\n" +
                 "3. Repita 4x → Após 4º pomodoro, pausa longa de 10s\n" +
                 "4. Teste atalhos: ESPAÇO (pausar), R (reset), ESC (sair)",
            font=("Arial", 9),
            bg="#e3f2fd",
            fg="#01579b",
            justify=tk.LEFT,
            padx=10,
            pady=10
        )
        test_instructions.pack(pady=10, padx=10, fill=tk.X)
        
        # Atalhos
        shortcuts_text = "⌨ Espaço: Iniciar/Pausar | R: Reiniciar | ESC: Sair"
        self.shortcuts_label = tk.Label(
            self.root,
            text=shortcuts_text,
            font=("Arial", 9),
            fg="#999999",
            bg="#ffffff"
        )
        self.shortcuts_label.pack(pady=5)
    
    def animate_gif(self):
        """Anima o GIF do tomate"""
        if self.frames:
            self.img_label.config(image=self.frames[self.current_frame])
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.root.after(100, self.animate_gif)
    
    def toggle_timer(self):
        """Inicia ou pausa o timer"""
        if not self.is_running:
            self.is_running = True
            self.start_button.config(text="⏸ Pausar / Pausa", bg="#ff5722")
            self.log_event("▶️ Timer INICIADO")
            self.timer_thread = threading.Thread(target=self.run_timer, daemon=True)
            self.timer_thread.start()
        else:
            self.is_running = False
            self.start_button.config(text="▶ Retomar / Riprendi", bg="#4caf50")
            self.log_event("⏸️ Timer PAUSADO")
    
    def reset_timer(self):
        """Reseta o timer"""
        self.is_running = False
        self.is_work_time = True
        self.time_left = self.WORK_TIME
        self.update_display()
        self.start_button.config(text="▶ Iniciar / Avvia", bg="#4caf50")
        self.log_event("🔄 Timer RESETADO")
    
    def run_timer(self):
        """Thread que executa o timer"""
        while self.is_running and self.time_left > 0:
            time.sleep(1)
            self.time_left -= 1
            self.update_display()
        
        if self.is_running and self.time_left == 0:
            self.timer_complete()
    
    def update_display(self):
        """Atualiza a exibição do timer"""
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        time_str = f"{minutes:02d}:{seconds:02d}"
        
        self.timer_label.config(text=time_str)
        
        if self.is_work_time:
            self.status_label.config(text="TRABALHO / LAVORO", fg="#d32f2f")
            self.timer_label.config(fg="#2e7d32")
        else:
            if self.pomodoro_count == 0:  # Após pausa longa
                self.status_label.config(text="PAUSA LONGA / PAUSA LUNGA", fg="#1976d2")
            else:
                self.status_label.config(text="PAUSA CURTA / PAUSA BREVE", fg="#f57c00")
            self.timer_label.config(fg="#1976d2")
    
    def timer_complete(self):
        """Callback quando o timer completa"""
        self.is_running = False
        
        if self.is_work_time:
            # Pomodoro completo
            self.pomodoro_count += 1
            self.total_pomodoros += 1
            self.log_event(f"✅ POMODORO COMPLETO! (#{self.total_pomodoros})")
            
            # Atualiza display de tomates
            self.pomodoro_display.config(text="🍅 " * self.pomodoro_count)
            self.count_label.config(text=f"Pomodoros: {self.total_pomodoros}")
            
            # Notificação
            messagebox.showinfo(
                "Pomodoro Completo! / Pomodoro Completato!",
                f"Parabéns! Você completou um pomodoro!\n"
                f"Pomodoro #{self.total_pomodoros}\n"
                f"Ciclo atual: {self.pomodoro_count}/4"
            )
            
            # Som
            try:
                import winsound
                winsound.Beep(1000, 500)
            except:
                print('\a')
            
            # Definir próximo período
            if self.pomodoro_count >= 4:
                # Pausa longa
                self.time_left = self.LONG_BREAK
                self.pomodoro_count = 0
                self.log_event("🛌 Iniciando PAUSA LONGA (10s)")
            else:
                # Pausa curta
                self.time_left = self.SHORT_BREAK
                self.log_event(f"☕ Iniciando PAUSA CURTA (3s) - {self.pomodoro_count}/4")
            
            self.is_work_time = False
        else:
            # Pausa completa
            self.log_event("🔔 Pausa COMPLETA - Voltando ao trabalho")
            messagebox.showinfo(
                "Pausa Completa! / Pausa Completata!",
                "Hora de voltar ao trabalho!\nTempo di tornare al lavoro!"
            )
            self.time_left = self.WORK_TIME
            self.is_work_time = True
        
        self.update_display()
        self.start_button.config(text="▶ Iniciar / Avvia", bg="#4caf50")
    
    def log_event(self, event):
        """Registra evento no arquivo de log"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"[{timestamp}] {event}\n"
        
        try:
            with open("pomodoro_test_log.txt", "a", encoding="utf-8") as f:
                f.write(log_line)
            print(log_line.strip())
        except Exception as e:
            print(f"Erro ao escrever log: {e}")

def main():
    root = tk.Tk()
    app = PomodoroTimerTest(root)
    root.mainloop()

if __name__ == "__main__":
    main()

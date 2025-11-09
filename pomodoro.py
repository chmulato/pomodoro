"""
Pomodoro Timer - Cronômetro Pomodoro

Aplicativo para gerenciamento de tempo usando a Técnica Pomodoro.
Ciclos de 25 minutos de trabalho, 5 minutos de pausa curta,
e 30 minutos de pausa longa após 4 pomodoros.

Funcionalidades:
- Timer visual com contagem regressiva
- Animação de tomate (GIF)
- Notificações sonoras
- Contador de pomodoros completados
- Histórico em arquivo de log
- Interface gráfica bilíngue (PT/IT)

Requisitos:
- Python 3.x
- Bibliotecas: tkinter, pillow, playsound

Autor: Christian Vladimir Uhdre Mulato
Data: Campo Largo, sábado, 09 de Novembro de 2025.
"""

import tkinter as tk
from tkinter import messagebox
import threading
import time
import datetime
import os
from PIL import Image, ImageTk

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer / Cronômetro Pomodoro")
        self.root.geometry("500x650")
        self.root.resizable(False, False)
        self.root.configure(bg="#ffffff")
        
        # Estados do timer
        self.is_running = False
        self.is_work_time = True
        self.pomodoro_count = 0
        self.total_pomodoros = 0
        
        # Tempos em segundos
        self.WORK_TIME = 25 * 60  # 25 minutos
        self.SHORT_BREAK = 5 * 60  # 5 minutos
        self.LONG_BREAK = 30 * 60  # 30 minutos
        
        self.time_left = self.WORK_TIME
        self.timer_thread = None
        
        # Garante que o arquivo de log exista
        if not os.path.exists("pomodoro_log.txt"):
            with open("pomodoro_log.txt", "w", encoding="utf-8") as f:
                f.write("=== Pomodoro Timer Log / Registro Cronômetro Pomodoro ===\n")
                f.write(f"Iniciado em / Iniziato il: {datetime.datetime.now():%Y-%m-%d %H:%M:%S}\n\n")
        
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
        self.log_event("Aplicação iniciada / Applicazione avviata")
        
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
        # Frame superior - Animação
        top_frame = tk.Frame(self.root, bg="#ffffff")
        top_frame.pack(pady=15)
        
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
        self.status_label.pack(pady=8)
        
        # Timer display
        self.timer_label = tk.Label(
            self.root,
            text="25:00",
            font=("Arial", 48, "bold"),
            fg="#2e7d32",
            bg="#ffffff"
        )
        self.timer_label.pack(pady=12)
        
        # Contador de pomodoros
        self.pomodoro_display = tk.Label(
            self.root,
            text="🍅 " * self.pomodoro_count,
            font=("Arial", 24),
            bg="#ffffff"
        )
        self.pomodoro_display.pack(pady=8)
        
        self.count_label = tk.Label(
            self.root,
            text=f"Pomodoros: {self.total_pomodoros}",
            font=("Arial", 12),
            bg="#ffffff"
        )
        self.count_label.pack()
        
        # Frame de botões
        button_frame = tk.Frame(self.root, bg="#ffffff")
        button_frame.pack(pady=25)
        
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
        
        # Informações na parte inferior
        info_text = (
            "Técnica Pomodoro / Tecnica Pomodoro:\n"
            "25 min trabalho → 5 min pausa → (4×) → 30 min pausa longa\n"
            "25 min lavoro → 5 min pausa → (4×) → 30 min pausa lunga"
        )
        self.info_label = tk.Label(
            self.root,
            text=info_text,
            font=("Arial", 10),
            fg="#666666",
            bg="#ffffff",
            justify=tk.CENTER,
            wraplength=480
        )
        self.info_label.pack(pady=15)
        
        # Atalhos
        shortcuts_text = "⌨ Espaço/Spazio: Iniciar/Avvia | R: Reiniciar/Riavvia | ESC: Sair/Esci"
        self.shortcuts_label = tk.Label(
            self.root,
            text=shortcuts_text,
            font=("Arial", 9),
            fg="#999999",
            bg="#ffffff",
            wraplength=480
        )
        self.shortcuts_label.pack(pady=5)
        
        # Background branco
        self.root.configure(bg="#ffffff")
    
    def animate_gif(self):
        """Anima o GIF do tomate"""
        if self.frames:
            self.img_label.config(image=self.frames[self.current_frame])
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.root.after(100, self.animate_gif)
    
    def toggle_timer(self):
        """Inicia ou pausa o timer"""
        if self.is_running:
            self.pause_timer()
        else:
            self.start_timer()
    
    def start_timer(self):
        """Inicia o timer"""
        self.is_running = True
        self.start_button.config(
            text="⏸ Pausar / Pausa",
            bg="#f44336"
        )
        
        if self.timer_thread is None or not self.timer_thread.is_alive():
            self.timer_thread = threading.Thread(target=self.run_timer, daemon=True)
            self.timer_thread.start()
        
        status = "trabalho / lavoro" if self.is_work_time else "pausa / pausa"
        self.log_event(f"Timer iniciado / Timer avviato - {status}")
    
    def pause_timer(self):
        """Pausa o timer"""
        self.is_running = False
        self.start_button.config(
            text="▶ Continuar / Continua",
            bg="#4caf50"
        )
        self.log_event("Timer pausado / Timer in pausa")
    
    def reset_timer(self):
        """Reinicia o timer atual"""
        was_running = self.is_running
        self.is_running = False
        
        if self.is_work_time:
            self.time_left = self.WORK_TIME
        else:
            if self.pomodoro_count >= 4:
                self.time_left = self.LONG_BREAK
            else:
                self.time_left = self.SHORT_BREAK
        
        self.update_display()
        
        if was_running:
            self.start_timer()
        else:
            self.start_button.config(
                text="▶ Iniciar / Avvia",
                bg="#4caf50"
            )
        
        self.log_event("Timer reiniciado / Timer riavviato")
    
    def run_timer(self):
        """Loop principal do timer"""
        while self.is_running and self.time_left > 0:
            time.sleep(1)
            self.time_left -= 1
            self.update_display()
        
        if self.time_left == 0 and self.is_running:
            self.timer_complete()
    
    def timer_complete(self):
        """Chamado quando o timer chega a zero"""
        self.is_running = False
        
        # Toca som de notificação
        self.play_notification()
        
        if self.is_work_time:
            # Completou um pomodoro
            self.pomodoro_count += 1
            self.total_pomodoros += 1
            self.update_pomodoro_display()
            
            self.log_event(
                f"Pomodoro completado / Pomodoro completato #{self.total_pomodoros} "
                f"({self.pomodoro_count}/4 no ciclo / nel ciclo)"
            )
            
            # Determina o tipo de pausa
            if self.pomodoro_count >= 4:
                self.time_left = self.LONG_BREAK
                self.show_notification(
                    "Pausa Longa! / Pausa Lunga!",
                    "Você completou 4 pomodoros!\nDescanse por 30 minutos.\n\n"
                    "Hai completato 4 pomodori!\nRiposa per 30 minuti."
                )
                self.log_event("Iniciando pausa longa / Iniziando pausa lunga (30 min)")
                self.pomodoro_count = 0
            else:
                self.time_left = self.SHORT_BREAK
                self.show_notification(
                    "Pausa Curta! / Pausa Breve!",
                    f"Descanse por 5 minutos.\nPomodoros: {self.pomodoro_count}/4\n\n"
                    f"Riposa per 5 minuti.\nPomodori: {self.pomodoro_count}/4"
                )
                self.log_event("Iniciando pausa curta / Iniziando pausa breve (5 min)")
            
            self.is_work_time = False
            
        else:
            # Completou uma pausa
            self.time_left = self.WORK_TIME
            self.show_notification(
                "De Volta ao Trabalho! / Torna al Lavoro!",
                "Hora de focar!\nNovo pomodoro de 25 minutos.\n\n"
                "Tempo di concentrazione!\nNuovo pomodoro di 25 minuti."
            )
            self.log_event("Pausa terminada, novo pomodoro / Pausa terminata, nuovo pomodoro")
            self.is_work_time = True
        
        self.update_display()
        self.update_pomodoro_display()
        self.start_button.config(
            text="▶ Iniciar / Avvia",
            bg="#4caf50"
        )
    
    def update_display(self):
        """Atualiza o display do timer"""
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        time_str = f"{minutes:02d}:{seconds:02d}"
        
        self.timer_label.config(text=time_str)
        
        # Atualiza status e cor
        if self.is_work_time:
            self.status_label.config(
                text="TRABALHO / LAVORO",
                fg="#d32f2f"
            )
            self.timer_label.config(fg="#2e7d32")
        else:
            if self.pomodoro_count >= 4 or self.time_left > self.SHORT_BREAK:
                self.status_label.config(
                    text="PAUSA LONGA / PAUSA LUNGA",
                    fg="#1976d2"
                )
            else:
                self.status_label.config(
                    text="PAUSA CURTA / PAUSA BREVE",
                    fg="#f57c00"
                )
            self.timer_label.config(fg="#0277bd")
    
    def update_pomodoro_display(self):
        """Atualiza o display de pomodoros completados"""
        tomatoes = "🍅 " * self.pomodoro_count
        if len(tomatoes) == 0:
            tomatoes = "⚪ ⚪ ⚪ ⚪"
        self.pomodoro_display.config(text=tomatoes)
        self.count_label.config(text=f"Pomodoros: {self.total_pomodoros}")
    
    def play_notification(self):
        """Toca som de notificação"""
        try:
            # Tenta tocar som usando diferentes métodos
            if os.name == 'nt':  # Windows
                import winsound
                winsound.MessageBeep(winsound.MB_ICONASTERISK)
            else:  # Linux/Mac
                print('\a')  # System beep
        except Exception as e:
            print(f"Não foi possível tocar o som: {e}")
    
    def show_notification(self, title, message):
        """Exibe notificação pop-up"""
        messagebox.showinfo(title, message)
    
    def log_event(self, mensagem):
        """Registra evento no arquivo de log"""
        log_line = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S} - {mensagem}"
        try:
            with open("pomodoro_log.txt", "a", encoding="utf-8") as f:
                f.write(log_line + "\n")
        except Exception as e:
            print(f"Erro ao escrever log: {e}")


def main():
    """Função principal"""
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()


if __name__ == "__main__":
    main()

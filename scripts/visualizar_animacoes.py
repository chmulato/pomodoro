#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visualizador de Animações do Pomodoro
Mostra as 4 animações lado a lado para comparação
"""

import tkinter as tk
from PIL import Image, ImageTk
import os

class AnimationViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("🍅 Comparação de Animações Pomodoro - MoviePy")
        self.root.configure(bg="#f5f5f5")
        
        # Carregar todas as animações
        self.animations = {
            "Trabalho\n(25 min)": self.load_gif("img/pomodoro.gif"),
            "Pausa Curta\n(5 min)": self.load_gif("img/pomodoro_break.gif"),
            "Pausa Longa\n(30 min)": self.load_gif("img/pomodoro_longbreak.gif"),
            "ESPECIAL\n(Bônus)": self.load_gif("img/pomodoro_special.gif")
        }
        
        self.setup_ui()
        self.animate_all()
    
    def load_gif(self, path):
        """Carrega frames de um GIF"""
        frames = []
        try:
            gif = Image.open(path)
            for frame_num in range(0, getattr(gif, "n_frames", 1)):
                gif.seek(frame_num)
                frame = gif.copy().resize((120, 120), Image.Resampling.LANCZOS)
                frames.append(ImageTk.PhotoImage(frame))
            print(f"✓ {os.path.basename(path)} carregado ({len(frames)} frames)")
        except Exception as e:
            print(f"✗ Erro ao carregar {path}: {e}")
        return frames
    
    def setup_ui(self):
        """Configura a interface"""
        # Título
        title = tk.Label(
            self.root,
            text="🎬 Animações MoviePy - Pomodoro Timer",
            font=("Arial", 18, "bold"),
            bg="#f5f5f5",
            fg="#d32f2f"
        )
        title.pack(pady=15)
        
        subtitle = tk.Label(
            self.root,
            text="Animações criadas com easing, rotação e efeitos avançados",
            font=("Arial", 11),
            bg="#f5f5f5",
            fg="#666"
        )
        subtitle.pack(pady=5)
        
        # Frame para as animações
        anim_frame = tk.Frame(self.root, bg="#f5f5f5")
        anim_frame.pack(pady=20)
        
        self.labels = []
        self.frame_counters = []
        
        col = 0
        for name, frames in self.animations.items():
            # Container para cada animação
            container = tk.Frame(anim_frame, bg="#ffffff", relief=tk.RAISED, bd=2)
            container.grid(row=0, column=col, padx=10, pady=10)
            
            # Nome
            name_label = tk.Label(
                container,
                text=name,
                font=("Arial", 12, "bold"),
                bg="#ffffff",
                fg="#333"
            )
            name_label.pack(pady=5)
            
            # GIF
            img_label = tk.Label(container, bg="#ffffff")
            img_label.pack(padx=10, pady=10)
            
            # Descrição
            descriptions = [
                "Pulsação + Rotação ±8°",
                "Movimento Pendular ±15°",
                "Respiração + Z's Flutuantes",
                "Zoom 0.8-1.4x + Rotação 360°"
            ]
            desc_label = tk.Label(
                container,
                text=descriptions[col],
                font=("Arial", 9),
                bg="#ffffff",
                fg="#666"
            )
            desc_label.pack(pady=5)
            
            self.labels.append(img_label)
            self.frame_counters.append(0)
            
            col += 1
        
        # Informações técnicas
        info = tk.Label(
            self.root,
            text="✨ Criadas com MoviePy 2.x | Easing Functions | Interpolação LANCZOS/BICUBIC",
            font=("Arial", 9),
            bg="#f5f5f5",
            fg="#888"
        )
        info.pack(pady=10)
        
        # Botão fechar
        close_btn = tk.Button(
            self.root,
            text="✕ Fechar",
            command=self.root.quit,
            font=("Arial", 10, "bold"),
            bg="#d32f2f",
            fg="white",
            cursor="hand2",
            relief=tk.FLAT
        )
        close_btn.pack(pady=10)
    
    def animate_all(self):
        """Anima todos os GIFs simultaneamente"""
        idx = 0
        for name, frames in self.animations.items():
            if frames:
                self.frame_counters[idx] = (self.frame_counters[idx] + 1) % len(frames)
                self.labels[idx].config(image=frames[self.frame_counters[idx]])
            idx += 1
        
        # Atualiza a cada 80ms para animação suave
        self.root.after(80, self.animate_all)

def main():
    root = tk.Tk()
    app = AnimationViewer(root)
    root.mainloop()

if __name__ == "__main__":
    main()

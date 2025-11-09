#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Assets para Pomodoro Timer - Versão MoviePy
Cria GIFs animados avançados usando MoviePy para efeitos mais suaves
"""

from PIL import Image, ImageDraw, ImageFont
import numpy as np
try:
    # MoviePy 2.x (novo)
    from moviepy import VideoClip, CompositeVideoClip, ImageClip
except ImportError:
    # MoviePy 1.x (antigo)
    from moviepy.editor import VideoClip, CompositeVideoClip, ImageClip
import os
import sys

def criar_tomate_pil(tamanho, escala=1.0, brilho=1.0, cor_fundo=(255, 255, 255, 0)):
    """
    Cria uma imagem PIL de tomate com tamanho e escala ajustáveis
    
    Args:
        tamanho: tupla (largura, altura)
        escala: fator de escala do tomate (1.0 = normal)
        brilho: fator de brilho da cor (1.0 = normal)
        cor_fundo: cor RGBA do fundo
    """
    img = Image.new('RGBA', tamanho, cor_fundo)
    draw = ImageDraw.Draw(img)
    
    w, h = tamanho
    cx, cy = w // 2, h // 2
    
    # Tamanho base do tomate
    raio = int(min(w, h) * 0.35 * escala)
    
    # Cores do tomate (ajustadas por brilho)
    vermelho = tuple(int(c * brilho) for c in (255, 99, 71))  # Tomato red
    vermelho_escuro = tuple(int(c * brilho * 0.8) for c in (220, 20, 60))  # Crimson
    verde = tuple(int(c * brilho) for c in (34, 139, 34))  # Forest green
    verde_escuro = tuple(int(c * brilho * 0.7) for c in (0, 100, 0))  # Dark green
    
    # Sombra do tomate
    sombra_offset = int(raio * 0.1)
    draw.ellipse(
        [cx - raio + sombra_offset, cy - raio + sombra_offset * 2,
         cx + raio + sombra_offset, cy + raio + sombra_offset * 2],
        fill=(0, 0, 0, 50)
    )
    
    # Corpo do tomate (círculo principal)
    draw.ellipse(
        [cx - raio, cy - raio, cx + raio, cy + raio],
        fill=vermelho,
        outline=vermelho_escuro,
        width=3
    )
    
    # Brilho no tomate
    brilho_raio = int(raio * 0.3)
    brilho_x = cx - int(raio * 0.3)
    brilho_y = cy - int(raio * 0.3)
    draw.ellipse(
        [brilho_x - brilho_raio, brilho_y - brilho_raio,
         brilho_x + brilho_raio, brilho_y + brilho_raio],
        fill=(255, 255, 255, 100)
    )
    
    # Caule (folhas em cima)
    caule_h = int(raio * 0.4)
    caule_y = cy - raio - caule_h // 2
    
    # Folha esquerda
    folha_esq = [
        (cx - int(raio * 0.3), caule_y),
        (cx - int(raio * 0.5), caule_y - caule_h),
        (cx - int(raio * 0.1), caule_y - int(caule_h * 0.5))
    ]
    draw.polygon(folha_esq, fill=verde, outline=verde_escuro)
    
    # Folha direita
    folha_dir = [
        (cx + int(raio * 0.3), caule_y),
        (cx + int(raio * 0.5), caule_y - caule_h),
        (cx + int(raio * 0.1), caule_y - int(caule_h * 0.5))
    ]
    draw.polygon(folha_dir, fill=verde, outline=verde_escuro)
    
    # Folha central
    folha_centro = [
        (cx, caule_y),
        (cx - int(raio * 0.1), caule_y - int(caule_h * 1.2)),
        (cx + int(raio * 0.1), caule_y - int(caule_h * 1.2))
    ]
    draw.polygon(folha_centro, fill=verde, outline=verde_escuro)
    
    return img

def easing_in_out_cubic(t):
    """Função de easing suave (cubic ease-in-out)"""
    if t < 0.5:
        return 4 * t * t * t
    else:
        return 1 - pow(-2 * t + 2, 3) / 2

def easing_bounce(t):
    """Efeito de bounce suave"""
    return abs(np.sin(t * np.pi))

def gerar_pomodoro_trabalho_moviepy():
    """
    Gera GIF animado para período de trabalho (25 min)
    Tomate pulsando com rotação sutil e easing suave
    """
    print("🍅 Gerando pomodoro.gif com MoviePy (trabalho - 25min)...")
    
    tamanho = (150, 150)
    duracao = 2.0  # 2 segundos de animação
    fps = 15
    output_path = os.path.join('img', 'pomodoro.gif')
    
    # Criar tomate base
    tomate_base = criar_tomate_pil(tamanho, escala=1.0, brilho=1.0)
    tomate_array = np.array(tomate_base)
    
    def make_frame(t):
        """Função que cria cada frame baseado no tempo"""
        # Calcular progresso com loop
        progress = (t % duracao) / duracao
        
        # Pulsação com easing suave
        pulse = 1.0 + 0.15 * easing_bounce(progress)
        
        # Rotação sutil (balança de -5 a +5 graus)
        angle = 8 * np.sin(progress * 2 * np.pi)
        
        # Criar novo frame
        img = Image.fromarray(tomate_array)
        
        # Aplicar escala
        new_size = (int(tamanho[0] * pulse), int(tamanho[1] * pulse))
        img_resized = img.resize(new_size, Image.Resampling.LANCZOS)
        
        # Aplicar rotação
        img_rotated = img_resized.rotate(angle, expand=False, resample=Image.Resampling.BICUBIC)
        
        # Centralizar na canvas
        canvas = Image.new('RGBA', tamanho, (255, 255, 255, 0))
        offset_x = (tamanho[0] - img_rotated.width) // 2
        offset_y = (tamanho[1] - img_rotated.height) // 2
        canvas.paste(img_rotated, (offset_x, offset_y), img_rotated)
        
        return np.array(canvas)
    
    # Criar clip de vídeo
    clip = VideoClip(make_frame, duration=duracao)
    
    # Salvar como GIF (MoviePy 2.x - parâmetros simplificados)
    clip.write_gif(output_path, fps=fps)
    
    print("✅ pomodoro.gif criado com MoviePy (animação fluida)")

def gerar_pomodoro_pausa_curta_moviepy():
    """
    Gera GIF animado para pausa curta (5 min)
    Tomate balançando suavemente como um pêndulo
    """
    print("☕ Gerando pomodoro_break.gif com MoviePy (pausa curta - 5min)...")
    
    tamanho = (150, 150)
    duracao = 2.5  # 2.5 segundos
    fps = 15
    output_path = os.path.join('img', 'pomodoro_break.gif')
    
    # Criar tomate mais escuro para pausa
    tomate_base = criar_tomate_pil(tamanho, escala=1.0, brilho=0.85)
    tomate_array = np.array(tomate_base)
    
    def make_frame(t):
        """Frame com movimento pendular"""
        progress = (t % duracao) / duracao
        
        # Movimento pendular suave
        angle = 15 * np.sin(progress * 2 * np.pi)
        
        # Escala sutil
        pulse = 0.95 + 0.05 * easing_in_out_cubic(abs(np.sin(progress * np.pi)))
        
        img = Image.fromarray(tomate_array)
        
        # Aplicar escala
        new_size = (int(tamanho[0] * pulse), int(tamanho[1] * pulse))
        img_resized = img.resize(new_size, Image.Resampling.LANCZOS)
        
        # Rotação
        img_rotated = img_resized.rotate(angle, expand=False, resample=Image.Resampling.BICUBIC)
        
        # Centralizar
        canvas = Image.new('RGBA', tamanho, (255, 255, 255, 0))
        offset_x = (tamanho[0] - img_rotated.width) // 2
        offset_y = (tamanho[1] - img_rotated.height) // 2
        canvas.paste(img_rotated, (offset_x, offset_y), img_rotated)
        
        return np.array(canvas)
    
    clip = VideoClip(make_frame, duration=duracao)
    clip.write_gif(output_path, fps=fps)
    
    print("✅ pomodoro_break.gif criado com MoviePy (movimento pendular)")

def gerar_pomodoro_pausa_longa_moviepy():
    """
    Gera GIF animado para pausa longa (30 min)
    Tomate dormindo com respiração lenta e Z's animados
    """
    print("😴 Gerando pomodoro_longbreak.gif com MoviePy (pausa longa - 30min)...")
    
    tamanho = (150, 150)
    duracao = 3.0  # 3 segundos (mais lento)
    fps = 12
    output_path = os.path.join('img', 'pomodoro_longbreak.gif')
    
    # Criar tomate bem escuro
    tomate_base = criar_tomate_pil(tamanho, escala=1.0, brilho=0.7)
    tomate_array = np.array(tomate_base)
    
    def make_frame(t):
        """Frame com respiração lenta e Z's"""
        progress = (t % duracao) / duracao
        
        # Respiração muito lenta
        breath = 0.92 + 0.06 * easing_in_out_cubic(abs(np.sin(progress * np.pi)))
        
        img = Image.fromarray(tomate_array)
        
        # Aplicar respiração
        new_size = (int(tamanho[0] * breath), int(tamanho[1] * breath))
        img_resized = img.resize(new_size, Image.Resampling.LANCZOS)
        
        # Centralizar
        canvas = Image.new('RGBA', tamanho, (255, 255, 255, 0))
        offset_x = (tamanho[0] - img_resized.width) // 2
        offset_y = (tamanho[1] - img_resized.height) // 2
        canvas.paste(img_resized, (offset_x, offset_y), img_resized)
        
        # Adicionar Z's animados
        draw = ImageDraw.Draw(canvas)
        try:
            font = ImageFont.truetype("arial.ttf", 24)
        except:
            font = ImageFont.load_default()
        
        # Z's flutuando para cima
        z_offset = int(15 * progress)
        alpha_base = int(200 * (1 - progress))
        
        # Três Z's com delays
        if progress < 0.8:
            z1_alpha = int(alpha_base * (1 - progress / 0.8))
            draw.text((100, 25 - z_offset), "Z", fill=(80, 80, 80, z1_alpha), font=font)
        
        if progress < 0.6:
            z2_alpha = int(alpha_base * 0.8 * (1 - progress / 0.6))
            draw.text((110, 35 - int(z_offset * 0.7)), "z", fill=(100, 100, 100, z2_alpha), font=font)
        
        if progress < 0.4:
            z3_alpha = int(alpha_base * 0.6 * (1 - progress / 0.4))
            draw.text((115, 45 - int(z_offset * 0.5)), "z", fill=(120, 120, 120, z3_alpha), font=font)
        
        return np.array(canvas)
    
    clip = VideoClip(make_frame, duration=duracao)
    clip.write_gif(output_path, fps=fps)
    
    print("✅ pomodoro_longbreak.gif criado com MoviePy (respiração lenta)")

def gerar_pomodoro_especial_moviepy():
    """
    BÔNUS: Gera GIF animado especial com efeitos avançados
    Tomate com zoom dramático e rotação completa
    """
    print("✨ Gerando pomodoro_special.gif com MoviePy (animação especial)...")
    
    tamanho = (150, 150)
    duracao = 3.0
    fps = 20
    output_path = os.path.join('img', 'pomodoro_special.gif')
    
    tomate_base = criar_tomate_pil(tamanho, escala=1.0, brilho=1.0)
    tomate_array = np.array(tomate_base)
    
    def make_frame(t):
        """Frame com zoom dramático e rotação completa"""
        progress = (t % duracao) / duracao
        
        # Zoom in e out com easing
        if progress < 0.5:
            zoom = 0.8 + 0.6 * easing_in_out_cubic(progress * 2)
        else:
            zoom = 1.4 - 0.6 * easing_in_out_cubic((progress - 0.5) * 2)
        
        # Rotação completa de 360 graus
        angle = 360 * progress
        
        # Brilho pulsante
        brightness = 0.9 + 0.2 * abs(np.sin(progress * 4 * np.pi))
        
        img = Image.fromarray(tomate_array)
        
        # Aplicar brilho
        enhancer = Image.new('RGBA', img.size, (255, 255, 255, 0))
        overlay = Image.new('RGBA', img.size, (255, 255, 255, int(30 * (brightness - 0.9))))
        img = Image.alpha_composite(img, overlay)
        
        # Aplicar zoom
        new_size = (int(tamanho[0] * zoom), int(tamanho[1] * zoom))
        img_resized = img.resize(new_size, Image.Resampling.LANCZOS)
        
        # Rotação
        img_rotated = img_resized.rotate(angle, expand=False, resample=Image.Resampling.BICUBIC)
        
        # Centralizar
        canvas = Image.new('RGBA', tamanho, (255, 255, 255, 0))
        offset_x = (tamanho[0] - img_rotated.width) // 2
        offset_y = (tamanho[1] - img_rotated.height) // 2
        canvas.paste(img_rotated, (offset_x, offset_y), img_rotated)
        
        return np.array(canvas)
    
    clip = VideoClip(make_frame, duration=duracao)
    clip.write_gif(output_path, fps=fps)
    
    print("✅ pomodoro_special.gif criado (animação especial!)")

def gerar_icone():
    """Gera ícone .ico para a aplicação"""
    print("🖼️  Gerando pomodoro.ico...")
    
    tamanhos = [256, 128, 64, 48, 32, 16]
    images = []
    output_path = os.path.join('img', 'pomodoro.ico')
    
    for tam in tamanhos:
        img = criar_tomate_pil((tam, tam), escala=1.0, brilho=1.0)
        images.append(img)
    
    images[0].save(
        output_path,
        format='ICO',
        sizes=[(t, t) for t in tamanhos]
    )
    print("✅ pomodoro.ico criado (multi-resolução)")

def main():
    """Função principal"""
    print("=" * 60)
    print("🍅 GERADOR DE ASSETS - POMODORO TIMER (MoviePy Edition)")
    print("=" * 60)
    print()
    
    try:
        # Verificar se MoviePy está instalado
        try:
            import moviepy
            print("✓ MoviePy detectado")
        except ImportError:
            print("❌ MoviePy não encontrado!")
            print("   Instale com: pip install moviepy")
            return 1
        
        # Criar pasta img se não existir
        os.makedirs('img', exist_ok=True)
        print("✓ Pasta img/ verificada")
        
        print()
        
        # Gerar todos os assets
        gerar_pomodoro_trabalho_moviepy()
        gerar_pomodoro_pausa_curta_moviepy()
        gerar_pomodoro_pausa_longa_moviepy()
        gerar_pomodoro_especial_moviepy()
        gerar_icone()
        
        print()
        print("=" * 60)
        print("✅ TODOS OS ASSETS FORAM GERADOS COM SUCESSO!")
        print("=" * 60)
        print()
        print("Arquivos criados em img/:")
        print("  📄 img/pomodoro.gif          - Animação trabalho (pulsação + rotação)")
        print("  📄 img/pomodoro_break.gif    - Animação pausa curta (pendular)")
        print("  📄 img/pomodoro_longbreak.gif - Animação pausa longa (respiração + Z's)")
        print("  📄 img/pomodoro_special.gif  - Animação especial (zoom + rotação 360°)")
        print("  📄 img/pomodoro.ico          - Ícone da aplicação")
        print()
        print("🎬 Animações criadas com MoviePy para qualidade cinematográfica!")
        print()
        
        return 0
        
    except Exception as e:
        print()
        print("❌ ERRO ao gerar assets:")
        print(f"   {str(e)}")
        print()
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())

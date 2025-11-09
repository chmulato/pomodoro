#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Assets para Pomodoro Timer
Cria GIFs animados e ícone para a aplicação
"""

from PIL import Image, ImageDraw, ImageFont
import os
import sys

def criar_tomate_frame(tamanho, escala=1.0, brilho=1.0, cor_fundo=(255, 255, 255, 0)):
    """
    Cria um frame de tomate com tamanho e escala ajustáveis
    
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

def gerar_pomodoro_trabalho():
    """
    Gera GIF animado para período de trabalho (25 min)
    Tomate pulsando suavemente
    """
    print("🍅 Gerando pomodoro.gif (trabalho - 25min)...")
    
    frames = []
    tamanho = (150, 150)
    num_frames = 12
    
    for i in range(num_frames):
        # Efeito de pulsação suave
        progresso = i / num_frames
        escala = 1.0 + 0.1 * abs(2 * progresso - 1)  # Pulsa entre 1.0 e 1.1
        brilho = 0.95 + 0.05 * abs(2 * progresso - 1)  # Brilho sutil
        
        frame = criar_tomate_frame(tamanho, escala=escala, brilho=brilho)
        frames.append(frame)
    
    frames[0].save(
        'pomodoro.gif',
        save_all=True,
        append_images=frames[1:],
        duration=100,  # 100ms por frame = animação suave
        loop=0,
        optimize=True
    )
    print("✅ pomodoro.gif criado (animação de trabalho)")

def gerar_pomodoro_pausa_curta():
    """
    Gera GIF animado para pausa curta (5 min)
    Tomate balançando suavemente
    """
    print("☕ Gerando pomodoro_break.gif (pausa curta - 5min)...")
    
    frames = []
    tamanho = (150, 150)
    num_frames = 8
    
    for i in range(num_frames):
        # Efeito de balanço
        progresso = i / num_frames
        escala = 0.95 + 0.05 * abs(2 * progresso - 1)
        brilho = 0.85  # Mais escuro para indicar descanso
        
        frame = criar_tomate_frame(tamanho, escala=escala, brilho=brilho)
        frames.append(frame)
    
    frames[0].save(
        'pomodoro_break.gif',
        save_all=True,
        append_images=frames[1:],
        duration=150,  # Mais lento durante descanso
        loop=0,
        optimize=True
    )
    print("✅ pomodoro_break.gif criado (animação de pausa)")

def gerar_pomodoro_pausa_longa():
    """
    Gera GIF animado para pausa longa (30 min após 4 tomates)
    Tomate dormindo/descansando
    """
    print("😴 Gerando pomodoro_longbreak.gif (pausa longa - 30min)...")
    
    frames = []
    tamanho = (150, 150)
    num_frames = 6
    
    for i in range(num_frames):
        # Respiração lenta
        progresso = i / num_frames
        escala = 0.9 + 0.05 * abs(2 * progresso - 1)
        brilho = 0.75  # Bem mais escuro
        
        frame = criar_tomate_frame(tamanho, escala=escala, brilho=brilho)
        
        # Adicionar "Zzz" para indicar sono
        draw = ImageDraw.Draw(frame)
        try:
            # Tentar usar fonte padrão
            font = ImageFont.truetype("arial.ttf", 20)
        except:
            font = ImageFont.load_default()
        
        # Desenhar Zzz animado
        offset_z = int(5 * (1 - abs(2 * progresso - 1)))
        draw.text((100, 20 - offset_z), "Z", fill=(100, 100, 100, 200), font=font)
        draw.text((110, 30 - offset_z), "z", fill=(120, 120, 120, 180), font=font)
        draw.text((115, 40 - offset_z), "z", fill=(140, 140, 140, 160), font=font)
        
        frames.append(frame)
    
    frames[0].save(
        'pomodoro_longbreak.gif',
        save_all=True,
        append_images=frames[1:],
        duration=200,  # Ainda mais lento
        loop=0,
        optimize=True
    )
    print("✅ pomodoro_longbreak.gif criado (animação de pausa longa)")

def gerar_icone():
    """
    Gera ícone .ico para a aplicação
    """
    print("🖼️  Gerando pomodoro.ico...")
    
    # Criar tomate em alta resolução
    tamanhos = [256, 128, 64, 48, 32, 16]
    images = []
    
    for tam in tamanhos:
        img = criar_tomate_frame((tam, tam), escala=1.0, brilho=1.0)
        images.append(img)
    
    # Salvar multi-resolução ICO
    images[0].save(
        'pomodoro.ico',
        format='ICO',
        sizes=[(t, t) for t in tamanhos]
    )
    print("✅ pomodoro.ico criado (multi-resolução)")

def gerar_preview():
    """
    Gera imagem preview PNG com os 4 tomates
    """
    print("📸 Gerando preview.png (4 tomates colecionados)...")
    
    # Canvas maior
    img = Image.new('RGBA', (400, 120), (255, 255, 255, 255))
    
    # 4 tomates lado a lado
    for i in range(4):
        tomate = criar_tomate_frame((100, 100), escala=0.9, brilho=1.0, cor_fundo=(255, 255, 255, 0))
        img.paste(tomate, (i * 100, 10), tomate)
    
    # Adicionar texto
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except:
        font = ImageFont.load_default()
    
    draw.text((10, 90), "4 Pomodoros = Pausa Longa (30 min)", fill=(50, 50, 50), font=font)
    
    img.save('preview.png', optimize=True)
    print("✅ preview.png criado")

def main():
    """Função principal"""
    print("=" * 60)
    print("🍅 GERADOR DE ASSETS - POMODORO TIMER")
    print("=" * 60)
    print()
    
    try:
        # Gerar todos os assets
        gerar_pomodoro_trabalho()
        gerar_pomodoro_pausa_curta()
        gerar_pomodoro_pausa_longa()
        gerar_icone()
        gerar_preview()
        
        print()
        print("=" * 60)
        print("✅ TODOS OS ASSETS FORAM GERADOS COM SUCESSO!")
        print("=" * 60)
        print()
        print("Arquivos criados:")
        print("  📄 pomodoro.gif          - Animação trabalho (25 min)")
        print("  📄 pomodoro_break.gif    - Animação pausa curta (5 min)")
        print("  📄 pomodoro_longbreak.gif - Animação pausa longa (30 min)")
        print("  📄 pomodoro.ico          - Ícone da aplicação")
        print("  📄 preview.png           - Preview dos 4 tomates")
        print()
        print("🚀 Agora você pode executar: python pomodoro.py")
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

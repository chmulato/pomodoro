# 🎬 Melhorias de Animação com MoviePy

## 📦 O que foi melhorado?

### **1. Animações mais fluidas com easing**

- **Easing cubic in-out**: Transições suaves e naturais
- **Bounce effect**: Pulsação realista
- **Controle temporal preciso**: FPS e duração configuráveis

### **2. Efeitos avançados implementados**

#### **🍅 pomodoro.gif (Trabalho - 25min)**

- Pulsação suave com bounce easing (15% de variação)
- Rotação sutil ±8° para dar vida
- 15 FPS para animação fluida
- Loop de 2 segundos

#### **☕ pomodoro_break.gif (Pausa Curta - 5min)**

- Movimento pendular realista ±15°
- Escala sutil (95-100%)
- Easing cubic para movimento natural
- Tom mais escuro (85% brilho)

#### **😴 pomodoro_longbreak.gif (Pausa Longa - 30min)**

- Respiração lenta e profunda
- Z's animados que flutuam para cima
- Fade out gradual nos Z's
- Escala 92-98% para respiração sutil
- Tom bem escuro (70% brilho)

#### **✨ pomodoro_special.gif (BÔNUS - Animação Especial)**

- Zoom dramático de 0.8x a 1.4x
- Rotação completa de 360°
- Efeito de brilho pulsante
- 20 FPS para máxima suavidade

### **3. Vantagens sobre PIL puro**

| Aspecto | PIL (Antigo) | MoviePy (Novo) |
|---------|--------------|----------------|
| **Easing** | Linear | Cubic, Bounce, Custom |
| **Rotação** | Não | Sim, suave |
| **Controle temporal** | Frame-by-frame | Baseado em tempo (t) |
| **Efeitos** | Básicos | Avançados |
| **Qualidade** | Boa | Excelente |
| **Flexibilidade** | Limitada | Alta |

## 🚀 Como usar

### **Instalação**

```bash
pip install -r requirements_moviepy.txt
```

### **Gerar assets**

```bash
python scripts/gerar_assets_moviepy.py
```

## 📊 Especificações técnicas

### **Funções de Easing**

```python
# Cubic ease-in-out (transições suaves)
easing_in_out_cubic(t) = 4t³ (se t < 0.5)
                       = 1 - (-2t + 2)³/2 (se t ≥ 0.5)

# Bounce (pulsação natural)
easing_bounce(t) = |sin(t × π)|
```

### **Parâmetros de animação**

- **Trabalho**: 2.0s loop, 15 FPS, pulsação 1.0-1.15x, rotação ±8°
- **Pausa Curta**: 2.5s loop, 15 FPS, escala 0.95-1.0x, rotação ±15°
- **Pausa Longa**: 3.0s loop, 12 FPS, escala 0.92-0.98x
- **Especial**: 3.0s loop, 20 FPS, zoom 0.8-1.4x, rotação 360°

## 🎨 Personalizações possíveis

### **Alterar velocidade**

```python
duracao = 1.5  # Mais rápido
duracao = 4.0  # Mais lento
```

### **Alterar intensidade**

```python
pulse = 1.0 + 0.3 * easing_bounce(progress)  # Pulsação mais intensa
angle = 20 * np.sin(progress * 2 * np.pi)     # Rotação maior
```

### **Alterar FPS**

```python
fps = 24  # Mais suave (arquivo maior)
fps = 10  # Menos suave (arquivo menor)
```

## 💡 Ideias para futuras melhorias

1. **Partículas**: Adicionar estrelas/brilhos ao redor do tomate
2. **Sombra dinâmica**: Sombra que acompanha o movimento
3. **Deformação**: Tomate que "estica" ao pulsar
4. **Trilha de movimento**: Rastro visual do movimento
5. **Cores dinâmicas**: Mudança gradual de tonalidade
6. **Física realista**: Simular gravidade e inércia

## 📈 Comparação de tamanho de arquivo

Os GIFs do MoviePy podem ser maiores devido à qualidade superior:

- PIL: ~50-100 KB por GIF
- MoviePy: ~100-200 KB por GIF (qualidade superior)

Para reduzir tamanho sem perder qualidade:

```python
clip.write_gif('file.gif', fps=12, opt='nq', fuzz=2)  # Mais compressão
```

## 🔧 Troubleshooting

### Erro: "MoviePy not found"

```bash
pip install moviepy
```

### Erro: "ImageMagick not found"

MoviePy usa ImageMagick para GIFs. Instale:

- **Windows**: [Download ImageMagick](https://imagemagick.org/script/download.php#windows)
- **Linux**: `sudo apt-get install imagemagick`
- **Mac**: `brew install imagemagick`

Ou configure MoviePy para usar Pillow:

```python
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": "auto-detect"})
```

## 🎯 Conclusão

O MoviePy oferece controle total sobre a animação, permitindo criar GIFs com qualidade cinematográfica. As animações são mais suaves, naturais e profissionais, melhorando significativamente a experiência do usuário no Pomodoro Timer.

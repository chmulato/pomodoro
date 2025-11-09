#!/usr/bin/env node
/**
 * Gerador de Bandeiras - Brasil e Itália
 * Cria imagens SVG/PNG das bandeiras para uso no README
 */

const { createCanvas } = require('canvas');
const fs = require('fs');
const path = require('path');

// Criar diretório img se não existir
const imgDir = path.join(__dirname, 'img');
if (!fs.existsSync(imgDir)) {
    fs.mkdirSync(imgDir, { recursive: true });
}

/**
 * Gera a bandeira do Brasil
 * Verde, Amarelo, Azul e Branco com estrelas
 */
function gerarBandeiraBrasil() {
    console.log('🇧🇷 Gerando bandeira do Brasil...');
    
    const width = 300;
    const height = 210;
    const canvas = createCanvas(width, height);
    const ctx = canvas.getContext('2d');
    
    // Fundo verde
    ctx.fillStyle = '#009c3b'; // Verde brasileiro
    ctx.fillRect(0, 0, width, height);
    
    // Losango amarelo
    ctx.fillStyle = '#ffdf00'; // Amarelo ouro
    ctx.beginPath();
    ctx.moveTo(width / 2, 15);           // Topo
    ctx.lineTo(width - 15, height / 2);  // Direita
    ctx.lineTo(width / 2, height - 15);  // Base
    ctx.lineTo(15, height / 2);          // Esquerda
    ctx.closePath();
    ctx.fill();
    
    // Círculo azul
    const centerX = width / 2;
    const centerY = height / 2;
    const radius = 45;
    
    ctx.fillStyle = '#002776'; // Azul brasileiro
    ctx.beginPath();
    ctx.arc(centerX, centerY, radius, 0, 2 * Math.PI);
    ctx.fill();
    
    // Faixa branca "Ordem e Progresso"
    ctx.strokeStyle = '#ffffff';
    ctx.lineWidth = 8;
    ctx.beginPath();
    ctx.arc(centerX, centerY, radius - 5, -0.3, Math.PI + 0.3);
    ctx.stroke();
    
    // Estrelas (simplificadas)
    ctx.fillStyle = '#ffffff';
    const starPositions = [
        { x: centerX - 20, y: centerY - 15 },
        { x: centerX, y: centerY - 25 },
        { x: centerX + 20, y: centerY - 15 },
        { x: centerX - 15, y: centerY + 10 },
        { x: centerX + 15, y: centerY + 10 }
    ];
    
    starPositions.forEach(pos => {
        drawStar(ctx, pos.x, pos.y, 3, 2, 1.5);
    });
    
    // Salvar PNG
    const buffer = canvas.toBuffer('image/png');
    fs.writeFileSync(path.join(imgDir, 'flag_brazil.png'), buffer);
    console.log('✅ Bandeira do Brasil salva: img/flag_brazil.png');
}

/**
 * Gera a bandeira da Itália
 * Verde, Branco e Vermelho (vertical)
 */
function gerarBandeiraItalia() {
    console.log('🇮🇹 Gerando bandeira da Itália...');
    
    const width = 300;
    const height = 200;
    const canvas = createCanvas(width, height);
    const ctx = canvas.getContext('2d');
    
    const stripeWidth = width / 3;
    
    // Faixa verde (esquerda)
    ctx.fillStyle = '#009246'; // Verde italiano
    ctx.fillRect(0, 0, stripeWidth, height);
    
    // Faixa branca (centro)
    ctx.fillStyle = '#ffffff';
    ctx.fillRect(stripeWidth, 0, stripeWidth, height);
    
    // Faixa vermelha (direita)
    ctx.fillStyle = '#ce2b37'; // Vermelho italiano
    ctx.fillRect(stripeWidth * 2, 0, stripeWidth, height);
    
    // Salvar PNG
    const buffer = canvas.toBuffer('image/png');
    fs.writeFileSync(path.join(imgDir, 'flag_italy.png'), buffer);
    console.log('✅ Bandeira da Itália salva: img/flag_italy.png');
}

/**
 * Desenha uma estrela
 */
function drawStar(ctx, cx, cy, spikes, outerRadius, innerRadius) {
    let rot = Math.PI / 2 * 3;
    let x = cx;
    let y = cy;
    const step = Math.PI / spikes;

    ctx.beginPath();
    ctx.moveTo(cx, cy - outerRadius);
    
    for (let i = 0; i < spikes; i++) {
        x = cx + Math.cos(rot) * outerRadius;
        y = cy + Math.sin(rot) * outerRadius;
        ctx.lineTo(x, y);
        rot += step;

        x = cx + Math.cos(rot) * innerRadius;
        y = cy + Math.sin(rot) * innerRadius;
        ctx.lineTo(x, y);
        rot += step;
    }
    
    ctx.lineTo(cx, cy - outerRadius);
    ctx.closePath();
    ctx.fill();
}

/**
 * Gera versões menores (ícones)
 */
function gerarIcones() {
    console.log('📐 Gerando ícones pequenos...');
    
    // Brasil - ícone 64x64
    const brazilIcon = createCanvas(64, 64);
    const ctxBr = brazilIcon.getContext('2d');
    
    ctxBr.fillStyle = '#009c3b';
    ctxBr.fillRect(0, 0, 64, 64);
    
    ctxBr.fillStyle = '#ffdf00';
    ctxBr.beginPath();
    ctxBr.moveTo(32, 8);
    ctxBr.lineTo(56, 32);
    ctxBr.lineTo(32, 56);
    ctxBr.lineTo(8, 32);
    ctxBr.closePath();
    ctxBr.fill();
    
    ctxBr.fillStyle = '#002776';
    ctxBr.beginPath();
    ctxBr.arc(32, 32, 12, 0, 2 * Math.PI);
    ctxBr.fill();
    
    const bufferBr = brazilIcon.toBuffer('image/png');
    fs.writeFileSync(path.join(imgDir, 'icon_brazil.png'), bufferBr);
    
    // Itália - ícone 64x64
    const italyIcon = createCanvas(64, 64);
    const ctxIt = italyIcon.getContext('2d');
    
    ctxIt.fillStyle = '#009246';
    ctxIt.fillRect(0, 0, 21, 64);
    
    ctxIt.fillStyle = '#ffffff';
    ctxIt.fillRect(21, 0, 22, 64);
    
    ctxIt.fillStyle = '#ce2b37';
    ctxIt.fillRect(43, 0, 21, 64);
    
    const bufferIt = italyIcon.toBuffer('image/png');
    fs.writeFileSync(path.join(imgDir, 'icon_italy.png'), bufferIt);
    
    console.log('✅ Ícones salvos: icon_brazil.png e icon_italy.png');
}

/**
 * Função principal
 */
function main() {
    console.log('='.repeat(60));
    console.log('🎨 GERADOR DE BANDEIRAS - BRASIL E ITÁLIA');
    console.log('='.repeat(60));
    console.log();
    
    try {
        gerarBandeiraBrasil();
        gerarBandeiraItalia();
        gerarIcones();
        
        console.log();
        console.log('='.repeat(60));
        console.log('✅ TODAS AS BANDEIRAS FORAM GERADAS COM SUCESSO!');
        console.log('='.repeat(60));
        console.log();
        console.log('Arquivos criados:');
        console.log('  📄 img/flag_brazil.png  (300x210) - Bandeira do Brasil');
        console.log('  📄 img/flag_italy.png   (300x200) - Bandeira da Itália');
        console.log('  📄 img/icon_brazil.png  (64x64)   - Ícone Brasil');
        console.log('  📄 img/icon_italy.png   (64x64)   - Ícone Itália');
        console.log();
        console.log('💡 Use no README.md:');
        console.log('   ![Brasil](img/flag_brazil.png)');
        console.log('   ![Itália](img/flag_italy.png)');
        console.log();
        
        process.exit(0);
        
    } catch (error) {
        console.error();
        console.error('❌ ERRO ao gerar bandeiras:');
        console.error(`   ${error.message}`);
        console.error();
        process.exit(1);
    }
}

// Executar
if (require.main === module) {
    main();
}

module.exports = { gerarBandeiraBrasil, gerarBandeiraItalia, gerarIcones };

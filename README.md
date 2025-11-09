# Pomodoro Timer / Cronômetro Pomodoro

<p align="center">
  <img src="img/icon_brazil.png" alt="Brasil" width="48" height="48" />
  <strong>Português</strong>
  &nbsp;&nbsp;|&nbsp;&nbsp;
  <img src="img/icon_italy.png" alt="Itália" width="48" height="48" />
  <strong>Italiano</strong>
</p>

<p align="center">
  Aplicativo de gerenciamento de tempo baseado na Técnica Pomodoro.<br>
  Applicazione per la gestione del tempo basata sulla Tecnica Pomodoro.
</p>

<p align="center">
  <img src="img/tela_inicial.png" alt="Tela Inicial" width="500" />
</p>

---

## Descrição / Descrizione

### Português

O Pomodoro Timer é uma ferramenta para aumentar a produtividade através da Técnica Pomodoro. O método consiste em trabalhar por 25 minutos (um "pomodoro"), seguido de 5 minutos de descanso. Após completar 4 pomodoros, o usuário ganha um descanso maior de 30 minutos. O aplicativo possui interface gráfica intuitiva com animação de tomate e sistema de notificações sonoras.

### Italiano

Il Pomodoro Timer è uno strumento per aumentare la produttività attraverso la Tecnica Pomodoro. Il metodo consiste nel lavorare per 25 minuti (un "pomodoro"), seguito da 5 minuti di pausa. Dopo aver completato 4 pomodori, l'utente ottiene una pausa più lunga di 30 minuti. L'applicazione ha un'interfaccia grafica intuitiva con animazione di pomodoro e sistema di notifiche sonore.

---

## Funcionalidades / Funzionalità

### Português

- Ciclos de trabalho de 25 minutos (Pomodoro)
- Pausas curtas de 5 minutos
- Pausa longa de 30 minutos após 4 pomodoros
- Interface gráfica com animação de tomate
- Notificações sonoras ao final de cada ciclo
- Contador visual de pomodoros completados
- Histórico de sessões em arquivo de log
- Atalhos de teclado para controle rápido
- Compilação para executável Windows

### Italiano

- Cicli di lavoro di 25 minuti (Pomodoro)
- Pause brevi di 5 minuti
- Pausa lunga di 30 minuti dopo 4 pomodori
- Interfaccia grafica con animazione di pomodoro
- Notifiche sonore alla fine di ogni ciclo
- Contatore visivo dei pomodori completati
- Cronologia delle sessioni in file di log
- Scorciatoie da tastiera per controllo rapido
- Compilazione in eseguibile Windows

---

## Requisitos do Sistema / Requisiti di Sistema

- Windows 7/8/10/11 (ou Linux/macOS com Python)
- Python 3.7 ou superior / Python 3.7 o superiore
- Resolução mínima / Risoluzione minima: 800x600 pixels

---

## Dependências / Dipendenze

- Python 3.x (tkinter incluído / tkinter incluso)
- Pillow >= 10.0.0 (manipulação de imagens / manipolazione di immagini)
- PyInstaller >= 6.0.0 (compilação para executável / compilazione in eseguibile)

---

## Instalação e Execução / Installazione ed Esecuzione

### Método 1: Executar com Python / Metodo 1: Eseguire con Python

**Português:**

1. Clone ou baixe este repositório
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o aplicativo:

```bash
python pomodoro.py
```

**Italiano:**

1. Clona o scarica questo repository
2. Installa le dipendenze:

```bash
pip install -r requirements.txt
```

3. Esegui l'applicazione:

```bash
python pomodoro.py
```

### Método 2: Arquivo Batch (Windows) / Metodo 2: File Batch (Windows)

Execute o arquivo / Esegui il file `scripts\executar_pomodoro.bat` com duplo clique / con doppio clic.

---

## Compilação para Executável / Compilazione in Eseguibile

### Compilação Automática / Compilazione Automatica

**Português:**  
Execute o script de compilação:

```bash
python scripts\pomodoro_exe.py
```

Ou use o arquivo batch:

```bash
scripts\compilar_pomodoro.bat
```

**Italiano:**  
Esegui lo script di compilazione:

```bash
python scripts\pomodoro_exe.py
```

O usa il file batch:

```bash
scripts\compilar_pomodoro.bat
```

### Compilação Manual / Compilazione Manuale

1. Instale PyInstaller / Installa PyInstaller:

```bash
pip install pyinstaller
```

2. Compile o executável / Compila l'eseguibile:

```bash
pyinstaller --onefile --windowed --name pomodoro --icon img\pomodoro.ico pomodoro.py
```

3. O executável será criado em / L'eseguibile sarà creato in `dist\pomodoro.exe`

---

## Atalhos de Teclado / Scorciatoie da Tastiera

- `Espaço / Spazio`: Iniciar/Pausar timer / Avvia/Pausa timer
- `R`: Reiniciar ciclo atual / Riavvia ciclo attuale
- `ESC`: Fechar aplicativo / Chiudi applicazione

---

## A Técnica Pomodoro / La Tecnica Pomodoro

### Português

A Técnica Pomodoro foi criada por Francesco Cirillo no final dos anos 1980. O nome vem do timer de cozinha em forma de tomate (pomodoro em italiano) que Cirillo usava quando era estudante universitário.

**Como funciona:**

1. Escolha uma tarefa
2. Configure o timer para 25 minutos (1 Pomodoro)
3. Trabalhe na tarefa até o timer tocar
4. Faça uma pausa curta de 5 minutos
5. A cada 4 Pomodoros, faça uma pausa longa de 30 minutos

**Benefícios:**

- Melhora o foco e concentração
- Reduz a procrastinação
- Aumenta a produtividade
- Previne o esgotamento mental
- Facilita o planejamento e estimativa de tarefas

### Italiano

La Tecnica Pomodoro è stata creata da Francesco Cirillo alla fine degli anni '80. Il nome deriva dal timer da cucina a forma di pomodoro che Cirillo usava quando era studente universitario.

**Come funziona:**

1. Scegli un compito
2. Imposta il timer per 25 minuti (1 Pomodoro)
3. Lavora sul compito fino a quando il timer suona
4. Fai una pausa breve di 5 minuti
5. Ogni 4 Pomodori, fai una pausa lunga di 30 minuti

**Benefici:**

- Migliora la concentrazione e l'attenzione
- Riduce la procrastinazione
- Aumenta la produttività
- Previene l'esaurimento mentale
- Facilita la pianificazione e la stima dei compiti

---

## Estrutura de Arquivos / Struttura dei File

```text
workspace_pomodoro/
├── pomodoro.py              # Aplicativo principal / Applicazione principale
├── requirements.txt         # Dependências Python / Dipendenze Python
├── pomodoro_log.txt         # Histórico de sessões / Cronologia delle sessioni
├── LICENSE                  # Licença MIT / Licenza MIT
├── README.md                # Este arquivo / Questo file
├── img/                     # Imagens e ícones / Immagini e icone
│   ├── pomodoro.ico         # Ícone do aplicativo / Icona dell'applicazione
│   ├── pomodoro.gif         # Animação trabalho / Animazione lavoro
│   ├── pomodoro_break.gif   # Animação pausa curta / Animazione pausa breve
│   ├── pomodoro_longbreak.gif # Animação pausa longa / Animazione pausa lunga
│   ├── preview.png          # Prévia do aplicativo / Anteprima dell'applicazione
│   ├── tela_inicial.png     # Screenshot inicial / Screenshot iniziale
│   ├── flag_brazil.png      # Bandeira do Brasil / Bandiera del Brasile
│   ├── flag_italy.png       # Bandeira da Itália / Bandiera dell'Italia
│   ├── icon_brazil.png      # Ícone Brasil / Icona Brasile
│   └── icon_italy.png       # Ícone Itália / Icona Italia
├── scripts/                 # Scripts auxiliares / Script ausiliari
│   ├── pomodoro_exe.py      # Script de compilação / Script di compilazione
│   ├── gerar_assets.py      # Gerador de imagens / Generatore di immagini
│   ├── gerar_bandeiras.js   # Gerador de bandeiras / Generatore di bandiere
│   ├── executar_pomodoro.bat # Executar com Python / Eseguire con Python
│   └── compilar_pomodoro.bat # Compilar executável / Compilare eseguibile
└── testes/                  # Testes automatizados / Test automatizzati
    ├── test_timer_logic.py  # Testes unitários / Test unitari
    ├── test_e2e_manual.py   # Testes E2E manuais / Test E2E manuali
    ├── pomodoro_test.py     # Versão de teste rápido / Versione test rapido
    ├── RELATORIO_TESTES.md  # Relatório de testes / Rapporto di test
    └── README_TESTES.md     # Documentação de testes / Documentazione test
```

---

## Logs e Histórico / Log e Cronologia

### Português

Todas as sessões são registradas no arquivo `pomodoro_log.txt` com as seguintes informações:

- Data e hora de início
- Tipo de ciclo (Trabalho, Pausa Curta, Pausa Longa)
- Duração do ciclo
- Número de pomodoros completados
- Total acumulado de pomodoros

### Italiano

Tutte le sessioni sono registrate nel file `pomodoro_log.txt` con le seguenti informazioni:

- Data e ora di inizio
- Tipo di ciclo (Lavoro, Pausa Breve, Pausa Lunga)
- Durata del ciclo
- Numero di pomodori completati
- Totale cumulativo di pomodori

---

## Testes / Test

### Português

O projeto inclui uma suíte completa de testes:

**Testes Unitários:**

- Validação de tempos (25/5/30 minutos)
- Lógica de ciclos (4 pomodoros → pausa longa)
- Formatação de tempo (MM:SS)
- Transições de estado
- Sistema de logging

**Testes E2E:**

- Interface gráfica
- Animações GIF
- Notificações sonoras
- Atalhos de teclado
- Versão de teste rápido (5s/3s/10s)

Para executar os testes:

```bash
python testes\test_timer_logic.py
```

### Italiano

Il progetto include una suite completa di test:

**Test Unitari:**

- Validazione dei tempi (25/5/30 minuti)
- Logica dei cicli (4 pomodori → pausa lunga)
- Formattazione del tempo (MM:SS)
- Transizioni di stato
- Sistema di logging

**Test E2E:**

- Interfaccia grafica
- Animazioni GIF
- Notifiche sonore
- Scorciatoie da tastiera
- Versione test rapido (5s/3s/10s)

Per eseguire i test:

```bash
python testes\test_timer_logic.py
```

---

## Troubleshooting

### Português

**Problema: Animação não aparece**

- Verifique se o arquivo `img\pomodoro.gif` existe
- Certifique-se de que a biblioteca Pillow está instalada: `pip install Pillow`

**Problema: Executável não abre**

- Execute como administrador
- Verifique se o Windows Defender não bloqueou o arquivo
- Recompile o executável usando `scripts\pomodoro_exe.py`

**Problema: Ícone não aparece**

- Verifique se o arquivo `img\pomodoro.ico` existe
- Recompile o executável especificando o caminho do ícone

### Italiano

**Problema: L'animazione non appare**

- Verifica che il file `img\pomodoro.gif` esista
- Assicurati che la libreria Pillow sia installata: `pip install Pillow`

**Problema: L'eseguibile non si apre**

- Esegui come amministratore
- Verifica che Windows Defender non abbia bloccato il file
- Ricompila l'eseguibile usando `scripts\pomodoro_exe.py`

**Problema: L'icona non appare**

- Verifica che il file `img\pomodoro.ico` esista
- Ricompila l'eseguibile specificando il percorso dell'icona

---

## Geração de Assets / Generazione di Asset

### Português

Os assets visuais podem ser regenerados usando os scripts na pasta `scripts/`:

**Gerar GIFs e ícones:**

```bash
python scripts\gerar_assets.py
```

**Gerar bandeiras:**

```bash
node scripts\gerar_bandeiras.js
```

### Italiano

Gli asset visivi possono essere rigenerati usando gli script nella cartella `scripts/`:

**Generare GIF e icone:**

```bash
python scripts\gerar_assets.py
```

**Generare bandiere:**

```bash
node scripts\gerar_bandeiras.js
```

---

## Licença / Licenza

MIT License

Copyright (c) 2025 Christian Vladimir Uhdre Mulato

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## Autor / Autore

**Christian Vladimir Uhdre Mulato**  
Campo Largo, PR - Brasil  
Data: 09 de Novembro de 2025

GitHub: [https://github.com/chmulato]  
Repositório: [https://github.com/chmulato/pomodoro]

---

## Agradecimentos / Ringraziamenti

### Português

Agradecimentos especiais a Francesco Cirillo por criar a Técnica Pomodoro e compartilhá-la com o mundo.

### Italiano

Ringraziamenti speciali a Francesco Cirillo per aver creato la Tecnica Pomodoro e averla condivisa con il mondo.

---

## Versão / Versione

**v1.0.0** - Versão inicial / Versione iniziale (09/11/2025)

### Changelog

**v1.0.0 (09/11/2025)**

- Implementação inicial do Pomodoro Timer
- Interface gráfica bilíngue (PT/IT)
- Animações GIF para trabalho, pausa curta e pausa longa
- Sistema de notificações sonoras
- Contador de pomodoros completados
- Sistema de logging de sessões
- Atalhos de teclado
- Scripts de compilação para Windows
- Suíte completa de testes (unitários e E2E)
- Documentação completa em português e italiano

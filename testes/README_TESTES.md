# 🧪 Testes - Pomodoro Timer

Documentação dos testes end-to-end para validação da aplicação Pomodoro Timer.

## 📂 Estrutura de Testes

```
testes/
├── __init__.py              # Inicialização do pacote
├── test_timer_logic.py      # Testes unitários (lógica)
├── test_e2e_manual.py       # Roteiro de testes E2E manuais
└── README_TESTES.md         # Esta documentação
```

## 🚀 Como Executar os Testes

### Testes Unitários (Automatizados)

```bash
# Executar testes unitários
cd D:\dev\workspace_pomodoro
python testes\test_timer_logic.py
```

**O que é testado:**
- ✅ Durações dos períodos (25/5/30 minutos)
- ✅ Lógica do ciclo de 4 pomodoros
- ✅ Formatação do tempo (MM:SS)
- ✅ Transições de estados
- ✅ Contador de tomates
- ✅ Sistema de logging

### Testes E2E Manuais (Interface Gráfica)

```bash
# 1. Iniciar aplicação em uma janela
python pomodoro.py

# 2. Em outra janela, executar roteiro de testes
python testes\test_e2e_manual.py
```

**O que é testado:**
1. Interface inicial e elementos visuais
2. Iniciar/pausar/retomar timer
3. Resetar timer
4. Completar pomodoro (notificação + som)
5. Ciclo completo de 4 pomodoros
6. Atalhos de teclado (Espaço, R, ESC)
7. Sistema de log (`pomodoro_log.txt`)
8. Animações GIF
9. Suporte bilíngue (PT/IT)

## ⚡ Testes Rápidos (Tempos Reduzidos)

Para testar rapidamente sem esperar 25 minutos, modifique temporariamente em `pomodoro.py`:

```python
# CONFIGURAÇÕES (modificar temporariamente)
WORK_TIME = 5        # 5 segundos ao invés de 1500
SHORT_BREAK = 3      # 3 segundos ao invés de 300
LONG_BREAK = 10      # 10 segundos ao invés de 1800
```

**⚠️ IMPORTANTE:** Restaure os valores originais após os testes!

## 📊 Cobertura de Testes

### Testes Unitários
- **TestPomodoroLogic**: Lógica de temporização
- **TestPomodoroStates**: Máquina de estados
- **TestPomodoroCounter**: Contador de tomates
- **TestLogging**: Sistema de logging

### Testes E2E Manuais
- **Teste 1**: Interface inicial
- **Teste 2**: Iniciar timer
- **Teste 3**: Pausar e retomar
- **Teste 4**: Resetar timer
- **Teste 5**: Completar pomodoro
- **Teste 6**: Ciclo completo (4 pomodoros)
- **Teste 7**: Atalhos de teclado
- **Teste 8**: Sistema de log
- **Teste 9**: Animações GIF
- **Teste 10**: Suporte bilíngue

## 🐛 Reportando Bugs

Ao encontrar bugs durante os testes, documente:

1. **Descrição**: O que aconteceu?
2. **Esperado**: O que deveria acontecer?
3. **Passos**: Como reproduzir?
4. **Ambiente**: Windows/Linux/Mac, versão Python
5. **Log**: Copiar saída relevante de `pomodoro_log.txt`

### Exemplo:

```
BUG #001: Timer não pausa ao pressionar Espaço

Descrição: Ao pressionar barra de espaço com timer rodando, nada acontece.
Esperado: Timer deveria pausar e botão mudar para "Retomar".
Passos:
  1. Iniciar timer
  2. Aguardar 5 segundos
  3. Pressionar Espaço
  4. Timer continua rodando
Ambiente: Windows 11, Python 3.11.5
Log: [2025-11-09 11:30:45] INÍCIO
```

## ✅ Checklist de Validação

Antes de considerar a aplicação pronta para release:

- [ ] Todos os testes unitários passam
- [ ] Todos os testes E2E manuais passam
- [ ] Animações GIF funcionam corretamente
- [ ] Notificações sonoras funcionam
- [ ] Arquivo de log é criado e atualizado
- [ ] Atalhos de teclado funcionam
- [ ] Contador de tomates incrementa corretamente
- [ ] Pausa longa acontece após 4 pomodoros
- [ ] Aplicação pode ser compilada (pomodoro_exe.py)
- [ ] Executável funciona sem Python instalado
- [ ] Textos bilíngues (PT/IT) estão corretos

## 🔧 Testes de Compilação

```bash
# Compilar aplicação
python pomodoro_exe.py

# Testar executável
cd dist
.\pomodoro.exe
```

**Verificar:**
- ✅ Executável abre sem erros
- ✅ GIF e ícone são carregados
- ✅ Todas as funcionalidades funcionam
- ✅ Log é criado na mesma pasta do executável

## 📚 Recursos Adicionais

- **Python unittest**: https://docs.python.org/3/library/unittest.html
- **tkinter testing**: https://wiki.python.org/moin/TkInter
- **Pomodoro Technique**: https://francescocirillo.com/pages/pomodoro-technique

---

**Última atualização**: 09/11/2025
**Versão**: 1.0.0

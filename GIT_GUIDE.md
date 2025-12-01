# Guia de Upload para Git

## 📁 Arquivos que DEVEM ser subidos

### ✅ Código Fonte (ESSENCIAL)
```
main.py                          # Script principal
config/
  └── settings.py                # Configurações
src/
  ├── __init__.py                # (se existir)
  ├── data/
  │   ├── __init__.py
  │   └── data_processor.py
  ├── analysis/
  │   ├── __init__.py
  │   ├── metrics.py
  │   ├── temporal.py
  │   ├── customers.py
  │   ├── sellers.py
  │   └── products.py
  └── utils/
      ├── __init__.py
      ├── data_loader.py
      └── visualization.py
```

### ✅ Configuração e Dependências
```
requirements.txt                 # Dependências do projeto
.gitignore                      # Arquivos ignorados
```

### ✅ Documentação (RECOMENDADO)
```
README.md                       # Documentação principal
PROJECT_OVERVIEW.md             # Visão geral do projeto
RELATORIO_TESTES.md             # Relatório de testes
```

### ✅ Estrutura de Diretórios
```
outputs/
  ├── __init__.py               # Mantém estrutura
  ├── figures/
  │   └── .gitkeep              # Mantém diretório vazio
  └── reports/
      └── .gitkeep              # Mantém diretório vazio
```

---

## ❌ Arquivos que NÃO devem ser subidos

### Dados (geralmente muito grandes)
```
DataSet/                        # Arquivos CSV (muito grandes)
  └── *.csv
```

### Outputs Gerados
```
outputs/figures/*.png           # Gráficos gerados
outputs/reports/*.txt           # Relatórios gerados
```

### Arquivos Temporários
```
__pycache__/                    # Cache Python
*.pyc                           # Bytecode Python
*.pyo                           # Bytecode otimizado
*.pyd                           # Extensões Python
*.log                           # Logs
test_*.py                       # Scripts de teste temporários
test_*.txt                      # Resultados de testes
validation_report.txt
test_results*.txt
test_execution.log
```

### Arquivos do Sistema
```
.DS_Store                       # macOS
Thumbs.db                       # Windows
.vscode/                        # Configurações do VS Code
.idea/                          # Configurações do PyCharm
*.swp                           # Vim
*.swo                           # Vim
```

---

## 📋 Checklist para Upload

### Antes de fazer commit:

- [ ] Verificar se `.gitignore` está atualizado
- [ ] Remover arquivos de teste temporários
- [ ] Verificar se não há dados sensíveis
- [ ] Confirmar que `requirements.txt` está atualizado
- [ ] Verificar se documentação está completa

### Comandos Git Recomendados:

```bash
# 1. Verificar status
git status

# 2. Adicionar arquivos essenciais
git add main.py
git add config/
git add src/
git add requirements.txt
git add .gitignore
git add README.md
git add PROJECT_OVERVIEW.md
git add outputs/__init__.py
git add outputs/figures/.gitkeep
git add outputs/reports/.gitkeep

# 3. Ou adicionar tudo (respeitando .gitignore)
git add .

# 4. Verificar o que será commitado
git status

# 5. Fazer commit
git commit -m "Initial commit: Projeto de análise de dados Olist"

# 6. Adicionar remote (se necessário)
git remote add origin <URL_DO_REPOSITORIO>

# 7. Push
git push -u origin main
```

---

## 🎯 Estrutura Final no Git

```
Projeto_A3/
├── .gitignore
├── README.md
├── PROJECT_OVERVIEW.md
├── RELATORIO_TESTES.md
├── requirements.txt
├── main.py
├── config/
│   └── settings.py
├── src/
│   ├── data/
│   │   ├── __init__.py
│   │   └── data_processor.py
│   ├── analysis/
│   │   ├── __init__.py
│   │   ├── metrics.py
│   │   ├── temporal.py
│   │   ├── customers.py
│   │   ├── sellers.py
│   │   └── products.py
│   └── utils/
│       ├── __init__.py
│       ├── data_loader.py
│       └── visualization.py
└── outputs/
    ├── __init__.py
    ├── figures/
    │   └── .gitkeep
    └── reports/
        └── .gitkeep
```

---

## ⚠️ Importante

### Sobre os Dados CSV:
- **NÃO subir** os arquivos CSV (muito grandes)
- Adicionar instrução no README sobre onde obter os dados
- Ou criar um script de download dos dados

### Sobre Outputs:
- **NÃO subir** gráficos e relatórios gerados
- Eles serão criados quando o projeto for executado
- Manter apenas estrutura de diretórios (.gitkeep)

---

## 📝 Exemplo de .gitignore Atualizado

O `.gitignore` atual já está configurado corretamente para ignorar:
- Outputs gerados
- Cache Python
- Arquivos temporários
- Dados CSV (se você adicionar DataSet/ ao .gitignore)

---

## ✅ Resumo Rápido

**SUBIR:**
- ✅ Todo o código fonte (src/, config/, main.py)
- ✅ requirements.txt
- ✅ .gitignore
- ✅ Documentação (.md)
- ✅ Estrutura de diretórios (__init__.py, .gitkeep)

**NÃO SUBIR:**
- ❌ Arquivos CSV (DataSet/)
- ❌ Gráficos gerados (outputs/figures/*.png)
- ❌ Relatórios gerados (outputs/reports/*.txt)
- ❌ Arquivos de teste temporários
- ❌ Cache Python (__pycache__)


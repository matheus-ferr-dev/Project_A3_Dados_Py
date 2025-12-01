# 📤 Guia de Upload para Git

## ✅ Arquivos que DEVEM ser subidos

### 1. Código Fonte (ESSENCIAL)
```
main.py
config/
  └── settings.py
src/
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

### 2. Configuração
```
requirements.txt
.gitignore
```

### 3. Documentação
```
README.md
PROJECT_OVERVIEW.md
RELATORIO_TESTES.md
GIT_UPLOAD.md (este arquivo)
```

### 4. Estrutura de Diretórios
```
outputs/
  ├── __init__.py
  ├── figures/
  │   └── .gitkeep
  └── reports/
      └── .gitkeep
```

---

## ❌ Arquivos que NÃO devem ser subidos

### Dados (muito grandes)
```
DataSet/                    # Arquivos CSV
  └── *.csv
```

### Outputs Gerados
```
outputs/figures/*.png       # Gráficos
outputs/reports/*.txt       # Relatórios
```

### Arquivos de Teste Temporários
```
test_*.py
test_*.txt
validate_project.py
execute_tests.py
run_and_test.py
simple_test.py
test_complete.py
test_run.py
```

### Cache e Temporários
```
__pycache__/
*.pyc
*.log
```

---

## 🚀 Comandos para Upload

### Opção 1: Adicionar arquivos específicos

```bash
# Inicializar repositório (se ainda não foi feito)
git init

# Adicionar arquivos essenciais
git add main.py
git add config/
git add src/
git add requirements.txt
git add .gitignore
git add README.md
git add PROJECT_OVERVIEW.md
git add RELATORIO_TESTES.md
git add outputs/__init__.py
git add outputs/figures/.gitkeep
git add outputs/reports/.gitkeep

# Verificar o que será commitado
git status

# Fazer commit
git commit -m "Initial commit: Projeto de análise de dados Olist"

# Adicionar remote
git remote add origin <URL_DO_SEU_REPOSITORIO>

# Push
git push -u origin main
```

### Opção 2: Adicionar tudo (respeitando .gitignore)

```bash
# Adicionar tudo (o .gitignore vai filtrar automaticamente)
git add .

# Verificar
git status

# Commit
git commit -m "Initial commit: Projeto de análise de dados Olist"

# Push
git push -u origin main
```

---

## 📋 Checklist Antes do Upload

- [ ] `.gitignore` está atualizado
- [ ] Arquivos de teste temporários foram removidos ou estão no .gitignore
- [ ] `requirements.txt` está atualizado
- [ ] Documentação está completa
- [ ] Não há dados sensíveis no código
- [ ] Estrutura de diretórios está correta

---

## 📁 Estrutura Final no Git

```
Projeto_A3/
├── .gitignore
├── README.md
├── PROJECT_OVERVIEW.md
├── RELATORIO_TESTES.md
├── GIT_UPLOAD.md
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
- **NÃO subir** os arquivos CSV (podem ser muito grandes)
- Adicione uma nota no README sobre onde obter os dados
- Ou crie um script de download

### Sobre Outputs:
- **NÃO subir** gráficos e relatórios gerados
- Eles serão criados quando alguém executar o projeto
- Mantenha apenas a estrutura (.gitkeep)

---

## ✅ Resumo Rápido

**SUBIR:**
- ✅ Código fonte completo (src/, config/, main.py)
- ✅ requirements.txt
- ✅ .gitignore
- ✅ Documentação (.md)
- ✅ Estrutura de diretórios

**NÃO SUBIR:**
- ❌ DataSet/*.csv (dados)
- ❌ outputs/figures/*.png (gráficos gerados)
- ❌ Arquivos de teste temporários
- ❌ Cache Python

---

## 🎯 Comando Rápido

```bash
git add . && git status
```

Isso adiciona tudo respeitando o `.gitignore` e mostra o que será commitado.


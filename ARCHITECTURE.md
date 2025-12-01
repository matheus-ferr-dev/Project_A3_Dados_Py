# Arquitetura do Projeto

Este documento descreve a arquitetura e organização do projeto de análise de dados Olist.

## Princípios de Design

### 1. Modularidade
O projeto é organizado em módulos independentes e reutilizáveis:
- **config/**: Configurações centralizadas
- **src/data/**: Processamento de dados
- **src/analysis/**: Análises específicas
- **src/utils/**: Funções utilitárias

### 2. Separação de Responsabilidades
Cada módulo tem uma responsabilidade específica:
- **Data Loader**: Apenas carregamento de dados
- **Data Processor**: Apenas processamento e transformação
- **Analysis Modules**: Apenas cálculos e análises
- **Visualization**: Apenas criação de gráficos

### 3. Configuração Centralizada
Todas as configurações estão em `config/settings.py`:
- Caminhos de arquivos
- Configurações de visualização
- Configurações do pandas

### 4. Reutilização de Código
Funções comuns são extraídas para módulos utilitários:
- `src/utils/data_loader.py`: Carregamento de CSV
- `src/utils/visualization.py`: Configuração de gráficos

## Estrutura de Diretórios

```
Projeto_A3/
├── config/                 # Configurações
│   └── settings.py        # Todas as configurações do projeto
│
├── src/                   # Código fonte
│   ├── data/             # Processamento de dados
│   │   ├── __init__.py
│   │   └── data_processor.py
│   │
│   ├── analysis/         # Módulos de análise
│   │   ├── __init__.py
│   │   ├── metrics.py    # Métricas principais
│   │   ├── temporal.py   # Análise temporal
│   │   ├── customers.py  # Análise de clientes
│   │   ├── sellers.py    # Análise de vendedores
│   │   └── products.py   # Análise de produtos
│   │
│   ├── visualization/    # Visualizações (futuro)
│   │   └── charts.py
│   │
│   └── utils/            # Utilitários
│       ├── __init__.py
│       ├── data_loader.py
│       └── visualization.py
│
├── DataSet/              # Dados brutos
│   └── *.csv
│
├── outputs/              # Resultados
│   ├── figures/         # Gráficos gerados
│   └── reports/         # Relatórios em texto
│
├── main.py               # Script principal
├── requirements.txt      # Dependências
├── README.md             # Documentação principal
└── ARCHITECTURE.md       # Este arquivo
```

## Fluxo de Dados

1. **Carregamento** (`src/utils/data_loader.py`)
   - Carrega CSVs do diretório `DataSet/`
   - Retorna DataFrames individuais

2. **Processamento** (`src/data/data_processor.py`)
   - Faz merge de todas as tabelas
   - Processa colunas (datas, receita, etc.)
   - Retorna DataFrame consolidado

3. **Análise** (`src/analysis/*.py`)
   - Cada módulo faz análises específicas
   - Retorna dicionários com resultados

4. **Visualização** (`main.py`)
   - Usa resultados das análises
   - Gera gráficos e salva em `outputs/figures/`

5. **Relatório** (`main.py`)
   - Consolida insights
   - Gera relatório em texto em `outputs/reports/`

## Padrões de Código

### Nomenclatura
- **Funções**: snake_case (`calculate_metrics`)
- **Classes**: PascalCase (`DataProcessor`)
- **Constantes**: UPPER_SNAKE_CASE (`DATA_DIR`)

### Documentação
- Todas as funções têm docstrings
- Type hints quando possível
- Comentários explicativos em código complexo

### Tratamento de Erros
- Validação de inputs
- Mensagens de erro claras
- Fallbacks quando apropriado

## Extensibilidade

### Adicionar Nova Análise
1. Criar módulo em `src/analysis/`
2. Implementar função de análise
3. Adicionar ao `__init__.py`
4. Chamar em `main.py`

### Adicionar Nova Visualização
1. Criar função em `main.py` ou módulo de visualização
2. Usar `save_figure()` para salvar
3. Adicionar ao fluxo principal

### Adicionar Nova Fonte de Dados
1. Adicionar configuração em `config/settings.py`
2. Atualizar `data_loader.py` se necessário
3. Integrar no `data_processor.py`

## Boas Práticas Seguidas

✅ **DRY (Don't Repeat Yourself)**: Código reutilizável em módulos  
✅ **SOLID Principles**: Separação de responsabilidades  
✅ **Clean Code**: Código legível e bem documentado  
✅ **Configuration Management**: Configurações centralizadas  
✅ **Error Handling**: Tratamento adequado de erros  
✅ **Type Hints**: Tipagem quando possível  
✅ **Documentation**: Docstrings e comentários  

## Melhorias Futuras

- [ ] Adicionar testes unitários
- [ ] Implementar logging estruturado
- [ ] Criar pipeline de CI/CD
- [ ] Adicionar validação de dados
- [ ] Implementar cache de resultados
- [ ] Criar API REST para acesso aos dados
- [ ] Adicionar suporte a banco de dados


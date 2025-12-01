# Visão Geral do Projeto - Análise de Dados Olist

## 📋 Sobre o Projeto

Este projeto realiza uma análise completa e profissional dos dados do e-commerce Olist, fornecendo insights estratégicos através de visualizações e métricas de negócio. O projeto foi desenvolvido seguindo boas práticas de arquitetura de software, clean code e ciência de dados.

### Objetivo

Analisar dados de vendas, clientes, produtos e vendedores da Olist para identificar padrões, tendências e oportunidades de negócio através de análises estatísticas e visualizações.

## 🏗️ Arquitetura do Projeto

O projeto segue uma arquitetura modular e escalável, organizada em camadas bem definidas:

```
Projeto_A3/
├── config/                 # Configurações centralizadas
│   └── settings.py         # Todas as configurações do projeto
│
├── src/                    # Código fonte modular
│   ├── data/              # Camada de dados
│   │   └── data_processor.py
│   ├── analysis/          # Camada de análise
│   │   ├── metrics.py
│   │   ├── temporal.py
│   │   ├── customers.py
│   │   ├── sellers.py
│   │   └── products.py
│   └── utils/             # Utilitários reutilizáveis
│       ├── data_loader.py
│       └── visualization.py
│
├── DataSet/                # Dados brutos (CSV)
├── outputs/               # Resultados gerados
│   ├── figures/          # Gráficos
│   └── reports/          # Relatórios
│
└── main.py                # Ponto de entrada principal
```

## 📦 Componentes Principais

### 1. Configuração (`config/settings.py`)

Centraliza todas as configurações do projeto:
- **Diretórios**: Caminhos para dados, figuras e relatórios
- **Arquivos CSV**: Mapeamento de nomes de arquivos (padrão e alternativo)
- **Visualização**: Configurações de estilo, tamanhos e paletas de cores
- **Pandas**: Configurações de exibição de DataFrames

**Benefício**: Facilita manutenção e alterações sem modificar código.

### 2. Camada de Dados (`src/data/`)

#### `data_processor.py`

Responsável por:
- **Carregamento**: Usa `data_loader` para carregar todos os CSVs
- **Consolidação**: Realiza merges sequenciais de todas as tabelas
- **Processamento**: 
  - Identifica e processa colunas importantes (preço, frete, timestamp, categoria)
  - Calcula receita total (preço + frete)
  - Converte timestamps para datetime
  - Cria colunas temporais (ano_mês, etc.)
  - Trata valores nulos

**Schema de Merge:**
```
orders + customers (customer_id)
  ↓
resultado + order_items (order_id)
  ↓
resultado + products (product_id)
  ↓
resultado + sellers (seller_id)
  ↓
DataFrame consolidado
```

### 3. Camada de Análise (`src/analysis/`)

Cada módulo é responsável por análises específicas:

#### `metrics.py`
Calcula métricas principais do negócio:
- Volume: total de pedidos, clientes, vendedores, produtos
- Financeiro: receita total, ticket médio
- Comportamento: taxa de recompra, clientes com múltiplas compras
- Temporal: período dos dados (início, fim, duração)

#### `temporal.py`
Análise de evolução temporal:
- Pedidos por mês com crescimento
- Receita por mês com crescimento
- Identificação de meses com maior/menor volume
- Cálculo de ticket médio mensal

#### `customers.py`
Análise de clientes:
- Top 10 cidades com mais clientes
- Top 10 estados com mais clientes
- Distribuição de pedidos por cliente
- Análise de recompra (clientes com múltiplas compras)

#### `sellers.py`
Análise de vendedores:
- Top 10 vendedores por número de vendas
- Top 10 vendedores por receita total
- Distribuição geográfica de vendedores por estado

#### `products.py`
Análise de produtos:
- Top 10 categorias mais vendidas
- Top 10 categorias por ticket médio
- Top 10 categorias com maior frete médio

### 4. Camada de Utilitários (`src/utils/`)

#### `data_loader.py`
Funções para carregamento de dados:
- `load_csv()`: Carrega um CSV específico (tenta nome padrão e alternativo)
- `load_all_datasets()`: Carrega todos os datasets disponíveis

**Características:**
- Tratamento de erros robusto
- Suporte a nomes alternativos de arquivos
- Mensagens de erro claras

#### `visualization.py`
Funções para visualização:
- `setup_visualization()`: Configura ambiente de visualização
- `save_figure()`: Salva figuras no diretório correto com configurações padrão

### 5. Ponto de Entrada (`main.py`)

Orquestra todo o fluxo de análise:

1. **Configuração**: Inicializa ambiente (pandas, visualização)
2. **Carregamento**: Cria DataFrame consolidado
3. **Métricas**: Calcula métricas principais
4. **Análises**: Executa análises específicas (temporal, clientes, vendedores, produtos)
5. **Visualizações**: Gera todos os gráficos
6. **Resultados**: Exibe resumo e localização dos outputs

## 🔄 Fluxo de Execução

```
1. main.py inicia
   ↓
2. configure_environment()
   - Configura pandas
   - Configura visualização
   ↓
3. create_main_dataframe()
   - load_all_datasets() → Carrega CSVs
   - Realiza merges sequenciais
   - Processa colunas
   ↓
4. prepare_temporal_data()
   - Garante timestamps convertidos
   - Cria colunas temporais
   ↓
5. calculate_main_metrics()
   - Calcula todas as métricas principais
   ↓
6. Análises específicas
   - analyze_temporal_evolution()
   - analyze_customers()
   - analyze_sellers()
   - analyze_products()
   ↓
7. generate_visualizations()
   - Cria cards de métricas
   - Gera gráficos temporais
   - Gera gráficos de clientes
   - Gera gráficos de vendedores
   - Gera gráficos de produtos
   ↓
8. Salva resultados em outputs/
```

## 📊 Análises Realizadas

### 1. Métricas Principais
- Total de pedidos, clientes, vendedores, produtos
- Receita total e ticket médio
- Taxa de recompra

### 2. Análise Temporal
- Evolução de pedidos ao longo do tempo
- Evolução de receita mensal
- Identificação de tendências e sazonalidade

### 3. Análise de Clientes
- Distribuição geográfica (cidades e estados)
- Comportamento de recompra
- Segmentação por número de pedidos

### 4. Análise de Vendedores
- Performance por volume de vendas
- Performance por receita
- Distribuição geográfica

### 5. Análise de Produtos
- Categorias mais vendidas
- Ticket médio por categoria
- Análise de frete por categoria

## 📈 Visualizações Geradas

1. **01_metricas_principais.png**: Dashboard com 6 cards de métricas principais
2. **02_evolucao_pedidos.png**: Gráfico de linha mostrando evolução de pedidos
3. **03_evolucao_receita.png**: Gráfico de linha mostrando evolução de receita
4. **04_top10_estados_clientes.png**: Gráfico de barras com top 10 estados
5. **05_top10_vendedores_receita.png**: Gráfico de barras com top 10 vendedores
6. **06_top10_categorias.png**: Gráfico de barras com top 10 categorias

## 🚀 Como Usar

### Instalação

```bash
pip install -r requirements.txt
```

### Execução Completa

```bash
python main.py
```

### Uso Programático

```python
from src.data.data_processor import create_main_dataframe
from src.analysis.metrics import calculate_main_metrics

# Carregar dados
df = create_main_dataframe()

# Calcular métricas
metrics = calculate_main_metrics(df)
print(f"Total de pedidos: {metrics['total_pedidos']:,}")
```

## 🎯 Princípios de Design Aplicados

### 1. Separação de Responsabilidades
Cada módulo tem uma responsabilidade única e bem definida:
- **Data**: Apenas processamento de dados
- **Analysis**: Apenas cálculos e análises
- **Utils**: Apenas funções auxiliares
- **Config**: Apenas configurações

### 2. DRY (Don't Repeat Yourself)
- Funções auxiliares reutilizáveis (`_find_column`, `_find_timestamp_column`)
- Configurações centralizadas
- Código sem duplicação

### 3. Clean Code
- Nomes descritivos e autoexplicativos
- Funções pequenas e focadas
- Sem comentários desnecessários
- Código legível e manutenível

### 4. Modularidade
- Módulos independentes e testáveis
- Fácil adicionar novas análises
- Baixo acoplamento entre componentes

### 5. Configuração Externa
- Todas as configurações em `config/settings.py`
- Fácil ajustar sem modificar código
- Suporte a diferentes ambientes

## 📁 Estrutura de Dados

### Datasets Utilizados

1. **customers**: Dados de clientes (ID, cidade, estado)
2. **orders**: Dados de pedidos (ID, status, timestamps)
3. **order_items**: Itens de pedido (preço, frete, quantidade)
4. **products**: Dados de produtos (categoria, dimensões)
5. **sellers**: Dados de vendedores (ID, estado)

### DataFrame Consolidado

Após os merges, o DataFrame principal contém:
- Todas as colunas de todas as tabelas
- Colunas calculadas: `receita_total`, `ano_mes`, `ano_mes_str`
- Dados tratados: timestamps convertidos, nulos preenchidos

## 🔧 Tecnologias Utilizadas

- **pandas**: Manipulação e análise de dados
- **numpy**: Cálculos numéricos (usado internamente pelo pandas)
- **matplotlib**: Visualizações básicas
- **seaborn**: Visualizações estatísticas avançadas

## 📝 Extensibilidade

### Adicionar Nova Análise

1. Criar módulo em `src/analysis/`
2. Implementar função de análise
3. Adicionar ao `__init__.py`
4. Chamar em `main.py`
5. Criar função de visualização se necessário

### Adicionar Nova Visualização

1. Criar função em `main.py` ou módulo de visualização
2. Usar `save_figure()` para salvar
3. Adicionar ao fluxo em `generate_visualizations()`

### Adicionar Nova Fonte de Dados

1. Adicionar configuração em `config/settings.py` (CSV_FILES)
2. Atualizar `data_processor.py` para incluir no merge
3. Ajustar análises se necessário

## 🎓 Boas Práticas Seguidas

✅ **Modularidade**: Código organizado em módulos reutilizáveis  
✅ **Documentação**: Docstrings em todas as funções  
✅ **Type Hints**: Tipagem quando possível  
✅ **Error Handling**: Tratamento adequado de erros  
✅ **Configuration Management**: Configurações centralizadas  
✅ **Clean Code**: Código limpo e legível  
✅ **SOLID Principles**: Separação de responsabilidades  
✅ **DRY**: Sem duplicação de código  

## 📊 Outputs

Todos os resultados são salvos em `outputs/`:

- **figures/**: Gráficos em alta resolução (300 DPI)
- **reports/**: Relatórios em texto (se implementado)

## 🔍 Exemplo de Fluxo de Dados

```
CSV Files (DataSet/)
    ↓
load_all_datasets()
    ↓
DataFrames individuais
    ↓
create_main_dataframe()
    ↓
DataFrame consolidado
    ↓
prepare_temporal_data()
    ↓
DataFrame processado
    ↓
Análises específicas
    ↓
Dicionários com resultados
    ↓
generate_visualizations()
    ↓
Gráficos salvos (outputs/figures/)
```

## 💡 Insights Fornecidos

O projeto fornece insights sobre:

1. **Performance Financeira**: Receita, ticket médio, crescimento
2. **Comportamento de Clientes**: Recompra, distribuição geográfica
3. **Performance de Vendedores**: Top performers, concentração
4. **Análise de Produtos**: Categorias mais vendidas, ticket médio
5. **Tendências Temporais**: Evolução ao longo do tempo, sazonalidade

## 🎯 Casos de Uso

- **Análise de Negócio**: Entender performance geral
- **Tomada de Decisão**: Baseado em dados reais
- **Identificação de Oportunidades**: Áreas de crescimento
- **Monitoramento**: Acompanhar métricas-chave
- **Relatórios Executivos**: Visualizações profissionais

## 📚 Documentação Adicional

- **README.md**: Guia de instalação e uso básico
- **requirements.txt**: Dependências do projeto
- **.gitignore**: Arquivos ignorados pelo Git

## 🔄 Manutenção

O projeto foi projetado para ser fácil de manter:

- **Código Limpo**: Fácil de ler e entender
- **Modular**: Mudanças isoladas em módulos específicos
- **Configurável**: Ajustes sem modificar código
- **Documentado**: Docstrings explicam cada função
- **Testável**: Módulos podem ser testados isoladamente

## 🚀 Próximos Passos Sugeridos

1. Adicionar testes unitários
2. Implementar logging estruturado
3. Adicionar validação de dados
4. Criar pipeline de CI/CD
5. Adicionar análise preditiva
6. Implementar cache de resultados
7. Criar API REST para acesso aos dados

---

**Projeto desenvolvido seguindo as melhores práticas de engenharia de software e ciência de dados.**


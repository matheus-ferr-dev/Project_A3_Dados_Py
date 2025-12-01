# Análise de Dados - Olist E-commerce

Projeto profissional de análise de dados do e-commerce Olist, desenvolvido seguindo boas práticas de arquitetura de software e ciência de dados.

## 📋 Sobre o Projeto

Este projeto realiza uma análise completa dos dados de vendas, clientes, produtos e vendedores da Olist, fornecendo insights estratégicos através de visualizações e métricas de negócio.

## 🏗️ Estrutura do Projeto

```
Projeto_A3/
├── config/                 # Configurações do projeto
│   └── settings.py         # Configurações centralizadas
├── DataSet/                # Dados brutos (CSV)
│   ├── olist_customers_dataset.csv
│   ├── olist_orders_dataset.csv
│   ├── olist_order_items_dataset.csv
│   ├── olist_products_dataset.csv
│   └── olist_sellers_dataset.csv
├── src/                    # Código fonte
│   ├── data/              # Processamento de dados
│   │   └── data_processor.py
│   ├── analysis/          # Análises específicas
│   │   ├── metrics.py
│   │   ├── temporal.py
│   │   ├── customers.py
│   │   ├── sellers.py
│   │   └── products.py
│   ├── visualization/     # Visualizações
│   │   └── charts.py
│   └── utils/             # Utilitários
│       ├── data_loader.py
│       └── visualization.py
├── outputs/               # Resultados gerados
│   ├── figures/          # Gráficos e visualizações
│   └── reports/           # Relatórios em texto
├── main.py               # Script principal
├── requirements.txt       # Dependências
└── README.md             # Este arquivo
```

## 🚀 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos

1. Clone ou baixe o repositório

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Certifique-se de que os arquivos CSV estão na pasta `DataSet/`

## 📊 Uso

### Executar Análise Completa

Execute o script principal para gerar todas as análises e visualizações:

```bash
python main.py
```

### Executar Análises Específicas

Você também pode executar análises individuais:

```python
from src.data.data_processor import create_main_dataframe
from src.analysis.metrics import calculate_main_metrics

# Carregar dados
df = create_main_dataframe()

# Calcular métricas
metrics = calculate_main_metrics(df)
print(metrics)
```

## 📈 Funcionalidades

### Análises Implementadas

1. **Métricas Principais**
   - Total de pedidos, receita, ticket médio
   - Base de clientes e vendedores
   - Taxa de recompra

2. **Análise Temporal**
   - Evolução de pedidos ao longo do tempo
   - Evolução de receita mensal
   - Identificação de tendências e sazonalidade

3. **Análise de Clientes**
   - Top 10 cidades e estados com mais clientes
   - Análise de recompra
   - Distribuição geográfica

4. **Análise de Vendedores**
   - Top 10 vendedores por vendas e receita
   - Distribuição geográfica de vendedores
   - Performance por estado

5. **Análise de Produtos**
   - Top 10 categorias mais vendidas
   - Ticket médio por categoria
   - Análise de frete por categoria

6. **Visualizações**
   - Gráficos de linha (evolução temporal)
   - Gráficos de barras (rankings)
   - Boxplots (distribuições)
   - Dashboards executivos

## 📁 Outputs

Todos os resultados são salvos na pasta `outputs/`:

- **figures/**: Gráficos em alta resolução (PNG, 300 DPI)
- **reports/**: Relatórios em texto com insights

## 🛠️ Tecnologias Utilizadas

- **pandas**: Manipulação e análise de dados
- **numpy**: Cálculos numéricos
- **matplotlib**: Visualizações básicas
- **seaborn**: Visualizações estatísticas avançadas

## 📝 Estrutura de Código

O projeto segue os princípios de:

- **Modularidade**: Código organizado em módulos reutilizáveis
- **Separação de responsabilidades**: Cada módulo tem uma função específica
- **Configuração centralizada**: Todas as configurações em `config/settings.py`
- **Reutilização**: Funções utilitárias para operações comuns

## 🔧 Configuração

As configurações do projeto podem ser ajustadas em `config/settings.py`:

- Diretórios de dados e outputs
- Configurações de visualização
- Configurações do pandas

## 📊 Exemplos de Uso

### Carregar Dados

```python
from src.utils.data_loader import load_all_datasets

datasets = load_all_datasets()
orders = datasets['orders']
```

### Criar DataFrame Consolidado

```python
from src.data.data_processor import create_main_dataframe

df = create_main_dataframe()
```

### Calcular Métricas

```python
from src.analysis.metrics import calculate_main_metrics

metrics = calculate_main_metrics(df)
print(f"Total de pedidos: {metrics['total_pedidos']:,}")
print(f"Receita total: R$ {metrics['receita_total']:,.2f}")
```

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais como parte do projeto A3 da disciplina de Dados.

## 👤 Autores

Marcos Natiel da Silva Pardim - 4251924809
Isadora Ribeiro Eugênio - 42322274
Victor Hugo Rodrigues Alves - 42421886
Matheus da Silva Ferreira - 4231924502
Vinicius Pereira Paiva - 4231923132
Letícia Ferreira Pinto - 4251925677
Kethlen Nunes de Carvalho - 4251920401





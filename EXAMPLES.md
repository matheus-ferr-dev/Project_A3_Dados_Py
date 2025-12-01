# Exemplos de Uso

Este documento contém exemplos práticos de como usar os módulos do projeto.

## Exemplo 1: Carregar Dados

```python
from src.utils.data_loader import load_csv, load_all_datasets

# Carregar um dataset específico
customers = load_csv('customers')
print(customers.head())

# Carregar todos os datasets
datasets = load_all_datasets()
orders = datasets['orders']
```

## Exemplo 2: Criar DataFrame Consolidado

```python
from src.data.data_processor import create_main_dataframe

# Criar DataFrame principal com todos os merges
df = create_main_dataframe()
print(f"Shape: {df.shape}")
print(df.columns.tolist())
```

## Exemplo 3: Calcular Métricas

```python
from src.data.data_processor import create_main_dataframe
from src.analysis.metrics import calculate_main_metrics

# Carregar dados
df = create_main_dataframe()

# Calcular métricas
metrics = calculate_main_metrics(df)

print(f"Total de pedidos: {metrics['total_pedidos']:,}")
print(f"Receita total: R$ {metrics['receita_total']:,.2f}")
print(f"Ticket médio: R$ {metrics['ticket_medio']:,.2f}")
```

## Exemplo 4: Análise Temporal

```python
from src.data.data_processor import create_main_dataframe, prepare_temporal_data
from src.analysis.temporal import analyze_temporal_evolution

# Preparar dados
df = create_main_dataframe()
df = prepare_temporal_data(df)

# Análise temporal
temporal = analyze_temporal_evolution(df)

# Ver evolução de pedidos
if 'pedidos_por_mes' in temporal:
    print(temporal['pedidos_por_mes'])
```

## Exemplo 5: Análise de Clientes

```python
from src.data.data_processor import create_main_dataframe
from src.analysis.customers import analyze_customers

df = create_main_dataframe()
customers_analysis = analyze_customers(df)

# Top 10 estados
if 'top_estados' in customers_analysis:
    print(customers_analysis['top_estados'])
```

## Exemplo 6: Análise de Vendedores

```python
from src.data.data_processor import create_main_dataframe
from src.analysis.sellers import analyze_sellers

df = create_main_dataframe()
sellers_analysis = analyze_sellers(df)

# Top 10 vendedores por receita
if 'top_vendedores_receita' in sellers_analysis:
    print(sellers_analysis['top_vendedores_receita'].head())
```

## Exemplo 7: Análise de Produtos

```python
from src.data.data_processor import create_main_dataframe
from src.analysis.products import analyze_products

df = create_main_dataframe()
products_analysis = analyze_products(df)

# Top 10 categorias
if 'top_categorias_vendas' in products_analysis:
    print(products_analysis['top_categorias_vendas'])
```

## Exemplo 8: Criar Visualização Personalizada

```python
import matplotlib.pyplot as plt
import seaborn as sns
from src.utils.visualization import setup_visualization, save_figure
from src.data.data_processor import create_main_dataframe

# Configurar visualização
setup_visualization()

# Carregar dados
df = create_main_dataframe()

# Criar gráfico
plt.figure(figsize=(12, 6))
# ... seu código de visualização ...
plt.title('Meu Gráfico Personalizado')
plt.tight_layout()

# Salvar
save_figure('meu_grafico.png')
plt.close()
```

## Exemplo 9: Script Completo Personalizado

```python
"""
Exemplo de script personalizado
"""

from src.data.data_processor import create_main_dataframe
from src.analysis.metrics import calculate_main_metrics
from src.analysis.customers import analyze_customers
import matplotlib.pyplot as plt
from src.utils.visualization import setup_visualization, save_figure

def minha_analise():
    # Configurar
    setup_visualization()
    
    # Carregar dados
    df = create_main_dataframe()
    
    # Calcular métricas
    metrics = calculate_main_metrics(df)
    
    # Análise específica
    customers = analyze_customers(df)
    
    # Visualização
    if 'top_estados' in customers:
        plt.figure(figsize=(10, 6))
        top_estados = customers['top_estados'].head(10)
        plt.bar(top_estados.index, top_estados.values)
        plt.title('Top 10 Estados')
        plt.tight_layout()
        save_figure('top_estados.png')
        plt.close()
    
    return metrics, customers

if __name__ == "__main__":
    metrics, customers = minha_analise()
    print("Análise concluída!")
```

## Exemplo 10: Usar Configurações

```python
from config.settings import (
    DATA_DIR, FIGURES_DIR, REPORTS_DIR,
    CSV_FILES, VISUALIZATION_CONFIG
)

# Acessar configurações
print(f"Dados em: {DATA_DIR}")
print(f"Figuras em: {FIGURES_DIR}")
print(f"Relatórios em: {REPORTS_DIR}")

# Ver configurações de arquivos
print(CSV_FILES.keys())

# Ver configurações de visualização
print(VISUALIZATION_CONFIG['color_palettes'])
```


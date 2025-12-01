"""
Configurações do Projeto - Análise de Dados Olist
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

DATA_DIR = PROJECT_ROOT / 'DataSet'
OUTPUTS_DIR = PROJECT_ROOT / 'outputs'
FIGURES_DIR = OUTPUTS_DIR / 'figures'
REPORTS_DIR = OUTPUTS_DIR / 'reports'

FIGURES_DIR.mkdir(parents=True, exist_ok=True)
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

CSV_FILES = {
    'customers': {
        'standard': 'olist_customers_dataset.csv',
        'alternative': 'olist_customers(Clientes)_dataset.csv'
    },
    'orders': {
        'standard': 'olist_orders_dataset.csv',
        'alternative': 'olist_orders(Pedidos)_dataset.csv'
    },
    'order_items': {
        'standard': 'olist_order_items_dataset.csv',
        'alternative': 'olist_order_items(itens_pedido)_dataset.csv'
    },
    'products': {
        'standard': 'olist_products_dataset.csv',
        'alternative': 'olist_products(Produtos)_dataset.csv'
    },
    'sellers': {
        'standard': 'olist_sellers_dataset.csv',
        'alternative': 'olist_sellers(Vendedores)_dataset.csv'
    }
}

VISUALIZATION_CONFIG = {
    'style': 'whitegrid',
    'figure_size': (14, 8),
    'font_size': 10,
    'dpi': 300,
    'color_palettes': {
        'primary': 'viridis',
        'secondary': 'coolwarm',
        'tertiary': 'mako',
        'categorical': 'Set2'
    }
}

PANDAS_CONFIG = {
    'display_max_columns': None,
    'display_max_rows': 100,
    'display_width': None,
    'display_max_colwidth': 50
}

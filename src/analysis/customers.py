"""
Análise de Clientes
"""

import pandas as pd
from typing import Dict


def analyze_customers(df: pd.DataFrame) -> Dict:
    """
    Analisa dados de clientes.
    
    Args:
        df: DataFrame principal
    
    Returns:
        Dicionário com análises de clientes
    """
    results = {}
    
    if 'customer_city' in df.columns:
        top_cidades = df.groupby('customer_city')['customer_unique_id'].nunique().sort_values(ascending=False).head(10)
        results['top_cidades'] = top_cidades
    
    if 'customer_state' in df.columns:
        top_estados = df.groupby('customer_state')['customer_unique_id'].nunique().sort_values(ascending=False).head(10)
        results['top_estados'] = top_estados
    
    if 'customer_unique_id' in df.columns:
        pedidos_cliente = df.groupby('customer_unique_id')['order_id'].nunique()
        results['distribuicao_pedidos'] = pedidos_cliente.value_counts().sort_index()
        results['clientes_recompra'] = len(pedidos_cliente[pedidos_cliente > 1])
        results['total_clientes'] = len(pedidos_cliente)
    
    return results

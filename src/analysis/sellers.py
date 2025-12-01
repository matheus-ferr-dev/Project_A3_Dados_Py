"""
Análise de Vendedores
"""

import pandas as pd
from typing import Dict


def analyze_sellers(df: pd.DataFrame) -> Dict:
    """
    Analisa dados de vendedores.
    
    Args:
        df: DataFrame principal
    
    Returns:
        Dicionário com análises de vendedores
    """
    results = {}
    
    vendas_vendedor = df.groupby('seller_id').agg({
        'order_id': 'count',
        'order_item_id': 'nunique'
    }).reset_index()
    vendas_vendedor.columns = ['seller_id', 'numero_vendas', 'numero_pedidos']
    vendas_vendedor = vendas_vendedor.sort_values('numero_vendas', ascending=False)
    results['top_vendedores_vendas'] = vendas_vendedor.head(10)
    
    if 'receita_total' in df.columns:
        receita_vendedor = df.groupby('seller_id')['receita_total'].sum().reset_index()
        receita_vendedor = receita_vendedor.sort_values('receita_total', ascending=False)
        results['top_vendedores_receita'] = receita_vendedor.head(10)
    
    if 'seller_state' in df.columns:
        estados_vendedores = df.groupby('seller_state')['seller_id'].nunique().sort_values(ascending=False)
        results['vendedores_por_estado'] = estados_vendedores
    
    return results

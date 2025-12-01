"""
Análise de Produtos
"""

import pandas as pd
from typing import Dict


def analyze_products(df: pd.DataFrame) -> Dict:
    """
    Analisa dados de produtos.
    
    Args:
        df: DataFrame principal
    
    Returns:
        Dicionário com análises de produtos
    """
    results = {}
    
    coluna_categoria = _find_category_column(df)
    if not coluna_categoria:
        return results
    
    top_categorias = df.groupby(coluna_categoria)['order_id'].count().sort_values(ascending=False).head(10)
    results['top_categorias_vendas'] = top_categorias
    
    if 'receita_total' in df.columns:
        ticket_categoria = df.groupby(coluna_categoria).agg({
            'receita_total': 'mean',
            'order_id': 'count'
        }).reset_index()
        ticket_categoria.columns = ['categoria', 'ticket_medio', 'vendas']
        ticket_categoria = ticket_categoria[ticket_categoria['vendas'] >= 100]
        ticket_categoria = ticket_categoria.nlargest(10, 'ticket_medio')
        results['top_categorias_ticket'] = ticket_categoria
    
    coluna_frete = _find_freight_column(df)
    if coluna_frete:
        frete_categoria = df.groupby(coluna_categoria).agg({
            coluna_frete: ['mean', 'sum', 'count']
        }).reset_index()
        frete_categoria.columns = ['categoria', 'frete_medio', 'frete_total', 'vendas']
        frete_categoria = frete_categoria.sort_values('frete_medio', ascending=False)
        results['top_categorias_frete'] = frete_categoria.head(10)
    
    return results


def _find_category_column(df: pd.DataFrame) -> str:
    """Encontra coluna de categoria."""
    for col in df.columns:
        if 'category' in col.lower() and 'name' in col.lower():
            return col
    return None


def _find_freight_column(df: pd.DataFrame) -> str:
    """Encontra coluna de frete."""
    for col in df.columns:
        if 'freight' in col.lower():
            return col
    return None

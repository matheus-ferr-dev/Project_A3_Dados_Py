"""
Cálculo de Métricas Principais
"""

import pandas as pd
from typing import Dict


def calculate_main_metrics(df: pd.DataFrame) -> Dict:
    """
    Calcula as métricas principais do negócio.
    
    Args:
        df: DataFrame principal consolidado
    
    Returns:
        Dicionário com todas as métricas calculadas
    """
    metrics = {}
    
    metrics['total_pedidos'] = df['order_id'].nunique()
    metrics['total_clientes'] = _get_unique_customers(df)
    metrics['total_vendedores'] = df['seller_id'].nunique()
    metrics['total_produtos'] = df['product_id'].nunique()
    
    if 'receita_total' in df.columns:
        metrics['receita_total'] = df['receita_total'].sum()
        metrics['ticket_medio'] = metrics['receita_total'] / metrics['total_pedidos'] if metrics['total_pedidos'] > 0 else 0
    else:
        metrics['receita_total'] = 0
        metrics['ticket_medio'] = 0
    
    if 'customer_unique_id' in df.columns:
        pedidos_por_cliente = df.groupby('customer_unique_id')['order_id'].nunique()
        metrics['clientes_recompra'] = len(pedidos_por_cliente[pedidos_por_cliente > 1])
        metrics['taxa_recompra'] = (metrics['clientes_recompra'] / metrics['total_clientes']) * 100 if metrics['total_clientes'] > 0 else 0
    else:
        metrics['clientes_recompra'] = 0
        metrics['taxa_recompra'] = 0
    
    timestamp_col = _find_timestamp_column(df)
    if timestamp_col and pd.api.types.is_datetime64_any_dtype(df[timestamp_col]):
        metrics['data_inicio'] = df[timestamp_col].min()
        metrics['data_fim'] = df[timestamp_col].max()
        metrics['periodo_dias'] = (metrics['data_fim'] - metrics['data_inicio']).days
    else:
        metrics['data_inicio'] = None
        metrics['data_fim'] = None
        metrics['periodo_dias'] = 0
    
    return metrics


def _get_unique_customers(df: pd.DataFrame) -> int:
    """Retorna número de clientes únicos."""
    if 'customer_unique_id' in df.columns:
        return df['customer_unique_id'].nunique()
    return df['customer_id'].nunique()


def _find_timestamp_column(df: pd.DataFrame) -> str:
    """Encontra coluna de timestamp."""
    for col in df.columns:
        if 'purchase' in col.lower() and 'timestamp' in col.lower():
            return col
    return None

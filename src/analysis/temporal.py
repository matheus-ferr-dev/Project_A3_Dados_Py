"""
Análise Temporal
"""

import pandas as pd
from typing import Dict


def analyze_temporal_evolution(df: pd.DataFrame) -> Dict:
    """
    Analisa a evolução temporal de pedidos e receita.
    
    Args:
        df: DataFrame principal
    
    Returns:
        Dicionário com análises temporais
    """
    results = {}
    
    if 'ano_mes_str' not in df.columns:
        return results
    
    pedidos_mes = df.groupby('ano_mes_str')['order_id'].nunique().reset_index()
    pedidos_mes.columns = ['periodo', 'pedidos']
    pedidos_mes = pedidos_mes.sort_values('periodo')
    pedidos_mes['crescimento'] = pedidos_mes['pedidos'].pct_change() * 100
    
    results['pedidos_por_mes'] = pedidos_mes
    results['mes_maior_volume'] = pedidos_mes.loc[pedidos_mes['pedidos'].idxmax()]
    results['mes_menor_volume'] = pedidos_mes.loc[pedidos_mes['pedidos'].idxmin()]
    
    if 'receita_total' in df.columns:
        receita_mes = df.groupby('ano_mes_str')['receita_total'].sum().reset_index()
        receita_mes.columns = ['periodo', 'receita']
        receita_mes = receita_mes.sort_values('periodo')
        receita_mes['crescimento'] = receita_mes['receita'].pct_change() * 100
        receita_mes['ticket_medio'] = receita_mes['receita'] / pedidos_mes['pedidos']
        
        results['receita_por_mes'] = receita_mes
        results['mes_maior_receita'] = receita_mes.loc[receita_mes['receita'].idxmax()]
        results['mes_menor_receita'] = receita_mes.loc[receita_mes['receita'].idxmin()]
    
    return results

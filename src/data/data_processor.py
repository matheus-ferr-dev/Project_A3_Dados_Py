"""
Processamento e Consolidação de Dados
"""

import pandas as pd
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent.parent))

from src.utils.data_loader import load_all_datasets


def create_main_dataframe() -> pd.DataFrame:
    """
    Cria o DataFrame principal consolidando todas as tabelas.
    
    Schema de merge:
    - orders + customers (por customer_id)
    - resultado + order_items (por order_id)
    - resultado + products (por product_id)
    - resultado + sellers (por seller_id)
    
    Returns:
        DataFrame consolidado
    """
    print("Carregando datasets...")
    datasets = load_all_datasets()
    
    print("\nRealizando merges...")
    
    df = datasets['orders'].merge(
        datasets['customers'],
        on='customer_id',
        how='inner',
        suffixes=('', '_customer')
    )
    
    df = df.merge(
        datasets['order_items'],
        on='order_id',
        how='inner',
        suffixes=('', '_item')
    )
    
    df = df.merge(
        datasets['products'],
        on='product_id',
        how='left',
        suffixes=('', '_product')
    )
    
    df = df.merge(
        datasets['sellers'],
        on='seller_id',
        how='left',
        suffixes=('', '_seller')
    )
    
    df = df.loc[:, ~df.columns.duplicated()]
    _process_columns(df)
    
    print(f"✓ DataFrame consolidado: {df.shape[0]:,} linhas × {df.shape[1]} colunas")
    
    return df


def _process_columns(df: pd.DataFrame):
    """Processa colunas importantes do DataFrame (modificado in-place)."""
    coluna_preco = _find_column(df, 'price', exclude='freight')
    coluna_frete = _find_column(df, 'freight')
    coluna_timestamp = _find_column(df, 'purchase', 'timestamp')
    coluna_categoria = _find_column(df, 'category', 'name')
    
    if coluna_preco:
        if coluna_frete:
            df['receita_total'] = df[coluna_preco] + df[coluna_frete]
        else:
            df['receita_total'] = df[coluna_preco]
    
    if coluna_timestamp:
        df[coluna_timestamp] = pd.to_datetime(df[coluna_timestamp], errors='coerce')
        df['ano_mes'] = df[coluna_timestamp].dt.to_period('M')
        df['ano_mes_str'] = df[coluna_timestamp].dt.strftime('%Y-%m')
    
    if coluna_categoria:
        df[coluna_categoria] = df[coluna_categoria].fillna('Sem Categoria')


def _find_column(df: pd.DataFrame, *keywords, exclude: str = None) -> str:
    """Encontra coluna por palavras-chave."""
    for col in df.columns:
        col_lower = col.lower()
        if all(kw.lower() in col_lower for kw in keywords):
            if exclude is None or exclude.lower() not in col_lower:
                return col
    return None


def prepare_temporal_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepara dados para análise temporal.
    
    Args:
        df: DataFrame principal
    
    Returns:
        DataFrame preparado para análise temporal
    """
    coluna_timestamp = _find_column(df, 'purchase', 'timestamp')
    
    if coluna_timestamp and not pd.api.types.is_datetime64_any_dtype(df[coluna_timestamp]):
        df[coluna_timestamp] = pd.to_datetime(df[coluna_timestamp], errors='coerce')
    
    if coluna_timestamp:
        if 'ano_mes' not in df.columns:
            df['ano_mes'] = df[coluna_timestamp].dt.to_period('M')
        if 'ano_mes_str' not in df.columns:
            df['ano_mes_str'] = df[coluna_timestamp].dt.strftime('%Y-%m')
    
    return df

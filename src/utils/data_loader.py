"""
Utilitários para Carregamento de Dados
"""

import pandas as pd
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent.parent))

from config.settings import DATA_DIR, CSV_FILES


def load_csv(dataset_name: str) -> pd.DataFrame:
    """
    Carrega um arquivo CSV do dataset.
    
    Args:
        dataset_name: Nome do dataset ('customers', 'orders', 'order_items', 'products', 'sellers')
    
    Returns:
        DataFrame com os dados carregados
    
    Raises:
        FileNotFoundError: Se o arquivo não for encontrado
    """
    if dataset_name not in CSV_FILES:
        available = list(CSV_FILES.keys())
        raise ValueError(f"Dataset '{dataset_name}' não encontrado. Opções: {available}")
    
    file_config = CSV_FILES[dataset_name]
    standard_path = DATA_DIR / file_config['standard']
    alternative_path = DATA_DIR / file_config['alternative']
    
    if standard_path.exists():
        return pd.read_csv(standard_path)
    elif alternative_path.exists():
        return pd.read_csv(alternative_path)
    else:
        raise FileNotFoundError(
            f"Arquivo não encontrado para '{dataset_name}'. "
            f"Procurado em: {standard_path} ou {alternative_path}"
        )


def load_all_datasets() -> dict:
    """
    Carrega todos os datasets disponíveis.
    
    Returns:
        Dicionário com todos os DataFrames carregados
    """
    datasets = {}
    
    for dataset_name in CSV_FILES.keys():
        try:
            datasets[dataset_name] = load_csv(dataset_name)
            print(f"✓ {dataset_name} carregado: {datasets[dataset_name].shape}")
        except FileNotFoundError as e:
            print(f"✗ Erro ao carregar {dataset_name}: {e}")
    
    return datasets

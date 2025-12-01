"""
Utilitários para Visualização
"""

import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent.parent))

from config.settings import VISUALIZATION_CONFIG, FIGURES_DIR


def setup_visualization():
    """Configura o ambiente de visualização com as configurações padrão."""
    sns.set_style(VISUALIZATION_CONFIG['style'])
    
    plt.rcParams['figure.figsize'] = VISUALIZATION_CONFIG['figure_size']
    plt.rcParams['font.size'] = VISUALIZATION_CONFIG['font_size']
    plt.rcParams['axes.labelsize'] = VISUALIZATION_CONFIG['font_size'] + 1
    plt.rcParams['axes.titlesize'] = VISUALIZATION_CONFIG['font_size'] + 4
    plt.rcParams['xtick.labelsize'] = VISUALIZATION_CONFIG['font_size'] - 1
    plt.rcParams['ytick.labelsize'] = VISUALIZATION_CONFIG['font_size'] - 1


def save_figure(filename: str, dpi: int = None, bbox_inches: str = 'tight'):
    """
    Salva uma figura no diretório de figuras.
    
    Args:
        filename: Nome do arquivo (será salvo em outputs/figures/)
        dpi: Resolução (usa o padrão se None)
        bbox_inches: Configuração de bbox_inches
    """
    if dpi is None:
        dpi = VISUALIZATION_CONFIG['dpi']
    
    filepath = FIGURES_DIR / filename
    plt.savefig(filepath, dpi=dpi, bbox_inches=bbox_inches)
    print(f"✓ Figura salva: {filepath}")

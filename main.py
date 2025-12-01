"""
Script Principal - Análise de Dados Olist
"""

import sys
from pathlib import Path
from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from config.settings import PANDAS_CONFIG, FIGURES_DIR, REPORTS_DIR
from src.utils.visualization import setup_visualization, save_figure
from src.data.data_processor import create_main_dataframe, prepare_temporal_data
from src.analysis.metrics import calculate_main_metrics
from src.analysis.temporal import analyze_temporal_evolution
from src.analysis.customers import analyze_customers
from src.analysis.sellers import analyze_sellers
from src.analysis.products import analyze_products

PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))


def configure_environment():
    """Configura o ambiente do projeto."""
    for key, value in PANDAS_CONFIG.items():
        pd.set_option(key, value)
    setup_visualization()
    
    print("=" * 80)
    print("ANÁLISE DE DADOS OLIST - SISTEMA DE ANÁLISE")
    print("=" * 80)
    print(f"Data de execução: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")


def main():
    """Orquestra todas as análises e gera visualizações."""
    configure_environment()
    
    print("ETAPA 1: Carregamento e Consolidação de Dados")
    print("-" * 80)
    df = create_main_dataframe()
    df = prepare_temporal_data(df)
    
    print("\nETAPA 2: Cálculo de Métricas Principais")
    print("-" * 80)
    metrics = calculate_main_metrics(df)
    
    print(f"\n📊 Métricas Principais:")
    print(f"  • Total de Pedidos: {metrics['total_pedidos']:,}")
    print(f"  • Total de Clientes: {metrics['total_clientes']:,}")
    print(f"  • Total de Vendedores: {metrics['total_vendedores']:,}")
    print(f"  • Receita Total: R$ {metrics['receita_total']:,.2f}")
    print(f"  • Ticket Médio: R$ {metrics['ticket_medio']:,.2f}")
    print(f"  • Taxa de Recompra: {metrics['taxa_recompra']:.2f}%")
    
    print("\nETAPA 3: Análises Específicas")
    print("-" * 80)
    
    print("  • Análise Temporal...")
    temporal_analysis = analyze_temporal_evolution(df)
    
    print("  • Análise de Clientes...")
    customers_analysis = analyze_customers(df)
    
    print("  • Análise de Vendedores...")
    sellers_analysis = analyze_sellers(df)
    
    print("  • Análise de Produtos...")
    products_analysis = analyze_products(df)
    
    print("\nETAPA 4: Geração de Visualizações")
    print("-" * 80)
    generate_visualizations(df, metrics, temporal_analysis, 
                           customers_analysis, sellers_analysis, products_analysis)
    
    print("\n" + "=" * 80)
    print("ANÁLISE CONCLUÍDA COM SUCESSO!")
    print("=" * 80)
    print(f"\nResultados salvos em:")
    print(f"  • Figuras: {FIGURES_DIR}")
    print(f"  • Relatórios: {REPORTS_DIR}")


def generate_visualizations(df, metrics, temporal, customers, sellers, products):
    """Gera todas as visualizações."""
    create_metrics_cards(metrics)
    
    if 'pedidos_por_mes' in temporal:
        create_temporal_charts(temporal)
    
    if 'top_estados' in customers:
        create_customer_charts(customers)
    
    if 'top_vendedores_receita' in sellers:
        create_seller_charts(sellers)
    
    if 'top_categorias_vendas' in products:
        create_product_charts(products)


def create_metrics_cards(metrics):
    """Cria cards com métricas principais."""
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle('Métricas Principais - Dashboard Olist', 
                 fontsize=20, fontweight='bold', y=0.98)
    
    cards = [
        (f"{metrics['total_pedidos']:,}", 'Total de Pedidos', '#2E86AB'),
        (f"R$ {metrics['receita_total']/1e6:.2f}M", 'Receita Total', '#A23B72'),
        (f"R$ {metrics['ticket_medio']:,.2f}", 'Ticket Médio', '#F18F01'),
        (f"{metrics['total_clientes']:,}", 'Total de Clientes', '#06A77D'),
        (f"{metrics['taxa_recompra']:.1f}%", 'Taxa de Recompra', '#C73E1D'),
        (f"{metrics['total_vendedores']:,}", 'Total de Vendedores', '#6C5CE7')
    ]
    
    for i, (valor, titulo, cor) in enumerate(cards):
        ax = axes[i // 3, i % 3]
        ax.axis('off')
        ax.text(0.5, 0.7, valor, ha='center', va='center', 
                fontsize=32, fontweight='bold', color=cor)
        ax.text(0.5, 0.4, titulo, ha='center', va='center', 
                fontsize=14, color='#666666')
        ax.add_patch(plt.Rectangle((0.05, 0.05), 0.9, 0.9, fill=False, 
                                   edgecolor=cor, linewidth=2))
    
    plt.tight_layout()
    save_figure('01_metricas_principais.png')
    plt.close()


def create_temporal_charts(temporal):
    """Cria gráficos temporais."""
    if 'pedidos_por_mes' in temporal:
        plt.figure(figsize=(14, 6))
        pedidos = temporal['pedidos_por_mes']
        plt.plot(pedidos['periodo'], pedidos['pedidos'], 
                marker='o', linewidth=2.5, markersize=8, color='#2E86AB')
        plt.title('Evolução Temporal de Pedidos', fontsize=16, fontweight='bold', pad=15)
        plt.xlabel('Período (Ano-Mês)', fontsize=12)
        plt.ylabel('Número de Pedidos', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        save_figure('02_evolucao_pedidos.png')
        plt.close()
    
    if 'receita_por_mes' in temporal:
        plt.figure(figsize=(14, 6))
        receita = temporal['receita_por_mes']
        plt.plot(receita['periodo'], receita['receita'], 
                marker='s', linewidth=2.5, markersize=8, color='#A23B72')
        plt.title('Evolução Temporal de Receita', fontsize=16, fontweight='bold', pad=15)
        plt.xlabel('Período (Ano-Mês)', fontsize=12)
        plt.ylabel('Receita Total (R$)', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        ax = plt.gca()
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'R$ {x/1e6:.1f}M'))
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        save_figure('03_evolucao_receita.png')
        plt.close()


def create_customer_charts(customers):
    """Cria gráficos de análise de clientes."""
    if 'top_estados' in customers:
        plt.figure(figsize=(12, 6))
        top_estados = customers['top_estados'].head(10)
        sns.barplot(x=top_estados.index, y=top_estados.values, palette='coolwarm')
        plt.title('Top 10 Estados com Mais Clientes', fontsize=16, fontweight='bold', pad=15)
        plt.xlabel('Estado', fontsize=12)
        plt.ylabel('Número de Clientes', fontsize=12)
        for i, v in enumerate(top_estados.values):
            plt.text(i, v + max(top_estados.values) * 0.01, f'{v:,}', 
                    ha='center', fontsize=9, fontweight='bold')
        plt.tight_layout()
        save_figure('04_top10_estados_clientes.png')
        plt.close()


def create_seller_charts(sellers):
    """Cria gráficos de análise de vendedores."""
    if 'top_vendedores_receita' in sellers:
        plt.figure(figsize=(12, 8))
        top_vend = sellers['top_vendedores_receita'].head(10)
        top_vend['seller_short'] = top_vend['seller_id'].str[:15] + '...'
        sns.barplot(y=top_vend['seller_short'], x=top_vend['receita_total'], palette='mako')
        plt.title('Top 10 Vendedores por Receita Total', fontsize=16, fontweight='bold', pad=15)
        plt.xlabel('Receita Total (R$)', fontsize=12)
        plt.ylabel('Vendedor', fontsize=12)
        ax = plt.gca()
        ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'R$ {x/1000:.0f}K'))
        plt.tight_layout()
        save_figure('05_top10_vendedores_receita.png')
        plt.close()


def create_product_charts(products):
    """Cria gráficos de análise de produtos."""
    if 'top_categorias_vendas' in products:
        plt.figure(figsize=(12, 8))
        top_cat = products['top_categorias_vendas'].head(10)
        sns.barplot(y=top_cat.index, x=top_cat.values, palette='viridis')
        plt.title('Top 10 Categorias Mais Vendidas', fontsize=16, fontweight='bold', pad=15)
        plt.xlabel('Número de Vendas', fontsize=12)
        plt.ylabel('Categoria', fontsize=12)
        for i, v in enumerate(top_cat.values):
            plt.text(v + max(top_cat.values) * 0.01, i, f'{v:,}', 
                    va='center', fontsize=9, fontweight='bold')
        plt.tight_layout()
        save_figure('06_top10_categorias.png')
        plt.close()


if __name__ == "__main__":
    main()

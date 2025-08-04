import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
import matplotlib as mpl

# Estilo mais limpo e moderno
plt.style.use('seaborn-v0_8-whitegrid')  # seaborn estilo mais bonito
mpl.rcParams['font.size'] = 12
mpl.rcParams['axes.titlesize'] = 14
mpl.rcParams['axes.labelsize'] = 12

# Carrega o arquivo Excel
df = pd.read_excel('dados.xlsx')

# Define os intervalos
cananeia_df = df.iloc[1:16].copy()
florianopolis_df = df.iloc[16:46].copy()

# Colunas dos elementos
element_columns = df.columns[1:]

# Cores fixas
colors = ['#4C72B0', '#DD8452']  # Azul e laranja

for col_name in element_columns:
    print(f"Processando elemento: {col_name}")

    cananeia_data = cananeia_df[col_name].astype(str).str.replace(',', '.', regex=False)
    florianopolis_data = florianopolis_df[col_name].astype(str).str.replace(',', '.', regex=False)

    cananeia_data_numeric = pd.to_numeric(cananeia_data, errors='coerce').dropna()
    florianopolis_data_numeric = pd.to_numeric(florianopolis_data, errors='coerce').dropna()

    if cananeia_data_numeric.empty and florianopolis_data_numeric.empty:
        print(f"Pulando {col_name}: Sem dados válidos.")
        continue

    # Cria figura
    fig, ax = plt.subplots(figsize=(8, 6))

    box = ax.boxplot(
        [cananeia_data_numeric, florianopolis_data_numeric],
        patch_artist=True,
        labels=['Cananeia', 'Florianópolis'],
        medianprops=dict(color='black'),
        boxprops=dict(facecolor=colors[0], color=colors[0], linewidth=1.5),
        whiskerprops=dict(color=colors[0], linewidth=1.2),
        capprops=dict(color=colors[0], linewidth=1.2),
        flierprops=dict(marker='o', markerfacecolor='gray', markersize=5, alpha=0.5)
    )

    # Atualiza cor da segunda área
    for patch, color in zip(box['boxes'], colors):
        patch.set_facecolor(color)

    # Título e eixos
    ax.set_title(f'Concentração de {col_name}')
    ax.set_ylabel(f'{col_name} (unidade)')
    ax.set_xlabel('Área')
    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=6))
    ax.grid(True, linestyle='--', alpha=0.6)

    # Adiciona número de amostras
    n_can = len(cananeia_data_numeric)
    n_flo = len(florianopolis_data_numeric)
    ax.text(1, ax.get_ylim()[1]*0.95, f'n={n_can}', ha='center', fontsize=10, color=colors[0])
    ax.text(2, ax.get_ylim()[1]*0.95, f'n={n_flo}', ha='center', fontsize=10, color=colors[1])

    plt.tight_layout()

    # Salva o gráfico
    safe_col_name = col_name.replace(' ', '_').replace('%', 'pct').replace('(', '').replace(')', '').replace('/', '_').replace('µg', 'ug').replace('g-1', 'g_1')
    plt.savefig(f'boxplot_{safe_col_name}.png', dpi=300)
    plt.close()

print("\nTodos os box plots foram gerados!")

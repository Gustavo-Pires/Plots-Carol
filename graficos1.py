import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carrega o arquivo Excel
df = pd.read_excel('dados.xlsx', sheet_name='Planilha1')

# Define os intervalos de linhas para as áreas "Cananeia" e "Florianopolis".
# No DataFrame (que é 0-indexado), A2 a A16 corresponde aos índices 1 a 15.
cananeia_df = df.iloc[1:16].copy()
# A17 a A46 corresponde aos índices 16 a 45.
florianopolis_df = df.iloc[16:46].copy()

# Identifica as colunas dos elementos a serem plotados.
# As colunas de elementos começam do índice 1 (coluna B) até o final.
element_columns = df.columns[1:]

# Itera sobre cada coluna de elemento para gerar um box plot separado.
for col_name in element_columns:
    print(f"Processando elemento: {col_name}")

    # Extrai os dados para a área "Cananeia" e "Florianopolis" para o elemento atual.
    cananeia_data = cananeia_df[col_name].copy()
    florianopolis_data = florianopolis_df[col_name].copy()

    # Limpa e converte os dados para numérico.
    # Primeiro, substitui a vírgula por ponto para permitir a conversão numérica.
    cananeia_data = cananeia_data.astype(str).str.replace(',', '.', regex=False)
    florianopolis_data = florianopolis_data.astype(str).str.replace(',', '.', regex=False)

    # Converte os dados para tipo numérico, transformando quaisquer erros em NaN (Not a Number).
    cananeia_data_numeric = pd.to_numeric(cananeia_data, errors='coerce')
    florianopolis_data_numeric = pd.to_numeric(florianopolis_data, errors='coerce')

    # Remove os valores NaN antes de plotar, pois box plots não os representam.
    cananeia_data_numeric = cananeia_data_numeric.dropna()
    florianopolis_data_numeric = florianopolis_data_numeric.dropna()

    # Verifica se há dados numéricos válidos para plotar.
    if cananeia_data_numeric.empty and florianopolis_data_numeric.empty:
        print(f"Pulando {col_name}: Não há dados numéricos válidos para Cananeia ou Florianopolis.")
        continue # Pula para o próximo elemento se não houver dados.
    elif cananeia_data_numeric.empty:
        print(f"Aviso: Não há dados numéricos válidos para Cananeia em {col_name}.")
    elif florianopolis_data_numeric.empty:
        print(f"Aviso: Não há dados numéricos válidos para Florianopolis em {col_name}.")

    # Cria a figura e os eixos para o box plot.
    plt.figure(figsize=(8, 6)) # Define o tamanho da figura.
    
    # Gera o box plot. O primeiro argumento é uma lista de arrays ou séries de dados,
    # e o 'tick_labels' define os rótulos para cada box plot no gráfico (alteração aqui).
    plt.boxplot([cananeia_data_numeric, florianopolis_data_numeric], labels=['Cananeia', 'Florianopolis'])

    # Adiciona título e rótulos aos eixos do gráfico.
    plt.title(f'{col_name}')
    plt.ylabel(f'Concentração de {col_name}')
    plt.xlabel('Área')
    plt.grid(True) # Adiciona uma grade ao gráfico.
    plt.tight_layout() # Ajusta o layout para evitar sobreposição de elementos.

    # Sanitiza o nome da coluna para usar como nome de arquivo (remove caracteres inválidos).
    safe_col_name = col_name.replace(' ', '_').replace('%', 'pct').replace('(', '').replace(')', '').replace('/', '_').replace('µg', 'ug').replace('g-1', 'g_1')
    
    # Salva o gráfico como um arquivo PNG.
    plt.savefig(f'boxplot_{safe_col_name}.png', dpi=300)
    plt.close() # Fecha a figura para liberar memória e evitar sobreposição em plots futuros.

# Carrega o arquivo Excel
df = pd.read_excel('dados.xlsx', sheet_name='Planilha2')

# Define os intervalos de linhas para as áreas "Salinidade" e "Florianopolis".
# No DataFrame (que é 0-indexado), A2 a A16 corresponde aos índices 1 a 15.
Salinidade_df = df.iloc[1:19].copy()
# A17 a A46 corresponde aos índices 16 a 45.
florianopolis_df = df.iloc[19:37].copy()

# Identifica as colunas dos elementos a serem plotados.
# As colunas de elementos começam do índice 1 (coluna B) até o final.
element_columns = df.columns[1:]

# Itera sobre cada coluna de elemento para gerar um box plot separado.
for col_name in element_columns:
    print(f"Processando elemento: {col_name}")

    # Extrai os dados para a área "Salinidade" e "Florianopolis" para o elemento atual.
    Salinidade_data = Salinidade_df[col_name].copy()
    florianopolis_data = florianopolis_df[col_name].copy()

    # Limpa e converte os dados para numérico.
    # Primeiro, substitui a vírgula por ponto para permitir a conversão numérica.
    Salinidade_data = Salinidade_data.astype(str).str.replace(',', '.', regex=False)
    florianopolis_data = florianopolis_data.astype(str).str.replace(',', '.', regex=False)

    # Converte os dados para tipo numérico, transformando quaisquer erros em NaN (Not a Number).
    Salinidade_data_numeric = pd.to_numeric(Salinidade_data, errors='coerce')
    florianopolis_data_numeric = pd.to_numeric(florianopolis_data, errors='coerce')

    # Remove os valores NaN antes de plotar, pois box plots não os representam.
    Salinidade_data_numeric = Salinidade_data_numeric.dropna()
    florianopolis_data_numeric = florianopolis_data_numeric.dropna()

    # Verifica se há dados numéricos válidos para plotar.
    if Salinidade_data_numeric.empty and florianopolis_data_numeric.empty:
        print(f"Pulando {col_name}: Não há dados numéricos válidos para Salinidade ou Florianopolis.")
        continue # Pula para o próximo elemento se não houver dados.
    elif Salinidade_data_numeric.empty:
        print(f"Aviso: Não há dados numéricos válidos para Salinidade em {col_name}.")
    elif florianopolis_data_numeric.empty:
        print(f"Aviso: Não há dados numéricos válidos para Florianopolis em {col_name}.")

    # Cria a figura e os eixos para o box plot.
    plt.figure(figsize=(8, 6)) # Define o tamanho da figura.
    
    # Gera o box plot. O primeiro argumento é uma lista de arrays ou séries de dados,
    # e o 'tick_labels' define os rótulos para cada box plot no gráfico (alteração aqui).
    plt.boxplot([Salinidade_data_numeric, florianopolis_data_numeric], labels=['Salinidade', 'Florianopolis'])

    # Adiciona título e rótulos aos eixos do gráfico.
    plt.title(f'{col_name}')
    plt.ylabel(f'Concentração de {col_name}')
    plt.xlabel('Área')
    plt.grid(True) # Adiciona uma grade ao gráfico.
    plt.tight_layout() # Ajusta o layout para evitar sobreposição de elementos.

    # Sanitiza o nome da coluna para usar como nome de arquivo (remove caracteres inválidos).
    safe_col_name = col_name.replace(' ', '_').replace('%', 'pct').replace('(', '').replace(')', '').replace('/', '_').replace('µg', 'ug').replace('g-1', 'g_1')
    
    # Salva o gráfico como um arquivo PNG.
    plt.savefig(f'boxplot_{safe_col_name}.png', dpi=300)
    plt.close() # Fecha a figura para liberar memória e evitar sobreposição em plots futuros.


print("\nTodos os box plots foram gerados e salvos.")
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def sanitize_filename(name):
    return name.replace(' ', '_')\
               .replace('%', 'pct')\
               .replace('(', '')\
               .replace(')', '')\
               .replace('/', '_')\
               .replace('µg', 'ug')\
               .replace('g-1', 'g_1')

def clean_numeric_data(series):
    return pd.to_numeric(series.astype(str).str.replace(',', '.', regex=False), errors='coerce').dropna()

def gerar_boxplots(df, area1_range, area2_range, area1_label, area2_label):
    area1_df = df.iloc[area1_range[0]:area1_range[1]].copy()
    area2_df = df.iloc[area2_range[0]:area2_range[1]].copy()
    element_columns = df.columns[1:]

    for col_name in element_columns:
        print(f"Processando elemento: {col_name}")
        
        # Limpa e converte os dados
        data1 = clean_numeric_data(area1_df[col_name])
        data2 = clean_numeric_data(area2_df[col_name])

        if data1.empty and data2.empty:
            print(f"Pulando {col_name}: Não há dados numéricos válidos para {area1_label} ou {area2_label}.")
            continue
        elif data1.empty:
            print(f"Aviso: Não há dados numéricos válidos para {area1_label} em {col_name}.")
        elif data2.empty:
            print(f"Aviso: Não há dados numéricos válidos para {area2_label} em {col_name}.")

       # Plot
        plt.figure(figsize=(8, 6))
        plt.boxplot([data1, data2], tick_labels=[area1_label, area2_label])  # <- Aqui foi atualizado!
        plt.title(col_name)
        plt.ylabel(f'Concentração de {col_name}')
        plt.xlabel('Área')
        plt.grid(True)
        plt.tight_layout()

        # Salva
        safe_col_name = sanitize_filename(col_name)
        plt.savefig(f'boxplot_{safe_col_name}.png', dpi=300)
        plt.close()

# Processa a Planilha1: Cananeia vs Florianopolis
df1 = pd.read_excel('dados.xlsx', sheet_name='Planilha1')
gerar_boxplots(df1, area1_range=(1, 16), area2_range=(16, 46), area1_label='Cananeia', area2_label='Florianopolis')

# Processa a Planilha2: Salinidade vs Florianopolis
df2 = pd.read_excel('dados.xlsx', sheet_name='Planilha2')
gerar_boxplots(df2, area1_range=(1, 19), area2_range=(19, 37), area1_label='Salinidade', area2_label='Florianopolis')

print("\nTodos os box plots foram gerados e salvos.")

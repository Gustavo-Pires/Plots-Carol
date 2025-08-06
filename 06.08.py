import pandas as pd
import matplotlib.pyplot as plt
import os

# Carrega os dados do Excel
df = pd.read_excel('dados2.xlsx', sheet_name='Planilha2')


# Converte as colunas 'Pb' e 'Sr' para numérico
# A conversão de vírgula para ponto não é necessária pois o arquivo CSV já usa pontos.
# Mas a conversão para numérico com 'errors=coerce' é mantida para garantir a consistência dos dados.
for elemento in ['Pb', 'Sr']:
    if elemento in df.columns:
        df[elemento] = pd.to_numeric(df[elemento], errors='coerce')

# Define os grupos de amostras com base nos índices do DataFrame
grupo_indices = {
    'S15': list(range(0, 6)),    # Índices 0 a 5
    'S20': list(range(6, 11)),   # Índices 6 a 10
    'S25': list(range(11, 14)),  # Índices 11 a 13
    'S30': list(range(14, 16)),  # Índices 14 a 15
    'S35': list(range(16, 18))   # Índices 16 a 17
}

# Cria a pasta de saída para os gráficos
os.makedirs("boxplots_grupos", exist_ok=True)

# Gera os boxplots para 'Pb' e 'Sr'
for elemento in ['Pb', 'Sr']:
    if elemento not in df.columns:
        print(f"❌ Coluna '{elemento}' não encontrada no DataFrame.")
        continue

    dados_para_boxplot = []
    labels = []

    for grupo, indices in grupo_indices.items():
        valores = df.iloc[indices][elemento].dropna()
        if not valores.empty:
            dados_para_boxplot.append(valores)
            labels.append(grupo)
        else:
            print(f"⚠️ Grupo '{grupo}' não possui dados válidos para '{elemento}'. Ignorado.")

    if not dados_para_boxplot:
        print(f"❌ Nenhum dado válido encontrado para '{elemento}'.")
        continue

    # Cria o gráfico
    plt.figure(figsize=(10, 6))
    plt.boxplot(dados_para_boxplot, labels=labels)
    plt.title(f'Concentração de {elemento} por Grupo de Amostras')
    plt.xlabel('Grupo')
    plt.ylabel(f'Concentração de {elemento}')
    plt.grid(True)
    plt.tight_layout()

    # Salva a imagem
    plt.savefig(f'boxplots_grupos/boxplot_grupos_{elemento}.png', dpi=300)
    plt.close()

print("\n✅ Boxplots por grupo gerados com sucesso.")
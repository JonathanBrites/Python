import pandas as pd

# Caminho do arquivo
caminho_arquivo = r'C:\Users\PC\Downloads\chamados_abertos_clientes.xlsx'


# Carregando o arquivo Excel
df = pd.read_excel(caminho_arquivo)


# Definindo os filtros
filtro_unidade = df['UNIDADE'].isin(['ALP', 'BAJU', 'BJR', 'BMA', 'BPI', 'CMC', 'CMO', 'COLG', 'GUA', 'INF', 'ITPV', 'IZA', 'JMPR', 'MPE', 'NFO', 'PDS', 'PFS', 'PIBT', 'PNDO', 'PNHE', 'PORE', 'PTS', 'RSD', 'SIU', 'SJM', 'SPC', 'STA', 'TER', 'TRS', 'VAS', 'VLC', 'VRD'])

# Aplicando os filtros
dados_filtrados = df[filtro_unidade ]

# Exibindo os dados filtrados
print(dados_filtrados)

# Exportando para Excel
caminho_saida_excel = r'C:\Users\PC\Downloads\resultados_filtrados.xlsx'
dados_filtrados.to_excel(caminho_saida_excel, index=False)

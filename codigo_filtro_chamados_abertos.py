import pandas as pd
import time

inicio = time.time()

# Caminho do arquivo
caminho_arquivo = r'C:\Users\GIGA\Downloads\chamados_abertos_clientes.xlsx'

# Carregando o arquivo Excel
df = pd.read_excel(caminho_arquivo)

# Definindo os filtros
filtro_unidade = df['UNIDADE'].isin(['ALP', 'BAJU', 'BJR', 'BMA', 'BPI', 'CMC', 'CMO', 'COLG', 'GUA', 'INF', 'ITPV', 'IZA', 'JMPR', 'MPE', 'NFO', 'PDS', 'PFS', 'PIBT', 'PNDO', 'PNHE', 'PORE', 'PTS', 'RSD', 'SIU', 'SJM', 'SPC', 'STA', 'TER', 'TRS', 'VAS', 'VLC', 'VRD'])

# Aplicando os filtros
dados_filtrados = df[filtro_unidade]

# Excluindo as colunas especificadas
colunas_para_excluir = ['CÓDIGO CONTRATO LEGADO', 'CÓDIGO CLIENTE LEGADO', 'CÓDIGO CLIENTE']
dados_filtrados = dados_filtrados.drop(columns=colunas_para_excluir)

# Exibindo os dados filtrados
print(dados_filtrados)

# Exportando para Excel
caminho_saida_excel = r'C:\Users\GIGA\Downloads\Chamados_abertos.xlsx'
dados_filtrados.to_excel(caminho_saida_excel, index=False)

fim = time.time()

tempo_execução = fim - inicio
print("Tempo de execução:", tempo_execução, "segundos")



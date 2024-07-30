import pandas as pd
from datetime import datetime

# Função para filtrar as unidades do arquivo 'vendas_por_preríodo.xlsx' e salvar em 'vendas_filtradas.xlsx'
def filtrar_unidades_e_salvar(caminho_arquivo_vendas_por_periodo):
    # Carregando o arquivo Excel
    vendas_por_periodo = pd.read_excel(caminho_arquivo_vendas_por_periodo)

    # Definindo os filtros
    filtro_unidade = vendas_por_periodo['UNIDADE_ATENDIMENTO'].isin(['ALP', 'BAJU', 'BJR', 'BMA', 'BPI', 'CMC', 'CMO', 'COLG', 'GUA', 'INF', 'ITPV', 'IZA', 'JMPR', 'MPE', 'NFO', 'PDS', 'PFS', 'PIBT', 'PNDO', 'PNHE', 'PORE', 'PTS', 'RSD', 'SIU', 'SJM', 'SPC', 'STA', 'TER', 'TRS', 'VAS', 'VLC', 'VRD'])

    # Aplicando os filtros
    dados_filtrados = vendas_por_periodo[filtro_unidade]

    # Exibindo os dados filtrados
    print(dados_filtrados)

    # Exportando para Excel
    caminho_saida_excel = r'C:\Users\GIGA\Downloads\vendas_filtradas.xlsx'
    dados_filtrados.to_excel(caminho_saida_excel, index=False)

    return caminho_saida_excel

# Função para atualizar o arquivo 'Banco Vendas.xlsx' com as vendas de hoje
def atualizar_banco_vendas(caminho_arquivo_vendas_filtradas, caminho_arquivo_banco_vendas):
    # Carrega o arquivo das vendas filtradas
    vendas_filtradas = pd.read_excel(caminho_arquivo_vendas_filtradas)

    # Carrega o arquivo do banco de vendas
    banco_de_vendas = pd.read_excel(caminho_arquivo_banco_vendas)

    # Encontra a data de hoje
    data_hoje = datetime.now().date()

    # Filtra os dados do banco de vendas para as vendas de hoje
    vendas_hoje = vendas_filtradas[pd.to_datetime(vendas_filtradas['DATA_CRIAÇÃO'], format='%d/%m/%Y').dt.date == data_hoje]

    # Remove as linhas do banco de vendas que correspondem à data de hoje
    banco_de_vendas = banco_de_vendas[~(pd.to_datetime(banco_de_vendas['DATA_CRIAÇÃO'], format='%d/%m/%Y').dt.date == data_hoje)]

    # Adiciona as vendas de hoje ao banco de vendas
    banco_de_vendas = pd.concat([banco_de_vendas, vendas_hoje], ignore_index=True)

    # Salva o banco de vendas atualizado
    banco_de_vendas.to_excel(caminho_arquivo_banco_vendas, index=False)

# Caminho do arquivo 'vendas_por_preríodo.xlsx'
caminho_arquivo_vendas_por_periodo = r'C:\Users\GIGA\Downloads\vendas_por_período.xlsx'

# Filtrar unidades e salvar no arquivo 'vendas_filtradas.xlsx'
caminho_arquivo_vendas_filtradas = filtrar_unidades_e_salvar(caminho_arquivo_vendas_por_periodo)

# Caminho do arquivo 'Banco Vendas.xlsx'
caminho_arquivo_banco_vendas = r'C:\Users\GIGA\Desktop\Relatorios R6\Banco dados\Banco Vendas.xlsx'

# Atualizar o arquivo 'Banco Vendas.xlsx' com as vendas de hoje
atualizar_banco_vendas(caminho_arquivo_vendas_filtradas, caminho_arquivo_banco_vendas)

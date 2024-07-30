import pandas as pd
import glob

def csv_to_xlsx(csv_file, xlsx_file):
    # Ler o arquivo CSV
    df = pd.read_csv(csv_file)
    
    # Salvar como arquivo XLSX com uma nova planilha chamada "Tarefas"
    with pd.ExcelWriter(xlsx_file, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Tarefas', index=False)

# Caminho para o diretório onde os arquivos CSV estão localizados
caminho_diretorio_csv = r'C:\Users\GIGA\Downloads'
caminho_diretorio_xlsx = r'C:\Users\GIGA\Downloads\Tarefas.xlsx'

# Padrão para encontrar todos os arquivos CSV no diretório
padrao_csv = caminho_diretorio_csv + r'\Atividades-R06_*.csv'

# Lista todos os arquivos CSV no diretório especificado com o padrão
arquivos_csv = glob.glob(padrao_csv)

# Itera sobre cada arquivo CSV encontrado
for arquivo_csv in arquivos_csv:
    # Converta o arquivo CSV para XLSX
    csv_to_xlsx(arquivo_csv, caminho_diretorio_xlsx)

# Biblioteca Pandas
# Leitura de um arquivo do Excel para o DataFrame

import pandas as pd

# Importação com o caminho original do arquivo
# Podemos utilizar os diretórios r'c:\Diretórios\atéO\Arquivo'
dados_excel = pd.read_excel(
    r'C:\Users\85189741\Documents\GitHub\pythonPandasLinkedin\Arquivos_Exercicios_Python_Excel\01_06_Notas.xlsx')

# Importação sem erros
# dados_excel = pd.read_excel('01_06_Notas.xlsx')

print('Shape: ', dados_excel.shape)

print('DataFrame com Notas: ')
print(dados_excel)

print('Total de registros: ', dados_excel['DISCIPLINA'].count())

# Biblioteca Pandas
# Leitura de um arquivo do Excel para o DataFrame

import pandas as pd

# Importação com o caminho original do arquivo
dados_excel = pd.read_excel('C:\TEMPORÁRIA\01_06_Notas.xlsx')

exit()

# Importação sem erros
dados_excel = pd.read_excel('01_06_Notas.xlsx')

print('Shape: ', dados_excel.shape)

print('DataFrame com Notas: ')
print(dados_excel)

print('Total de registros: ', dados_excel['DISCIPLINA'].count())

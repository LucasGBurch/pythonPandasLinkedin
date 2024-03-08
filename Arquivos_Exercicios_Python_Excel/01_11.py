# Biblioteca Pandas
# Leitura de um arquivo do Excel para o DataFrame e salvamento do resultado

import pandas as pd
dados_excel = pd.read_excel(
    r'C:\Users\85189741\Documents\GitHub\pythonPandasLinkedin\Arquivos_Exercicios_Python_Excel\01_11_Notas.xlsx')

print(dados_excel.shape)  # Essa planilha tem 1k linhas e 3 colunas
print(dados_excel.head(10))  # Visualizar as colunas das 10 primeiras linhas

for index, row in dados_excel.iterrows():  # percorre cada linha do DataFrame
    if row['NOTA'] >= 5:
        dados_excel.loc[index, 'Aprovado'] = 'Sim'
    else:
        dados_excel.loc[index, 'Aprovado'] = 'Não'

print(dados_excel.head(10))

with pd.ExcelWriter(r'C:\Users\85189741\Documents\GitHub\pythonPandasLinkedin\Arquivos_Exercicios_Python_Excel\01_11_Notas_Resultado.xlsx') as arq_excel:
    dados_excel.to_excel(arq_excel, sheet_name='Alunos', index=False)

# Unir diversas pastas de trabalho do Excel para análise

import pandas as pd

df1 = pd.read_excel(
    r'C:\Users\85189741\Documents\GitHub\pythonPandasLinkedin\Arquivos_Exercicios_Python_Excel\01_10_Produtos_Parte_A.xlsx')
df2 = pd.read_excel(
    r'C:\Users\85189741\Documents\GitHub\pythonPandasLinkedin\Arquivos_Exercicios_Python_Excel\01_10_Produtos_Parte_B.xlsx')
df3 = pd.read_excel(
    r'C:\Users\85189741\Documents\GitHub\pythonPandasLinkedin\Arquivos_Exercicios_Python_Excel\01_10_Produtos_Parte_C.xlsx')

print(df1)
print(df2)
print(df3)

# Unir consultas - append FOI DESCONTINUADO PARA O PANDAS. SÓ O CONCAT FUNCIONA NAS VERSÕES ATUAIS (2024)
dfResultado1 = df1.append(df2).append(df3)
dfResultado2 = pd.concat([df1, df2, df3])

print(dfResultado2['ITEM'].count())

dfResultado3 = pd.concat([df1['PRODUTO'], df2['PRODUTO']])
print(dfResultado3)

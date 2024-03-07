# Filtrar dados de um DataFrame

import pandas as pd

df = pd.read_excel('01_09_Produtos.xlsx')
print(df)

# Filtrar uma coluna
print(df['PRODUTO'])

# Filtrar uma linha
# Método 1: cria uma lista com a comparação entre os valores, não faz a filtragem
print(df['PRODUTO'] == 'Produto 18')

lista_filtro = ['Produto 1', 'Produto 10', 'Produto 15']
print(df.loc[df['PRODUTO'].isin(lista_filtro)])

# Filtrar duas linhas
print(df[1:3])

filtro = df['TOTAL'] > 500
print(df[filtro])

# Método Query
print(df.query('PRODUTO=="Produto 18" or PRODUTO=="Produto 20"'))
print(df.query('TOTAL>700'))
print(df.query('PRODUTO=="Produto 18" or TOTAL>500'))

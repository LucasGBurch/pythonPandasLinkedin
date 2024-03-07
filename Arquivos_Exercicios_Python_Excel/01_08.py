# Classificação dos dados de um DataFrame

import pandas as pd

df = pd.read_excel('01_06_Notas.xlsx')
# print(df)

# SORT_VALUES

# Classificar valores do DataFrame em ordem decrescente
print(df.sort_values(by=['NOTA'], ascending=False))

# Classificar valores do DataFrame em ordem crescente
print(df.sort_values(by=['NOTA'], ascending=True))

# SORT_INDEX

print(df.sort_index(ascending=False))

# Transposição do Dataframe
print(df.T)

print()

# axis = 0 para índices nas colunas
#      = 1 para índices em linhas
print(df.T.sort_index(ascending=False, axis=1))

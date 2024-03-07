# DataFrames

import pandas as pd
# shift + enter para executar no terminal e rodar linha por linha ou seus conjuntos
import numpy as np

# Criação de um array padrão, com apenas 1 coluna com 6 dias sequênciais
datas = pd.date_range("20220101", periods=6, freq='D')
print(datas)

# Array multidimensional de 6 linhas com 4 colunas sem índice
np.random.randn(6, 4)

# Vamos definir o índice com o uso do array datas
df = pd.DataFrame(np.random.randn(6, 4), index=datas, columns=list("ABCD"))
df

# Algumas propriedades de um DataFrame
# Cabeçalho
df.head(len(df) - 2)
# head() vazio mostrou 5 linhas em vez das 6, por isso testei usando len(df) e funcionou melhor

# Rodapé
df.tail(2)

# Descritivo do dataframe (informações sobre o dataframe)
df.describe()

# Transposição do Dataframe (inverte linhas e colunas)
df.T

# Classificar valores do DataFrame (neste caso, os da coluna C ficam em ordem crescente)
df.sort_values(by="C")

# Selecionar apenas uma coluna
df["B"]

# Selecionar faixa de valores (Retorna segunda e terceira linha)
df[1:3]

# Localizar dados no DataFrame com loc
# No exemplo, localiza a terceira linha do dataFrame datas
df
df.loc[datas[2]]

# NUNCA ESQUECER DE SELECIONAR OS TRECHOS E APLICAR SHIFT + ENTER PARA RODAR SEPARADAMENTE!!!

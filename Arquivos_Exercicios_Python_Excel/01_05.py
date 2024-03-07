# DataFrames

import pandas as pd
import numpy as np

# Criação de um array padrão, com apenas 1 coluna com 6 dias sequênciais
datas = pd.date_range("20220101", periods=6, freq='D')
print(datas)

exit()

# Array multidimensional de 6 linhas com 4 colunas sem índice
np.random.randn(6, 4)

# Vamos definir o índice com o uso do array datas
df = pd.DataFrame(np.random.randn(6, 4), index=datas, columns=list("ABCD"))
df

# Algumas propriedades de um DataFrame
# Cabeçalho
df.head()

# Rodapé
df.tail(2)

# Descritivo do dataframe
df.describe()

# Transposição do Dataframe
df.T

# Classificar valores do DataFrame
df.sort_values(by="C")

# Selecionar apenas uma coluna
df["B"]

# Selecionar faixa de valores (Retorna segunda e terceira linha)
df[1:3]

# Localizar dados no DataFrame com loc
# No exemplo, localiza a terceira linha do dataFrame datas
df
df.loc[datas[3]]

# Pandas SERIES

import pandas as pd
import numpy as np  # biblioteca para manipulação de matrizes

s = pd.Series([1, 2, 3])
print(s)

# exit() serve para interromper a execução depois da chamada da função

# Cria uma Serie com índice padrão
s1 = pd.Series(np.random.randn(5))
print(s1)

# Cria uma Serie com um índice abcde com dados gerados com o numpy
s2 = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
print(s2)

# Acessando um elemento dessa lista
print(s1[0])

# Acessando um elemento com base em um índice
print(s2["c"])

# Exibe o índice de uma Serie
print(s2.index)

# VALOR ESCALAR (Único para todos os elementos)

s3 = pd.Series(5, index=["a", "b", "c", "d", "e"])
print(s3)

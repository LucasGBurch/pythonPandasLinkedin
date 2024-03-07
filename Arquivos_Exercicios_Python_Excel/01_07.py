# Biblioteca Pandas
# Leitura de um arquivo CSV para o DataFrame

# Ler arquivo CSV
# Dados em diretórios diferentes podem ser escritos da forma abaixo:
# 'c:/temporária/01_07_CSV.csv'

import pandas as pd

#dados_csv = pd.read_csv(filepath_or_buffer='01_07_CSV.csv', sep=';',  encoding='utf8')

print(dados_csv)

# Testar propriedade do objeto dados_csv
print('Quantidade de registros: ', dados_csv['PRODUTO'].count())

# Converter para um objeto do tipo DataFrame
df = pd.DataFrame(dados_csv)

print(df.sum())

valor_total = 0

for registro in dados_csv['TOTAL']:
    valor_total += float(registro.replace(',', '.'))

print()
print('O valor total convertido é de: ', valor_total)

# Criação de um gráfico de haste

import pandas as pd
import xlwings as xw
import matplotlib.pyplot as plt

wb = xw.Book('03_05_Notas.xlsx')
ws = wb.sheets(1)

ultcel = ws.used_range.last_cell.row

# Transferindo os dados para um DataFrame

df = pd.DataFrame(data=ws.range("A2:C" + str(ultcel)).value,
                  columns=ws.range("A1:C1").value)

# Definir eixos X e Y

x = df['DISCIPLINA']
y = df['NOTA']

# Criação do gráfico

fig, ax = plt.subplots()
ax.stem(x, y, linefmt='--')  # tipo de gráfico

ax.set(xticks=range(0, 8),
       yticks=range(1, 11))  # definição dos limites

for label in ax.get_xticklabels(which='major'):
    label.set(rotation=30, horizontalalignment='right')

plt.show()
wb.close()

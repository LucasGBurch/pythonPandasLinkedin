# Gráfico de Pizza

import pandas as pd
import xlwings as xw
import matplotlib.pyplot as plt

wb = xw.Book('03_06_Notas.xlsx')
ws = wb.sheets(1)

ultcel = ws.used_range.last_cell.row

# Transferindo os dados para um DataFrame

df = pd.DataFrame(data=ws.range("A2:C" + str(ultcel)).value,
                  columns=ws.range("A1:C1").value)

# Definir Legenda e Fatias

x = df['DISCIPLINA']
y = df['NOTA']

plt.pie(y, labels=x, autopct='%1.1f%%', shadow=False,
        explode=(0.1, 0, 0, 0, 0, 0, 0, 0))
plt.title('Relatório de Notas - FINAL')
plt.show()

wb.close()

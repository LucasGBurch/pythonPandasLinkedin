# Gráficos de Barras Horizontais com DataFrame Pandas

import pandas as pd
import xlwings as xw
import matplotlib.pyplot as plt

wb = xw.Book(
    r'C:\Users\85189741\Documents\GitHub\pythonPandasLinkedin\Arquivos_Exercicios_Python_Excel\03_04_Notas.xlsx')
ws = wb.sheets(1)

ultcel = ws.used_range.last_cell.row

# Transferindo os dados para um DataFrame

df = pd.DataFrame(data=ws.range("A2:C" + str(ultcel)).value,
                  columns=ws.range("A1:C1").value)

# Definir eixos X e Y

x = df['DISCIPLINA']
y = df['NOTA']

plt.barh(x, y, height=0.9)
plt.grid(which='major', axis='x', linewidth=0.2)
plt.xticks(range(1, 11))
# Uma range de 0 a 10 em linhas verticais para marcar os valores do eixo X

plt.title('Relatório de Notas - FINAL')
plt.show()

wb.close()

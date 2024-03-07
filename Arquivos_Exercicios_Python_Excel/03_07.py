# Chamar a rotina do Python diretamente do Excel

import matplotlib.pyplot as plt
import xlwings as xw
import pandas as pd

wb = xw.Book('03_07_Notas.xlsm')
ws = wb.sheets(1)

ultcel = ws.used_range.last_cell.row

# Transferindo os dados para um DataFrame

df = pd.DataFrame(data=ws.range("A2:C" + str(ultcel)).value,
                  columns=ws.range("A1:C1").value)

# Definir Legenda e Fatias

x = df['DISCIPLINA']
y = df['NOTA']
fig = plt.figure()

plt.pie(y, labels=x, autopct='%1.1f%%', shadow=False,
        explode=(0.1, 0, 0, 0, 0, 0, 0, 0))
plt.title('Relatório de Notas - FINAL')
# plt.show()

# Transfere o gráfico para o Excel

ws = wb.sheets(1)
ws.pictures.add(
    fig,
    name="GráficoTeste",
    update=True,
    width=300,
    height=250,
    left=ws.range("H1").left,
    top=ws.range("H1").top)


# wb.close()

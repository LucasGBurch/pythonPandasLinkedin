# Utilizar dados de uma planilha em um DataFrame
# Biblioteca xlwings

import pandas as pd
import xlwings as xw

wb = xw.Book('02_05_Notas.xlsx')
ws = wb.sheets(1)
ultcel = ws.used_range.last_cell.row
Total_Aprovados = 0
Total_Reprovados = 0

# Transferindo os dados para um DataFrame

df = pd.DataFrame(data=ws.range("A2:C" + str(ultcel)).value,
                  columns=ws.range("A1:C1").value)
print(df.shape)
print('Média Geral dos alunos: ' + str(df['NOTA'].sum() / df['NOTA'].count()))

# Contagem da quantidade de aprovados e reprovados

for registro in df['NOTA']:
    if registro >= 5:
        Total_Aprovados += 1
    else:
        Total_Reprovados += 1

print('Aprovados: ', Total_Aprovados)
print('Reprovados: ', Total_Reprovados)

wb.save()
wb.close()

# Gravar dados em um arquivo csv
# Biblioteca xlwings

import pandas as pd
import xlwings as xw

wb = xw.Book(
    r'C:\Users\85189741\Documents\GitHub\pythonPandasLinkedin\Arquivos_Exercicios_Python_Excel\02_06_Notas.xlsx')
ws = wb.sheets(1)
ln = 1
col = 4

ultcel = ws.used_range.last_cell.row

# Transferindo os dados para um DataFrame

df = pd.DataFrame(data=ws.range("A2:C" + str(ultcel)).value,
                  columns=ws.range("A1:C1").value)
print(df.head(10))
resultado = []

for value in df['NOTA']:
    if value >= 5:
        resultado.append("Aprovado")
    else:
        resultado.append("Reprovado")

df['RESULTADO'] = resultado
print(df)

df.to_csv(r'C:\Users\85189741\Documents\GitHub\pythonPandasLinkedin\Arquivos_Exercicios_Python_Excel\02_06_CSVExportado.csv', index=False)

wb.close()

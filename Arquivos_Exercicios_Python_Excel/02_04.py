# Manipulação de planilhas
# Biblioteca xlwings

import xlwings as xw

wb = xw.Book()
ws = wb.sheets(1)
ws = wb.sheets('Planilha1')

wb.sheets.add(name='Plan 2', after=wb.sheets(1))
wb.sheets.add(name='Plan 3', before=wb.sheets(1))

wb.sheets(1).name = 'Planilha renomeada'
print(wb.sheets(1).name)

# exit()

wb.sheets(3).delete()
wb.close()   # Fecha sem salvar

# Abrir pasta de trabalho e capturar seus objetos
# Biblioteca xlwings

import xlwings as xw

# Abrir uma pasta de trabalho
wb = xw.Book('02_02_Notas.xlsx')

# Criar uma workbook nova
wbNovo = xw.Book()

# Escrever na célula A1
wbNovo.sheets(1).range("A1").value = 'Módulo 2 - Aula 02 - Excel x Python'

# Salvar a pasta de trabalho
wbNovo.save('02_02_wbNovo.xlsx')
wbNovo.close()

# Exibir nome da planilha 1
print('Nome da planilha 1: ', wb.sheets(1).name)

# Mapear planilha 1
ws = wb.sheets(1)
print(ws.name)

wb.save()
wb.close()

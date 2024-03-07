# Manipulação de células
# Biblioteca xlwings

import xlwings as xw

wb = xw.Book()

ws = wb.sheets(1)

# Escrever nas células
ws.range("A1").value = 'Módulo 2 - Aula 02 - Excel x Python'
ws.range("A2").value = 'Como manipular células utilizando a biblioteca xlwings'

# Mesclar células
ws.range("A1:G1").merge()
ws.range("A2:G2").merge()

# Formatação
ws.range("A1:G2").color = "#548235"
ws.range("A1:G2").font.color = "#FFFFFF"
ws.range("A1:G2").font.bold = True

Titulos = ['ITEM', 'PRODUTO', 'PREÇO UNIT', 'TOTAL']
Itens = ([1, 'Produto 1', 100], [2, 'Produto 2', 200], [3, 'Produto 3', 150])

ws.range("A4:D4").value = Titulos
ws.range("A5:D7").value = Itens
ws.used_range.autofit()

wb.save(r'c:\temp\02_03_ManipularPlanilhas.xlsx')
wb.close()

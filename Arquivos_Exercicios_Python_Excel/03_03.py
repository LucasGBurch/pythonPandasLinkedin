# Transferir gráfico gerado para o Excel

import matplotlib.pyplot as plt
import xlwings as xw

# Gráfico de colunas padrão

x = [1, 2, 3, 4]
y = [1, 7, 4, 9]

fig = plt.figure()

plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.grid(False)
plt.title('Python x Excel - Exemplo')
plt.bar(x, y)

plt.show()
exit()

# Transfere o gráfico para o Excel

wb = xw.Book()
ws = wb.sheets(1)
ws.pictures.add(
    fig,
    name="GráficoTeste",
    update=True,
    width=300,
    height=250,
    left=ws.range("C3").left,
    top=ws.range("C3").top)

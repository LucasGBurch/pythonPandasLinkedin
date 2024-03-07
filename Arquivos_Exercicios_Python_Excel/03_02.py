# Gerar um gráfico com matplotlib

import matplotlib.pyplot as plt

# Gráfico de colunas padrão

x = [1, 2, 3, 4]
y = [1, 4, 9, 5]

plt.bar(x, y)  # Variações barh, pie, boxplot

plt.show()

plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.grid(False)
plt.title('Python x Excel - Exemplo')
plt.bar(x, y, color='red')

plt.show()

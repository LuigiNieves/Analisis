import matplotlib.pyplot as plt

# Datos originales (reemplaza estos datos con tus propias listas)
Y = [10, 12, 15, 20, 25]
C = [8, 10, 12, 18, 20]

# Calcular las medias de Y y C
mean_Y = sum(Y) / len(Y)
mean_C = sum(C) / len(C)

# Centrar los datos restando las medias
Y_centered = [y - mean_Y for y in Y]
C_centered = [c - mean_C for c in C]

# Crear el gráfico de dispersión antes y después de centrar los datos
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.scatter(Y, C)
plt.xlabel('Ingreso (Y)')
plt.ylabel('Consumo (C)')
plt.title('Antes de centrar los datos')

plt.subplot(1, 2, 2)
plt.scatter(Y_centered, C_centered)
plt.xlabel('Ingreso centrado')
plt.ylabel('Consumo centrado')
plt.title('Después de centrar los datos')

plt.tight_layout()
plt.show()

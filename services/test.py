import pprint

import numpy as np

data = np.array([1764, 1039, 549, 291, 142, 99, 60, 36, 32, 20, 19, 16, 11, 6, 2, 7, 14, 1, 2, 2, 2, 1, 1, 2, 1])
li = np.array([1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100, 109, 118, 127, 136, 145, 154, 163, 172, 181, 190, 199, 208])
ls = np.array([9,18, 27, 36, 45,54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153, 162, 171, 180, 189, 198, 207, 216])
# data = np.array([446,2509,1153,11])
num_classes = 28
total_data = 4119



print()

range_data = np.max(data) - np.min(data)
print(range_data.__round__())
class_width = range_data / num_classes
print(class_width.__round__())
lower_limits = np.arange(np.min(data), np.max(data), class_width.__round__() + 1)
upper_limits = lower_limits + class_width.__round__()

# Asegurarse de que el último límite superior sea igual al máximo valor de los datos
upper_limits[-1] = np.max(data)
classes = np.arange(1, num_classes + 1)
frequencies = np.bincount((data - np.min(data)) // class_width.astype(int))
print("Límites inferiores de las clases:");
print(lower_limits)
print("Límites superiores de las clases:");
print(upper_limits)
print("Frecuencia absoluta de cada clase:");
print(frequencies)
print("Frecuencia absoluta de cada clase:");
print(np.column_stack((classes, frequencies)))
# import matplotlib.pyplot as plt

# Datos de las clases
# clases = [1, 2, 3, 4, 5]
# lim_inf = [20, 23, 26, 29, 32]
# lim_sup = [22, 25, 28, 31, 33]
# marca_clase = [21, 24, 27, 30, 21]
# frec_abs = [1, 1, 5, 9, 7]

# Crear el histograma
# plt.figure(figsize=(8, 6))
# plt.bar(clases, frec_abs, align='center', color='blue', edgecolor='black')
# plt.xlabel('Clase')
# plt.ylabel('Frecuencia Absoluta')
# plt.title('Histograma')
# plt.show()

# Crear la gráfica de barras
# plt.figure(figsize=(8, 6))
# plt.bar(marca_clase, frec_abs, align='center', color='red', edgecolor='black', width=2)
# plt.xlabel('Marca de Clase')
# plt.ylabel('Frecuencia Absoluta')
# plt.title('Gráfica de Barras')
# plt.show()

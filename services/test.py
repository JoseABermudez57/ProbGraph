import tkinter as tk
from pandastable import Table
import pandas as pd

def create_frequency_table(data):
    if len(set(map(len, data))) > 1:
        raise ValueError("Todos los arrays deben tener la misma longitud")

    # Resto del código para crear la tabla de frecuencias

# Crear una ventana principal
window = tk.Tk()
window.title("Tabla de Frecuencias")

# Ejemplo de datos
data = pd.Series([1, 2, 3, 2, 4, 3, 1, 2, 3, 4, 1, 3, 2, 4, 1])

# Envolver el número entero en una lista
data = [data]

# Verificar la longitud de los datos
if len(set(map(len, data))) > 1:
    raise ValueError("Todos los arrays deben tener la misma longitud")

# Crear la tabla de frecuencias
frequency_table = create_frequency_table(data)

# Resto del código para mostrar la tabla en la ventana
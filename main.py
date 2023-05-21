from tkinter import Tk, Button, Label, filedialog, ttk
import pandas as pd

def open_files():
    root = Tk()
    root.withdraw()

    file = filedialog.askopenfile(filetypes=[('CSV Files', '*.csv')])  # Open the dialog box
    if file:
        # Open file process
        content = pd.read_csv(file)
        attributes = content.columns.tolist()

        Label(window, text="Seleccione el atributo y el tipo de gráfico que desea realizar").place(x=60, y=130)
        combobox_attributes = ttk.Combobox(window, values=attributes)
        combobox_attributes.place(x=60, y=150)

        combobox_graph = ttk.Combobox(window, values=["Barras", "Pastel"])
        combobox_graph.place(x=200, y=150)

        def get_column_values():
            selected_column = combobox_attributes.get()
            column_values = content[selected_column].tolist()
            Label(window, text=column_values).place(x=60, y=220)

        values_button = Button(window, text="Obtener gráfica", command=get_column_values)
        values_button.place(x=60, y=190)

# Create the main window
window = Tk()
window.geometry("900x500")
window.title("ProbGraph")

# Create the "Open file" section
text = Label(window, text="Seleccione el archivo '.csv' que desee analizar")
text.place(x=60, y=40)
open_button = Button(window, text="Abrir archivo", command=open_files)
open_button.place(x=60, y=60)

# Initiate the event loop for the graphical interface
window.mainloop()

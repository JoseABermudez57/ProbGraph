from tkinter import Tk, Button, Label, filedialog, ttk
import pandas as pd
import services.graphics as graphics
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import services.utils as nc


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
        graphics_select = ["Histograma", "Polígono de frecuencias", "Ojivas", "Gráfica de barras", "Gráfica de pastel"]
        combobox_graph = ttk.Combobox(window, values=graphics_select)
        combobox_graph.place(x=200, y=150)

        def get_column_values():
            selected_column = combobox_attributes.get()
            column_values = content[selected_column]
            graphs = combobox_graph.get()
            if graphs == "Histograma":
                total_value = nc.total_value(column_values.value_counts().__len__())
                number_class = nc.number_class(total_value)
                range_method = nc.range_method(column_values.value_counts())
                class_width = nc.class_width(range_method, number_class)
                lower_limits = nc.limit_inf(column_values.value_counts().sort_values(ascending=False), class_width)
                upper_limits = nc.limit_sup(lower_limits, class_width)
                upper_limits[-1] = max(column_values.value_counts())
                class_marks = nc.class_marks(lower_limits, upper_limits)
                frec_absolute = nc.frec_absolute(column_values.value_counts(), number_class, class_width)
                graphics.histogram_plot(frec_absolute, class_marks, canvas)
            elif graphs == "Polígono de frecuencias":
                graphics.frequency_polygon_graph(column_values.value_counts().sort_values(ascending=False),
                                                 column_values.value_counts().sort_values(ascending=False).index.tolist(), canvas)
            elif graphs == "Ojivas":
                graphics.warhead_graph(column_values.value_counts().sort_values(ascending=True),
                                       column_values.value_counts().index.tolist(), canvas)
            elif graphs == "Gráfica de barras":
                graphics.bar_graph(column_values.value_counts().sort_values(ascending=True),
                                   column_values.value_counts().sort_values(ascending=True).index.tolist(), canvas)
            else:
                graphics.pie_chart(column_values.value_counts(), column_values.value_counts().index.tolist(), canvas)

        values_button = Button(window, text="Obtener gráfica", command=get_column_values)
        values_button.place(x=60, y=190)


# Create the main window
window = Tk()
window.geometry("1080x1080")
window.title("ProbGraph")

# Create the "Open file" section
text = Label(window, text="Seleccione el archivo '.csv' que desee analizar")
text.place(x=60, y=40)
open_button = Button(window, text="Abrir archivo", command=open_files)
open_button.place(x=60, y=60)

fig = plt.figure(figsize=(6, 5), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().place(x=450, y=150)

# Initiate the event loop for the graphical interface
window.mainloop()

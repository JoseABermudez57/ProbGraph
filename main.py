from tkinter import Tk, Button, Label, filedialog, ttk, font, Canvas
import pandas as pd
import DataGraphics as graphics
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import DataOperations as do
from pandastable import Table

def open_files():
    root = Tk()
    root.withdraw()

    file = filedialog.askopenfile(filetypes=[('CSV Files', '*.csv')])

    if file:

        content = pd.read_csv(file)

        canvas2 = Canvas(window)
        canvas2.configure(bg="black")

        canvas2.place(x=0, y=385)

        table = Table(canvas2, dataframe=content)
        table.configure(background="blue", width=574)
        table.show()

        table.update_idletasks()
        canvas2.config(scrollregion=canvas2.bbox("all"))

        attributes = content.columns.tolist()
        text_font_t = font.Font(family="Helvetica", size=10, weight="bold")
        label_attribute = Label(window, text="Select attribute", font=text_font_t)
        label_attribute.configure(bg="black", fg="white")
        label_attribute.place(x=25, y=80)
        combobox_attributes = ttk.Combobox(window, values=attributes, foreground="black",
                                           font=text_font_t)
        combobox_attributes.place(x=9, y=110)
        label_graphics = Label(window, text="Select type graphics", font=text_font_t)
        label_graphics.configure(bg="black", fg="white")
        label_graphics.place(x=12, y=140)
        graphics_select = ["Histograma", "Polígono de frecuencias", "Ojivas", "Gráfica de barras", "Gráfica de pastel"]
        combobox_graph = ttk.Combobox(window, values=graphics_select, foreground="black",
                                      font=text_font_t)
        combobox_graph.place(x=9, y=170)


        def get_column_values():
            selected_column = combobox_attributes.get()

            column_values = content[selected_column]
            # dtype = content[selected_column].dtype
            # if dtype == 'object':
            total_value = do.total_value(column_values.value_counts().__len__())
            number_class = do.number_class(total_value)
            range_method = do.range_method(column_values.value_counts())
            class_width = do.class_width(range_method, number_class)
            lower_limits = do.limit_inf(column_values.value_counts().sort_values(ascending=False), class_width)
            upper_limits = do.limit_sup(lower_limits, class_width)
            upper_limits[-1] = max(column_values.value_counts())
            class_marks = do.class_marks(lower_limits, upper_limits)
            frec_absolute = do.frec_absolute(column_values.value_counts(), number_class)
            #d = {'Clases': list(range(1, number_class + 1)), 'Limite inferior': lower_limits, 'Limite superior': upper_limits,
            #'Frecuencia absoluta': frec_absolute, 'Frecuencia relativa': ,
            #'Frecuencia relativa acumulada': ['-', '-', '-']}
            graphs = combobox_graph.get()
            if graphs == "Histograma":
                graphics.histogram_plot(frec_absolute, class_marks, canvas)
            elif graphs == "Polígono de frecuencias":
                graphics.frequency_polygon_graph(column_values.value_counts().sort_values(ascending=False),
                                                 column_values.value_counts().sort_values(
                                                     ascending=False).index.tolist(), canvas)
            elif graphs == "Ojivas":
                graphics.warhead_graph(column_values.value_counts().sort_values(ascending=True),
                                       column_values.value_counts().index.tolist(), canvas)
            elif graphs == "Gráfica de barras":
                graphics.bar_graph(column_values.value_counts().sort_values(ascending=True),
                                   column_values.value_counts().sort_values(ascending=True).index.tolist(), canvas)
            else:
                graphics.pie_chart(column_values, column_values.value_counts().index.tolist(), canvas)

        values_button = Button(window, text="Get graphic", command=get_column_values, font=text_font_t)
        values_button.configure(bg="blue", fg="white", relief="groove", bd=2, highlightthickness=2)
        values_button.place(x=40, y=200)


window = Tk()
window.geometry("1200x700")
window.title("ProbGraph")
window.configure(background="white")

text_font = font.Font(family="Helvetica", size=10, weight="bold")
text = Label(window, text="Select file '.csv'", font=text_font)
text.configure(bg="black", fg="white")
text.place(x=25, y=10)

open_button = Button(window, text="Open file", command=open_files, font=text_font)
open_button.configure(bg="black", fg="white", relief="groove", bd=2, highlightthickness=2)
open_button.place(x=40, y=40)

fig = plt.figure(figsize=(4, 5), dpi=139)
fig.patch.set_facecolor('gray')
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().place(x=642, y=2)


window.mainloop()

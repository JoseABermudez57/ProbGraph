import os
from tkinter import Tk, Button, Label, filedialog, ttk, font, Canvas
import pandas as pd
import DataGraphics as graphics
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import DataOperations as do
from pandastable import Table

def create_frequency_table(file_name, graph_name,classes, lower_limits, upper_limits, class_marks, rel_frequency
                           , ab_frequency, ac_frequency):
    print(f'El numero de clases es {classes} de la columna {graph_name}')

    canvas = Canvas(window)
    canvas.configure(bg="black")
    canvas.place(x=200, y=10, width=390)

    def export_table():

        folder_name = f'csv_files'
        os.makedirs(folder_name, exist_ok=True)

        file_path = os.path.join(folder_name, f'{graph_name}Table.csv')

        df.to_csv(file_path, index=False)

    df = pd.DataFrame({
        "# clase": list(range(1, classes + 1)),
        "Lim.inf": lower_limits,
        "Lim.sup": upper_limits,
        "Marc.Clase": class_marks,
        "Frec.abs": ab_frequency,
        "Frec.rel": rel_frequency,
        "Frec.rel_acum": ac_frequency
    })

    export_button = Button(window, text="Export table", command=export_table, font=text_font)
    export_button.configure(bg="black", fg="white", relief="groove", bd=2, highlightthickness=2)
    export_button.place(x=250, y=340)

    table = Table(canvas, dataframe=df)
    table.configure(background="blue")
    table.autoResizeColumns()
    table.show()
    table.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

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

        def on_attribute_select(event):
            selected_column = combobox_attributes.get()
            column_values = content[selected_column]

            is_numeric = all(isinstance(item, (int, float)) for item in column_values)
            is_string = all(isinstance(item, str) for item in column_values)

            if is_numeric:
                graphics_select = ["Histograma", "Polígono de frecuencias", "Ojivas", "Gráfica de barras",
                                   "Gráfica de pastel"]
            elif is_string:
                graphics_select = ["Gráfica de barras", "Gráfica de pastel"]
            else:
                graphics_select = []

            combobox_graph.configure(values=graphics_select)

        combobox_attributes.bind("<<ComboboxSelected>>", on_attribute_select)

        combobox_attributes.place(x=9, y=110)
        label_graphics = Label(window, text="Select type graphics", font=text_font_t)
        label_graphics.configure(bg="black", fg="white")
        label_graphics.place(x=12, y=140)
        graphics_select = [""]
        combobox_graph = ttk.Combobox(window, values=graphics_select, foreground="black",
                                      font=text_font_t)
        combobox_graph.place(x=9, y=170)

        def crate_column_graph():
            selected_column = combobox_attributes.get()
            column_values = content[selected_column]

            total_value = do.total_value(column_values.__len__())
            range_method = do.range_method(column_values)
            number_class = do.number_class(total_value)
            class_width = do.class_width(range_method, number_class)
            lower_limits = do.limit_inf(column_values, class_width)
            upper_limits = do.limit_sup(lower_limits, class_width)
            class_marks = do.class_marks(lower_limits, upper_limits)
            frec_absolute = do.frec_absolute(column_values, lower_limits, upper_limits)
            frec_relative = do.frequency_relative(frec_absolute)
            frec_relative_accum = do.frequency_relative_accumulate(frec_relative)
            graphs = combobox_graph.get()
            print(f'El nombre de la gráfica es: {graphs}')
            print(f'El numero de clases es {number_class}')
            print(lower_limits.__len__())
            print(upper_limits.__len__())
            print(class_marks.__len__())
            print(frec_relative.__len__())
            print(frec_absolute.__len__())
            print(frec_relative_accum.__len__())

            # create_frequency_table(file_name, graph_name,classes, lower_limits, upper_limits, class_marks, rel_frequency
            #                            , ab_frequency, ac_frequency)
            if graphs == "Histograma":
                graphics.histogram_plot(frec_absolute, class_marks, canvas)
                create_frequency_table(file.name, selected_column, number_class, lower_limits, upper_limits, class_marks, frec_relative, frec_absolute, frec_relative_accum)
            elif graphs == "Polígono de frecuencias":
                graphics.frequency_polygon_graph(frec_relative, class_marks, canvas)
                create_frequency_table(file.name, selected_column, number_class, lower_limits, upper_limits, class_marks, frec_relative, frec_absolute, frec_relative_accum)
            elif graphs == "Ojivas":
                graphics.warhead_graph(frec_relative_accum, class_marks, canvas)
                create_frequency_table(file.name, selected_column, number_class, lower_limits, upper_limits, class_marks, frec_relative, frec_absolute, frec_relative_accum)
            elif graphs == "Gráfica de barras":
                graphics.bar_graph(column_values, canvas)
                create_frequency_table(file.name, selected_column, number_class, lower_limits, upper_limits, class_marks, frec_relative, frec_absolute, frec_relative_accum)
            elif graphs == "Gráfica de pastel":
                graphics.pie_chart(column_values, canvas)
                create_frequency_table(file.name, selected_column, number_class, lower_limits, upper_limits, class_marks, frec_relative, frec_absolute, frec_relative_accum)
            else:
                selected_graphic = Tk()
                selected_graphic.geometry("200x200")
                selected_graphic.configure(background="white")
                text_font2 = font.Font(family="Helvetica", size=15, weight="bold")
                text22 = Label(selected_graphic, text="Select graphic please", font=text_font2)
                text22.configure(bg="black", fg="white")
                text22.place(x=30, y=20)

                def close_window():
                    selected_graphic.destroy()

                open_button2 = Button(selected_graphic, text="Ok", command=close_window, font=text_font2)
                open_button2.configure(bg="black", fg="white", relief="groove", bd=2, highlightthickness=2)
                open_button2.place(x=50, y=80)

        values_button = Button(window, text="Get graphic", command=crate_column_graph, font=text_font_t)
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

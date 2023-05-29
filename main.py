import os
import random
from tkinter import Tk, Button, Label, filedialog, ttk, font, Canvas
import numpy as np
import pandas as pd
import DataGraphics as graphics
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import DataOperations as do
from pandastable import Table


def create_frequency_table(column_values, type_data, graph_name):

    canvas = Canvas(window)
    canvas.configure(bg="black")
    canvas.place(x=200, y=7, width=390)

    def export_table():

        folder_name = f'csv_files'
        os.makedirs(folder_name, exist_ok=True)

        file_path = os.path.join(folder_name, f'{graph_name}Table.csv')

        df.to_csv(file_path, index=False)

    if type_data == "object" or type_data == "bool" or (type_data == "int64" and graph_name == "Gráfica de barras") or (type_data == "int64" and graph_name == "Gráfica de pastel"):
        index = column_values.value_counts().index
        frec_abs = column_values.value_counts().values
        frec_relative = do.frequency_relative(frec_abs)
        frec_rel_acumm = do.frequency_relative_accumulate(frec_relative)
        frec_abs_acumm = do.frec_abs_acumm(frec_abs)
        df = pd.DataFrame({
            "# clase": index,
            "Frec.abs": frec_abs,
            "Frec.abs_acum": frec_abs_acumm,
            "Frec.rel": frec_relative,
            "Frec.rel_acum": frec_rel_acumm
        })
    elif type_data == "int64" or type_data == "float64":
        total_value = do.total_value(column_values.__len__())
        range_method = do.range_method(column_values)
        number_class = do.number_class(total_value)
        class_width = do.class_width(range_method, number_class)
        lower_limits = do.limit_inf(column_values, class_width)
        upper_limits = do.limit_sup(lower_limits, class_width)
        class_marks = do.class_marks(lower_limits, upper_limits)
        frec_absolute = do.frec_absolute(column_values, lower_limits, upper_limits)
        frec_relative = do.frequency_relative(frec_absolute.values)
        frec_relative_accum = do.frequency_relative_accumulate(frec_relative)
        frec_abs_acumm = do.frec_abs_acumm(frec_absolute)
        y = np.arange(1, number_class + 1)


        df = pd.DataFrame({
            "# clase": y,
            "Lim.inf": lower_limits,
            "Lim.sup": upper_limits,
            "Marc.Clase": class_marks,
            "Frec.abs": frec_absolute,
            "Frec.abs_acum": frec_abs_acumm,
            "Frec.rel": frec_relative,
            "Frec.rel_acum": frec_relative_accum
        })

    export_button = Button(window, text="Export table", command=export_table, font=text_font)
    export_button.configure(bg="black", fg="white", relief="groove", bd=2, highlightthickness=2)
    export_button.place(x=250, y=280)

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
            is_boolean = all(isinstance(item, bool) for item in column_values)

            if is_numeric:
                graphics_select = ["Histograma", "Polígono de frecuencias", "Ojivas", "Gráfica de barras",
                                   "Gráfica de pastel"]
            elif is_string or is_boolean or is_numeric:
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

        def conglo(data):
            num_samples = len(data)
            cong_size = 100
            num_cong = num_samples // cong_size
            remainder = num_samples % cong_size

            random.shuffle(data)

            conglomerates = []

            start_index = 0
            for i in range(num_cong):
                end_index = start_index + cong_size

                cluster = data[start_index:end_index]
                conglomerates.append(cluster)

                start_index = end_index

            if remainder > 0:
                last_cluster = data[start_index:]
                conglomerates.append(last_cluster)

            return random.choice(conglomerates)

        def show_data(grouped_data, ungrouped_data, grouped_data2, ungrouped_data2):

            label_grouped_data = Label(window, text=f'DATOS AGRUPADOS\n\n'
                                                    f'Mediana: {grouped_data["grouped_median"]}\n'
                                                    f'Media aritmética: {grouped_data["arith_mean_a"]}\n'
                                                    f'Moda: {grouped_data["grouped_mode"]}\n'
                                                    f'Rango: {grouped_data["range_class"]}\n'
                                                    f'Varianza: {grouped_data["variance_on"]}\n'
                                                    f'Desviacion estandar: {grouped_data["unstandar_deviation"]}\n'
                                                    f'El sesgo con datos agruapdos es: {grouped_data["grouped_bias"]}')

            label_ungrouped_data = Label(window, text=f'DATOS NO AGRUPADOS\n\n'
                                                      f'Media aritmética: {ungrouped_data["arith_mean_not_a"]}\n'
                                                      f'Media truncada: {ungrouped_data["truncated"]} \n'
                                                      f'Media geométrica: {ungrouped_data["geome_mean"]}\n'
                                                      # f'Media temporal: {ungrouped_data["temp"]}\n'
                                                      f'Mediana: {ungrouped_data["ungrouped_median"]}\n'
                                                      f'Moda: {ungrouped_data["ungrouped_mode"]}\n'
                                                      f'Rango: {ungrouped_data["range_class"]}\n'
                                                      f'El sesgo con datos no agrupados es: {ungrouped_data["ungrouped_bias"]}\n'
                                                      f'Varianza: {ungrouped_data["variance_un"]}\n'
                                                      f'La desviación estandar es: {ungrouped_data["standard_deviation"]}')

            label_grouped_data2 = Label(window, text=f'DATOS AGRUPADOS\n\n'
                                                    f'Mediana: {grouped_data2["grouped_median"]}\n'
                                                    f'Media aritmética: {grouped_data2["arith_mean_a"]}\n'
                                                    f'Moda: {grouped_data2["grouped_mode"]}\n'
                                                    f'Rango: {grouped_data2["range_class"]}\n'
                                                    f'Varianza: {grouped_data2["variance_on"]}\n'
                                                    f'Desviacion estandar: {grouped_data2["unstandar_deviation"]}\n'
                                                    f'El sesgo con datos agruapdos es: {grouped_data2["grouped_bias"]}')

            label_ungrouped_data2 = Label(window, text=f'DATOS NO AGRUPADOS\n\n'
                                                      f'Media aritmética: {ungrouped_data2["arith_mean_not_a"]}\n'
                                                      f'Media truncada: {ungrouped_data2["truncated"]} \n'
                                                      f'Media geométrica: {ungrouped_data2["geome_mean"]}\n'
                                                    # f'Media temporal: {ungrouped_data["temp"]}\n'
                                                      f'Mediana: {ungrouped_data2["ungrouped_median"]}\n'
                                                      f'Moda: {ungrouped_data2["ungrouped_mode"]}\n'
                                                      f'Rango: {ungrouped_data2["range_class"]}\n'
                                                      f'El sesgo con datos no agrupados es: {ungrouped_data2["ungrouped_bias"]}\n'
                                                      f'Varianza: {ungrouped_data2["variance_un"]}\n'
                                                      f'La desviación estandar es: {ungrouped_data2["standard_deviation"]}')

            label_grouped_data.place(x=50, y=400)
            label_ungrouped_data.place(x=350, y=400)
            label_grouped_data2.place(x=50, y=500)
            label_ungrouped_data2.place(x=350, y=500)


        def data_e_p(column_values, conglomera, type_data):
            number_class = do.number_class(len(column_values))
            range_class = do.range_method(column_values)
            class_width = do.class_width(range_class, number_class)
            lower_limits = do.limit_inf(column_values, class_width)
            upper_limits = do.limit_sup(lower_limits, class_width)
            class_marks = do.class_marks(lower_limits, upper_limits)
            freq_abs = do.frec_absolute(column_values, lower_limits, upper_limits)
            arith_mean_a, arith_mean_not_a = do.arithmetic_mean(column_values, type_data)
            grouped_median = do.grouped_median(class_marks)
            ungrouped_median = do.ungrouped_median(column_values)
            grouped_mode = do.grouped_mode(class_marks, freq_abs)
            ungrouped_mode = do.ungrouped_mode(column_values)
            grouped_bias = do.bias(arith_mean_a, grouped_median, grouped_mode)
            ungrouped_bias = do.bias(arith_mean_not_a, ungrouped_median, ungrouped_mode)
            variance_un = do.ungrouped_variance(column_values, arith_mean_not_a)
            standard_deviation = do.standard_deviation(variance_un)
            variance_on = do.grouped_variance(column_values, arith_mean_a)
            unstandard_deviation = do.unstandard_deviation(variance_on)
            geome_mean = do.ungrouped_geometric_mean(column_values)
            truncated = do.half_truncated(column_values, 0.1)
            temp = do.temporal_mean(column_values, 71)

            number_class2 = do.number_class(len(conglomera))
            range_class2 = do.range_method(conglomera)
            class_width2 = do.class_width(range_class2, number_class2)
            lower_limits2 = do.limit_inf(conglomera, class_width2)
            upper_limits2 = do.limit_sup(lower_limits2, class_width2)
            class_marks2 = do.class_marks(lower_limits2, upper_limits2)
            freq_abs2 = do.frec_absolute(conglomera, lower_limits2, upper_limits2)
            arith_mean_a2, arith_mean_not_a2 = do.arithmetic_mean(conglomera, type_data)
            grouped_median2 = do.grouped_median(class_marks2)
            ungrouped_median2 = do.ungrouped_median(conglomera)
            grouped_mode2 = do.grouped_mode(class_marks2, freq_abs2)
            ungrouped_mode2 = do.ungrouped_mode(conglomera)
            grouped_bias2 = do.bias(arith_mean_a2, grouped_median2, grouped_mode2)
            ungrouped_bias2 = do.bias(arith_mean_not_a2, ungrouped_median2, ungrouped_mode2)
            variance_un2 = do.ungrouped_variance(conglomera, arith_mean_not_a2)
            standard_deviation2 = do.standard_deviation(variance_un2)
            variance_on2 = do.grouped_variance(conglomera, arith_mean_a2)
            unstandard_deviation2 = do.unstandard_deviation(variance_on2)
            geome_mean2 = do.ungrouped_geometric_mean(conglomera)
            truncated2 = do.half_truncated(conglomera, 0.1)
            temp2 = do.temporal_mean(conglomera, 71)

            grouped_data = {
                "grouped_median": grouped_median,
                "arith_mean_a": arith_mean_a,
                "grouped_mode": grouped_mode,
                "range_class": range_class,
                "variance_on": variance_on,
                "unstandar_deviation": unstandard_deviation,
                "grouped_bias": grouped_bias
            }

            ungrouped_data = {
                "arith_mean_not_a": arith_mean_not_a,
                "truncated": truncated,
                "geome_mean": geome_mean,
                # "temp": temp,
                "ungrouped_median": ungrouped_median,
                "ungrouped_mode": ungrouped_mode,
                "range_class": range_class,
                "ungrouped_bias": ungrouped_bias,
                "variance_un": variance_un,
                "standard_deviation": standard_deviation
            }

            grouped_data2 = {
                "grouped_median": grouped_median2,
                "arith_mean_a": arith_mean_a2,
                "grouped_mode": grouped_mode,
                "range_class": range_class2,
                "variance_on": variance_on2,
                "unstandar_deviation": unstandard_deviation2,
                "grouped_bias": grouped_bias2
            }

            ungrouped_data2 = {
                "arith_mean_not_a": arith_mean_not_a,
                "truncated": truncated2,
                "geome_mean": geome_mean2,
                # "temp": temp,
                "ungrouped_median": ungrouped_median2,
                "ungrouped_mode": ungrouped_mode2,
                "range_class": range_class2,
                "ungrouped_bias": ungrouped_bias2,
                "variance_un": variance_un2,
                "standard_deviation": standard_deviation2
            }

            return grouped_data, ungrouped_data, grouped_data2, ungrouped_data2


        def crate_column_graph():
            selected_column = combobox_attributes.get()
            column_values = content[selected_column]
            type_data = content[selected_column].dtype
            conglomera = conglo(column_values)

            grouped_data, ungrouped_data, grouped_data2, ungrouped_data2 = data_e_p(column_values, conglomera, type_data)

            show_data(grouped_data, ungrouped_data, grouped_data2, ungrouped_data2)
            graphs = combobox_graph.get()

            if graphs == "Histograma":
                graphics.histogram_plot(column_values, canvas)
                create_frequency_table(column_values, type_data, graphs)
            elif graphs == "Polígono de frecuencias":
                graphics.frequency_polygon_graph(column_values, canvas)
                create_frequency_table(column_values, type_data, graphs)
            elif graphs == "Ojivas":
                graphics.warhead_graph(column_values, canvas)
                create_frequency_table(column_values, type_data, graphs)
            elif graphs == "Gráfica de barras":
                graphics.bar_graph(column_values, canvas)
                create_frequency_table(column_values, type_data, graphs)
            elif graphs == "Gráfica de pastel":
                graphics.pie_chart(column_values, canvas)
                create_frequency_table(column_values, type_data, graphs)
                graphics.temporal_mean_g(column_values, 13, canvas)
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

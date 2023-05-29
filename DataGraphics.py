import matplotlib.pyplot as plt
import numpy as np
import DataOperations as do


def histogram_plot(column_values, canvas):
    plt.close()
    total_value = do.total_value(column_values.__len__())
    number_class = do.number_class(total_value)
    range = do.range_method(column_values)
    class_width = do.class_width(range, number_class)
    limit_inf = do.limit_inf(column_values, class_width)
    limit_sup = do.limit_sup(limit_inf, class_width)
    classMarks = do.class_marks(limit_inf, limit_sup)
    frecAbsolutas = do.frec_absolute(column_values, limit_inf, limit_sup)
    fig, ax = plt.subplots(figsize=(9.3, 11.6), dpi=60)
    x = np.arange(len(classMarks))
    ax.bar(x, frecAbsolutas, align='center', edgecolor="black")
    ax.set_xticks(x, labels=classMarks)
    fig.savefig("./GraphicsExports/histogram-graphic.png")
    canvas.figure = fig
    canvas.draw()


def frequency_polygon_graph(column_values, canvas):
    plt.close()
    total_value = do.total_value(column_values.__len__())
    number_class = do.number_class(total_value)
    range = do.range_method(column_values)
    class_width = do.class_width(range, number_class)
    limit_inf = do.limit_inf(column_values, class_width)
    limit_sup = do.limit_sup(limit_inf, class_width)
    classMarks = do.class_marks(limit_inf, limit_sup)
    frecAbsolutas = do.frec_absolute(column_values, limit_inf, limit_sup)
    frecRelative = do.frequency_relative(frecAbsolutas)
    frecRelative = np.insert(frecRelative, 0, 0)
    frecRelative = np.append(frecRelative, 0)
    classMarks.insert(0, 0)
    classMarks.append(0)
    frec_relative = frecRelative[0:] * 100
    fig, ax = plt.subplots(figsize=(9.3, 11.6), dpi=60)
    x = np.arange(len(classMarks))
    ax.plot(x, frec_relative, marker="o")
    ax.set_xticks(x, labels=classMarks)
    fig.savefig("./GraphicsExports/f-polygon-graphic.png")
    canvas.figure = fig
    canvas.draw()


def warhead_graph(column_values, canvas):
    plt.close()
    total_value = do.total_value(column_values.__len__())
    number_class = do.number_class(total_value)
    range = do.range_method(column_values)
    class_width = do.class_width(range, number_class)
    limit_inf = do.limit_inf(column_values, class_width)
    limit_sup = do.limit_sup(limit_inf, class_width)
    classMarks = do.class_marks(limit_inf, limit_sup)
    frecAbsolutas = do.frec_absolute(column_values, limit_inf, limit_sup)
    frecRelative = do.frequency_relative(frecAbsolutas)
    frecRelativeAccum = do.frequency_relative_accumulate(frecRelative)
    frec_RelativeAccum = np.insert(frecRelativeAccum, 0, 0)
    frec_RelativeAccum = frec_RelativeAccum[0:] * 100
    classMarks.insert(0, 0)
    fig, ax = plt.subplots(figsize=(9.3, 11.6), dpi=60)
    x = np.arange(len(classMarks))
    ax.plot(x, frec_RelativeAccum, marker="o")
    ax.set_xticks(x, labels=classMarks)
    fig.savefig("./GraphicsExports/warhead-graphic.png")
    canvas.figure = fig
    canvas.draw()


def bar_graph(data, canvas):
    plt.close()
    data_bar = data.value_counts()
    y = np.arange(len(data_bar.index[0:]))
    fig, ax = plt.subplots(figsize=(9.3, 11.6), dpi=60)
    ax.barh(y, data_bar)
    ax.set_yticks(y, labels=data_bar.index)
    fig.savefig("./GraphicsExports/bar-graphic.png")
    canvas.figure = fig
    canvas.draw()


def pie_chart(data, canvas):
    plt.close()
    data_pie = data.value_counts()
    frequency_relative = do.frequency_relative(data_pie.values) * 100
    fig, ax = plt.subplots(figsize=(9.3, 11.6), dpi=60)
    ax.pie(frequency_relative, labels=data_pie.values[0:], autopct='%1.1f%%', shadow=True)
    ax.legend(data_pie.index.tolist(), title="Data", loc="upper left")
    fig.savefig("./GraphicsExports/pie-graphic.png")
    canvas.figure = fig
    canvas.draw()


def temporal_mean_g(column_values, window, canvas):
    plt.close()
    temporal = do.temporal_mean(column_values, window)
    fig, ax = plt.subplots(figsize=(9.3, 11.6), dpi=60)
    x = np.arange(len(temporal))
    ax.plot(column_values)
    ax.plot(x, temporal)
    ax.set_xticks(x, labels=temporal)
    fig.savefig("./GraphicsExports/warhead-graphic.png")
    canvas.figure = fig
    canvas.draw()

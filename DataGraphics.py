import matplotlib.pyplot as plt
import numpy as np
import DataOperations as do


def histogram_plot(frecAbsolutas, classMarks, canvas):
    fig, ax = plt.subplots(figsize=(9.3, 11.6), dpi=60)
    x = np.arange(len(classMarks))
    ax.bar(x, frecAbsolutas, align='center', edgecolor="black")
    ax.set_xticks(x, labels=classMarks)
    fig.savefig("./GraphicsExports/histogram-graphic.png")
    canvas.figure = fig
    canvas.draw()


def frequency_polygon_graph(frecRelative, classMarks, canvas):
    plt.clf()
    frecRelative = np.insert(frecRelative, 0, 0)
    frecRelative = np.append(frecRelative, 0)
    classMarks.insert(0, 0)
    classMarks.append(0)
    frec_relative = frecRelative[0:] * 100
    fig, ax = plt.subplots(figsize=(9.3, 11.6), dpi=60)
    x = np.arange(len(classMarks))
    ax.plot(x, frec_relative, marker="o")
    # ax.tick_params(axis='x', rotation=30)
    ax.set_xticks(x, labels=classMarks)
    fig.savefig("./GraphicsExports/f-polygon-graphic.png")
    canvas.figure = fig
    canvas.draw()


def warhead_graph(frecRelativeAccum, classMarks, canvas):
    plt.clf()
    frec_RelativeAccum = np.insert(frecRelativeAccum, 0, 0)
    classMarks.insert(0, 0)
    fig, ax = plt.subplots(figsize=(9.3, 11.6), dpi=60)
    x = np.arange(len(classMarks))
    ax.plot(x, frec_RelativeAccum, marker="o")
    # plt.plot(accumulative, valueIndex[::-1], 'o')
    ax.set_xticks(x, labels=classMarks)
    fig.savefig("./GraphicsExports/warhead-graphic.png")
    canvas.figure = fig
    canvas.draw()


# ME FALTA DESORDENAR LA GRAFICA
def bar_graph(data, canvas):
    data_bar = data.value_counts()
    y = np.arange(len(data_bar.index[0:]))
    fig, ax = plt.subplots(figsize=(9.3, 11.6), dpi=60)
    ax.barh(y, data_bar)
    ax.set_yticks(y, labels=data_bar.index)
    fig.savefig("./GraphicsExports/bar-graphic.png")
    canvas.figure = fig
    canvas.draw()


def pie_chart(data, canvas):
    data_pie = data.value_counts()
    frequency_relative = do.frequency_relative(data_pie) * 100
    fig, ax = plt.subplots(figsize=(9.3, 11.6), dpi=60)
    # %0.f%
    ax.pie(frequency_relative, labels=data_pie.values[0:], autopct='%1.1f%%', shadow=True)
    ax.legend(data_pie.index.tolist(), title="Data", loc="upper left")
    fig.savefig("./GraphicsExports/pie-graphic.png")
    canvas.figure = fig
    canvas.draw()

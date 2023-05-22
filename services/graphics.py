import matplotlib.pyplot as plt
import numpy as np


def histogram_plot(frecAbsolutas, classMarks, canvas):
    print(frecAbsolutas)
    print(classMarks)
    fig, ax = plt.subplots()
    ax.bar(classMarks, frecAbsolutas, width=classMarks[1]-classMarks[0], align='center', edgecolor="black")
    canvas.figure = fig
    canvas.draw()


def frequency_polygon_graph(data, valueIndex, canvas):
    plt.clf()
    print(data)
    frec_relative = (data / sum(data))*100
    print(frec_relative.sum().__round__())
    fig, ax = plt.subplots(figsize=(8.5, 6.5), dpi=75)
    ax.plot(valueIndex, frec_relative, marker="o")
    ax.tick_params(axis='x', rotation=30)
    canvas.figure = fig
    canvas.draw()


def warhead_graph(data, valueIndex, canvas):
    plt.clf()
    frec_relative = (data / sum(data))
    accumulative = np.cumsum(frec_relative)
    print(accumulative)
    plt.plot(accumulative, valueIndex[::-1], 'bo-')
    canvas.draw()


def bar_graph(data, valueIndex, canvas):
    print(data)
    fig, ax = plt.subplots(figsize=(8.5, 7), dpi=75)
    ax.barh(valueIndex, data)
    canvas.figure = fig
    canvas.draw()


def pie_chart(data, valueIndex, canvas):
    print(valueIndex)
    fig, axs = plt.subplots(figsize=(10, 8), dpi=60)
    axs.pie(data, labels=valueIndex, autopct='%.0f%%', shadow=True)
    axs.legend(valueIndex, title="Data", loc="best")
    canvas.figure = fig
    canvas.draw()

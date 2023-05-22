import matplotlib.pyplot as plt
import numpy as np

null = 0


def histogram_plot(frecAbsolutas, classMarks, canvas):
    fig, ax = plt.subplots(figsize=(10, 8), dpi=60)
    bins = np.arange(len(classMarks) + 1)
    ax.hist(frecAbsolutas[:-1], bins=bins, edgecolor="black")
    # fig, ax = plt.subplots(figsize=(10, 8), dpi=60)
    # bins = np.arange(len(classMarks) + 1)
    # ax.hist(frecAbsolutas[:-1], bins=len(frecAbsolutas), edgecolor="black")
    ax.set_xticks(frecAbsolutas[:-1])
    ax.set_xticklabels(frecAbsolutas[:-1])
    plt.show()
    canvas.figure = fig
    canvas.draw()

    # fig, ax = plt.subplots()
    # ax.hist(frecAbsolutas, bins=len(classMarks), edgecolor="white")
    # canvas.figure = fig
    # canvas.draw()


def frequency_polygon_graph(data, valueIndex, canvas):
    print(data)
    # print("------")
    print(valueIndex)
    fig, ax = plt.subplots(figsize=(8.5, 7), dpi=75)
    ax.plot(valueIndex, data, marker="o")
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

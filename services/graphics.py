import pandas as pd
import matplotlib.pyplot as plt

null = 0
def histogram_plot(data):
    return null

def frequency_polygon_graph(data):
    return null

def warhead_graph(data):
    return null

def bar_graph(data, canvas):
    plt.clf()
    plt.barh(data, height=1, width=10000)
    canvas.draw()

def pie_chart(data, canvas):
    plt.clf()
    plt.pie(data, autopct='%1.1f%%')
    canvas.draw()

import math
import numpy as np


def number_class(amount_data):
    amount_data = int(amount_data)
    nc = 1 + 3.3 * math.log(amount_data)
    return nc.__round__()


def range_method(data):
    print(max(data))
    print(min(data))
    rango = max(data) - min(data)
    return rango


def class_width(rangeMethod, numberClass):
    cw = rangeMethod / numberClass
    return cw.__round__()


def total_value(totalValue):
    return totalValue


def class_marks(limitInf, limitSup):
    i = 0
    class_marks = []
    for element in limitInf:
        cm = (element + limitSup[i]) / 2
        class_marks.append(cm)
        i = i + 1
    return class_marks


def limit_inf(data, classWidth):
    lower_limits = np.arange(np.min(data), np.max(data), classWidth + 1)
    return lower_limits


def limit_sup(lowerLimits, classWidth):
    lowerLimits = np.array(lowerLimits)
    upper_limits = lowerLimits + classWidth
    return upper_limits


def frec_absolute(data, num_classes):
    frequencies, _ = np.histogram(data, bins=num_classes, range=(np.min(data), np.max(data)))
    return frequencies


def frequency_relative(data):
    print(data)
    freq_relative = data.values[:-1] / sum(data.values)
    print(freq_relative)
    return freq_relative

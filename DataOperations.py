import math
import numpy as np
import pandas as pd


def number_class(amount_data):
    amount_data = int(amount_data)
    nc = 1 + (3.3 * math.log10(amount_data))
    return nc.__round__()


def range_method(data):
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


def frec_absolute(data, lower_limit, upper_limit):
    ranges = pd.IntervalIndex.from_arrays(lower_limit, upper_limit, closed="both")
    frequency = pd.cut(data, bins=ranges, include_lowest=True).value_counts().sort_index()
    # frequencies, _ = np.histogram(data, bins=num_classes - 1, range=(np.min(data), np.max(data)))
    return frequency


def frequency_relative(data):
    freq_relative = data.values[0:] / sum(data.values)
    return freq_relative


def frequency_relative_accumulate(frecRelative):
    frec_relative_accum = np.cumsum(frecRelative)
    return frec_relative_accum

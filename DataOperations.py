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
    lower_limit = []
    for i in range(number_class(len(data))):
        if i == 0:
            value = min(data)
        else:
            value = min(data) + (i * classWidth) + i

        lower_limit.append(value)
    return lower_limit


def limit_sup(lowerLimits, classWidth):
    limits_sup = [limit + classWidth for limit in lowerLimits]
    return limits_sup


def frec_absolute(data, lower_limit, upper_limit):
    ranges = pd.IntervalIndex.from_arrays(lower_limit, upper_limit, closed="both")
    frequency = pd.cut(data, bins=ranges, include_lowest=True).value_counts().sort_index()
    return frequency


def frec_abs_acumm(frecAbs):
    frec_relative_accum = np.cumsum(frecAbs)
    return frec_relative_accum


def frequency_relative(data):
    freq_relative = data[0:] / sum(data)
    return freq_relative


def frequency_relative_accumulate(frecRelative):
    frec_relative_accum = np.cumsum(frecRelative)
    return frec_relative_accum

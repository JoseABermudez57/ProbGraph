import math
from statistics import median, mode, variance, pvariance, median_grouped, geometric_mean
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


def arithmetic_mean(data, type_data):
    n = number_class(len(data))
    r = range_method(data)
    cw = class_width(r, n)
    li = limit_inf(data, cw)
    ls = limit_sup(li, cw)
    clas_marks = class_marks(li, ls)
    freq_absolute = frec_absolute(data, li, ls)
    i = 0
    abs_marks = []
    total = 0
    for freq in freq_absolute.values:
        fm = freq * clas_marks[i]
        abs_marks.append(fm)
        total = total + abs_marks[i]
        i = i + 1
    am = total / len(data)
    media = sum(p * f for p, f in zip(clas_marks, freq_absolute)) / sum(freq_absolute)
    print("mediaaaaa agrupasa", media)
    # me
    # else:
    i = 0
    sum_total_data_values = sum(data.values[i:])
    amn = sum_total_data_values / len(data)
    return am, amn


def grouped_median(class_marks):
    return median(class_marks)


def grouped_mode(class_marks, freq_abs):
    values = list(freq_abs.values)
    index_max_value = values.index(max(values))
    return class_marks[index_max_value]


def ungrouped_median(column_values):
    return median(sorted(column_values))


def ungrouped_mode(column_values):
    return mode(column_values)


def bias(mean, median, mode):
    if mean < median < mode:
        return "Sesgado a la derecha"
    elif mean == median == mode:
        return "Simétrico"
    elif mode < median < mean:
        return "Sesgado a la izquierda"
    else:
        return "Indeterminado"


def ungrouped_variance(data, mean):
    return pvariance(data.values, mean)


def grouped_variance(data, mean):
    n = number_class(len(data))
    r = range_method(data)
    cw = class_width(r, n)
    li = limit_inf(data, cw)
    ls = limit_sup(li, cw)
    clas_marks = class_marks(li, ls)
    freq_absolute = frec_absolute(data, li, ls)
    i = 0
    abs_marks = []
    cmq = []
    total = 0
    for freq in freq_absolute.values:
        cmqp = clas_marks[i] ** 2
        print(cmqp)
        cmq.append(cmqp)
        fm = freq * cmq[i]
        print(fm)
        abs_marks.append(fm)
        total = total + abs_marks[i]
        print(total)
        i = i + 1
    headquarter = mean ** 2
    upper = total - (len(data) * headquarter)
    variance_grouped = upper / len(data) - 1
    return variance_grouped


def ungrouped_geometric_mean(data):
    media_geometrica = geometric_mean(data)
    return media_geometrica


def temporal(data):
    serie = pd.Series(data)
    media_temporal = serie.rolling(window=3).mean()
    return media_temporal


def standard_deviation(variance):
    return math.sqrt(variance)

"""
3.1.2 Задача 2: Среднее по списку

Создайте список случайных значений и найдите для него: среднее,
дисперсию и медиану.
Выведите список этих чисел и полученные значения.
"""
# -*- coding: utf-8 -*-

import random
import statistics  # модуль для вычисления среднего, медианы, дисперсии

# Создаём список из 100 случайных значений с нормальным распределением
# (ср. = 3, σ = 1)
values = [random.normalvariate(3, 1) for _ in range(100)]

# среднее арифметическое
mean_val = statistics.mean(values)
# выборочная дисперсия (по умолчанию ddof=1)
variance_val = statistics.variance(values)
# медиана
median_val = statistics.median(values)

# Выводим результаты
print("Список значений:")
print(values)
print("\nСтатистики:")
print("Среднее: {:.5f}".format(mean_val))
print("Дисперсия: {:.5f}".format(variance_val))
print("Медиана: {:.5f}".format(median_val))

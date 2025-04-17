"""
Created on Thu Apr 17 03:36:22 2025

    Демонстрационный файл лабораторных работ по Информатике,

    студента: Никифорова О.В.
    группы: ЗИИИм-11

    каф. АСОиУ.

    Лабораторная работа 3, Numpy. Array

@licence: GPL
@author: Никифорова О.В.
"""
# -*- coding: utf-8 -*-

import numpy as np

shape = (2, 3)
object = [[2, 3], [3, 5], [4, 6], [5, 7]]
n = 5
m = 4

# Способ 1 – создание матрицы из объекта (двумерного списка целых чисел).
arr1 = np.array(object, dtype=np.float)
print("Способ 1:\n", arr1)

# Способ 2 – создание матрицы нулей размера shape.
arr2 = np.zeros(shape, dtype=np.float)
print("Способ 2:\n", arr2)

# Способ 3 – создание матрицы единиц размера shape.
arr3 = np.ones(shape, dtype=np.float)
print("Способ 3:\n", arr3)

# Способ 4 – создание "пустой" матрицы размера shape (ячейки размечены в памяти, но не инициализированы).
arr4 = np.empty(shape, dtype=np.float)
print("Способ 4:\n", arr4)

# Способ 5 – создание "пустой" матрицы по размерам другой матрицы.
arr5 = np.empty_like(arr1, dtype=np.float)
print("Способ 5:\n", arr5)

# Способ 6 – создание матрицы нулей по размеру другой матрицы.
arr6 = np.zeros_like(arr1, dtype=np.float)
print("Способ 6:\n", arr6)

# Способ 7 – создание матрицы единиц по размеру другой матрицы.
arr7 = np.ones_like(arr1, dtype=np.float)
print("Способ 7:\n", arr7)

# Способ 8 – создание единичной квадратной матрицы со стороной n.
arr8 = np.identity(n, dtype=np.float)
print("Способ 8:\n", arr8)

# Способ 9 – создание "особой" единичной матрицы (матрицы-глаза) размером n x m с диагональю k.
arr9 = np.eye(n, m, k=1, dtype=np.float)
print("Способ 9:\n", arr9)

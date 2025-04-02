"""
Created on Mon Mar 31 13:30:06 2025

    Демонстрационный файл лабораторных работ по Информатике,

    студента: Никифорова О.В.
    группы: ЗИИИм-11

    каф. АСОиУ.

    Лабораторная работа 1, Основы Python
    Упражнение 4, Тесты и автотесты.

@licence: GPL
@author: Никифорова О.В.
"""# -*- coding: utf-8 -*-

import numpy as np

# Функция сложения любого количества аргументов
def add(*args):
    if len(args) == 0:
        return None  # если ничего не передано — возвращаем None
    result = args[0]  # начинаем с первого элемента
    for arg in args[1:]:  # перебираем остальные
        result += arg  # складываем
    return result

# Функция вычитания
def subs(*args):
    if len(args) == 0:
        return None
    result = args[0]
    for arg in args[1:]:
        result -= arg
    return result

# Функция умножения
def multiply(*args):
    if len(args) == 0:
        return None
    result = args[0]
    for arg in args[1:]:
        result *= arg
    return result

# Функция деления: первый аргумент — делимое, остальные — делители
def div(A, *args):
    result = A
    for arg in args:
        if isinstance(arg, np.ndarray):
            if np.any(arg == 0):
                return "Ошибка: деление на ноль"
        elif arg == 0:
                return "Ошибка: деление на ноль"
        result /= arg
    return result

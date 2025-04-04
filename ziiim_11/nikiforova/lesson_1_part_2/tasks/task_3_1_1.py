"""
3.1.1 Задача 1: Решение квадратного уравнения

Создайте программу решения квадратного уравнения:
    
Пользователь вводит коэффициенты уравнения, 
а программа выводит его корни, если есть.
Если корней нет, выводится текст «нет корней» 
и выводит значение дискриминанта.
"""
# -*- coding: utf-8 -*-

import math  # Импортируем модуль для работы с квадратным корнем


def solve_quadratic(a, b, c):
    """
    Решает квадратное уравнение ax^2 + bx + c = 0
    и выводит корни, если они есть.
    Если нет — сообщает об этом и показывает дискриминант.
    """
    D = b ** 2 - 4 * a * c  # Вычисление дискриминанта

    if D < 0:
        print("Нет корней")
        print("D={}".format(D))
    elif D == 0:
        x = -b / (2 * a)
        print("Один корень: {:.5f}".format(x))
    else:
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)
        print("Корень 1: {:.5f}".format(x1))
        print("Корень 2: {:.5f}".format(x2))


def solve_quadratic_run():
    # Ввод коэффициентов уравнения от пользователя
    a = float(input("Коэффициент 1: "))  # коэффициент при x^2
    b = float(input("Коэффициент 2: "))  # коэффициент при x
    c = float(input("Коэффициент 3: "))  # свободный член
    
    solve_quadratic(a,b,c)

# solve_quadratic_run()
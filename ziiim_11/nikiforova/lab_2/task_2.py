"""
### 3.2.2 Задача 2: "Квадратное уравнение с графиком"
    
Добавьте в программу из задания 1 из первой лабораторной рисование
параболы и точек, соответствующих корням (если есть). 
"""
# -*- coding: utf-8 -*-

import math
import numpy as np
import matplotlib.pyplot as plt

def solve_quadratic(a, b, c):
    """
    Решает квадратное уравнение ax^2 + bx + c = 0
    и возвращает корни (или None), и дискриминант.
    """
    D = b ** 2 - 4 * a * c

    if D < 0:
        print("Нет корней")
        print("D={}".format(D))
        return None, D
    elif D == 0:
        x = -b / (2 * a)
        print("Один корень: {:.5f}".format(x))
        return [x], D
    else:
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)
        print("Корень 1: {:.5f}".format(x1))
        print("Корень 2: {:.5f}".format(x2))
        return [x1, x2], D


def solve_quadratic_run():
    # Ввод коэффициентов
    a = float(input("Коэффициент 1 (a): "))
    b = float(input("Коэффициент 2 (b): "))
    c = float(input("Коэффициент 3 (c): "))

    # Решаем уравнение и получаем корни
    roots, D = solve_quadratic(a, b, c)

    # Строим график параболы
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c
    plt.plot(x, y, label='Парабола')

    # Добавляем оси
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    # Добавляем корни, если они есть
    if roots:
        for r in roots:
            plt.plot(r, 0, 'ro', label='Корень: {:.2f}'.format(r))

    plt.title('График квадратного уравнения')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()


solve_quadratic_run()

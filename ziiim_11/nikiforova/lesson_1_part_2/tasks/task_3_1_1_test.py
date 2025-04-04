# -*- coding: utf-8 -*-

import task_3_1

# Тест 1: D < 0
print("Тест 1: a=1, b=5, c=10")
task_3_1.solve_quadratic(1, 5, 10)
print()

# Тест 2: D > 0
print("Тест 2: a=2, b=6, c=-1")
task_3_1.solve_quadratic(2, 6, -1)
print()

# Тест 3: D == 0
print("Тест 3: a=1, b=2, c=1")
task_3_1.solve_quadratic(1, 2, 1)
print()
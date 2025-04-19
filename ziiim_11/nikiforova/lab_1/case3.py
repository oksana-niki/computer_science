import random

"""
3.1.3 Задача 3: Поэлементные операции со списками

Создаются два списка A и B из случайных значений (нормальное распределение N(3,1)).
Осуществляется поэлементное:
- сложение
- вычитание
- умножение
- деление
Результат сохраняется в список C и выводится в консоль.
"""

# Генерация случайных списков A и B
A = [random.normalvariate(3, 1) for _ in range(100)]
B = [random.normalvariate(3, 1) for _ in range(100)]

# Функции поэлементных операций
def add_lists(a, b):
    C = [a[i] + b[i] for i in range(len(a))]
    return C

def subtract_lists(a, b):
    C = [a[i] - b[i] for i in range(len(a))]
    return C

def multiply_lists(a, b):
    C = [a[i] * b[i] for i in range(len(a))]
    return C

def divide_lists(a, b):
    C = []
    for i in range(len(a)):
        if b[i] != 0:
            C.append(a[i] / b[i])
        else:
            C.append(None)  # защита от деления на 0
    return C

# Результаты
sum_list = add_lists(A, B)
diff_list = subtract_lists(A, B)
prod_list = multiply_lists(A, B)
div_list = divide_lists(A, B)

# Вывод примеров
print("Первые 5 элементов списка A:", A[:5])
print("Первые 5 элементов списка B:", B[:5])
print("Сумма (первые 5):", sum_list[:5])
print("Разность (первые 5):", diff_list[:5])
print("Произведение (первые 5):", prod_list[:5])
print("Частное (первые 5):", div_list[:5])

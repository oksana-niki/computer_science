"""
### 3.3.1. Задача 1: "Трансформация матриц в numpy"

Создайте две матрицы по формулам,
воспользовавшись типом «numpy.array(some_list)» и
командой «numpy.fromfunction(function)», для них вычислите:

- Вычислите Aᵀ и Bᵀ;
- Вычислите A + B;
- Вычислите A - B;
- Вычислите A * B и B * A;
- Вычислите A / B и B / A;
- Вычислите A // B и B // A;
- Вычислите A⁻¹ и B⁻¹;
- Вычислите A * B⁻¹ и B * A⁻¹;
- Вычислите значение 2Aᵀ - E, где E — единичная матрица, размера MxN, при том,
что изначально матрица A имеет размер NxM.
- Вычислите значение многочлена 𝑓(𝑥) = 𝑥³ − 7𝑥² + 13𝑥 − 5, если 𝑥 — это матрицы A и B;
- Вычислите значения функции 1 и функции 2 из Таблицы 2 для матриц A и B;
- Вычислите значения функции 3 из Таблицы 2, приняв что переменная
«у» — это матрица A, а переменная «𝑥𝑥» — это матрица B;

При этом учтите, что здесь знак «*» обозначает матричное умножение,
а не поэлементное.
"""
# -*- coding: utf-8 -*-

import numpy as np
import math

# Установка параметров для красивого вывода
np.set_printoptions(precision=3, suppress=True)

# ---------- Создание матриц A и B по формулам варианта 1 ----------
# Матрица A[i,j] = (i! - j!) / i!
def A_func(i, j):
    i = i + 1  # Индексация с 1
    j = j + 1
    i_fact = np.vectorize(math.factorial)(i)
    j_fact = np.vectorize(math.factorial)(j)
    return (i_fact - j_fact) / i_fact

# Матрица B[i,j] = (i - j) / (i + j)
def B_func(i, j):
    i = i + 1
    j = j + 1
    with np.errstate(divide='ignore', invalid='ignore'):
        result = (i - j) / (i + j)
        result[(i + j) == 0] = 0
    return result

# Размеры по варианту 1:
# A — 10x20, B — 20x10
A = np.fromfunction(A_func, (10, 20), dtype=int)
B = np.fromfunction(B_func, (20, 10), dtype=int)

# ---------------- Операции по заданию ---------------- #

# 1. Вычислите: Aᵀ и Bᵀ
print("1. Транспонированные матрицы A.T и B.T:")
print("A.T:\n", A.T)
print("\nB.T:\n", B.T)

# 2. Вычислите: A + B
print("\n2. A + B (приводим к одинаковому размеру 10x10):")
A_small = A[:, :10]
B_small = B[:10, :]
print(A_small + B_small)

# 3. Вычислите: A - B
print("\n3. A - B:")
print(A_small - B_small)

# 4. Вычислите: A * B и B * A (поэлементно)
print("\n4. A * B (поэлементно):")
print(A_small * B_small)
print("\n4. B * A (поэлементно):")
print(B_small * A_small)
print("\n4a. A @ B (матричное умножение):")
print(A_small @ B_small)
print("\n4a. B @ A (матричное умножение):")
print(B_small @ A_small)

# 5. Вычислите: A / B и B / A (поэлементно)
print("\n5. A / B:")
print(np.divide(A_small, B_small, where=B_small!=0))
print("\n5. B / A:")
print(np.divide(B_small, A_small, where=A_small!=0))

# 6. Вычислите: A // B и B // A (целочисленное деление)
print("\n6. A // B (целочисленно):")
with np.errstate(divide='ignore', invalid='ignore'):
    result1 = np.floor_divide(A_small, B_small, where=B_small!=0)
    result1[B_small == 0] = 0
print(result1)

print("\n6. B // A (целочисленно):")
with np.errstate(divide='ignore', invalid='ignore'):
    result2 = np.floor_divide(B_small, A_small, where=A_small!=0)
    result2[A_small == 0] = 0
print(result2)

# 7. Вычислите A⁻¹ и B⁻¹
print("\n7. Обратные матрицы A⁻¹ и B⁻¹ (используем квадратные версии):")
A_square = A[:, :10]
B_square = B[:10, :]
try:
    A_inv = np.linalg.inv(A_square)
    B_inv = np.linalg.inv(B_square)
    print("A⁻¹:\n", A_inv)
    print("\nB⁻¹:\n", B_inv)
except np.linalg.LinAlgError:
    print("Матрицы A или B не обратимы")

# 8. Вычислите: A * B⁻¹ и B * A⁻¹
print("\n8. A * B⁻¹ и B * A⁻¹:")
try:
    print("A * B⁻¹:\n", A_square @ B_inv)
    print("\nB * A⁻¹:\n", B_square @ A_inv)
except:
    print("Умножение невозможно из-за формы или необратимости")

# 9. Вычислите 2Aᵀ - E, где E — единичная матрица 10x10
print("\n9. Выражение 2Aᵀ - E:")
E = np.identity(10)
print(2 * A_square.T - E)

# 10. Вычислите значение многочлена f(x) = x³ - 7x² + 13x - 5 для A и B
def poly_f(x):
    return x @ x @ x - 7 * x @ x + 13 * x - 5 * np.identity(x.shape[0])

print("\n10. Многочлен f(x) = x³ - 7x² + 13x - 5 от A:")
try:
    print(poly_f(A_square))
except:
    print("Ошибка вычисления многочлена от A")

print("\n10. Многочлен f(x) = x³ - 7x² + 13x - 5 от B:")
try:
    print(poly_f(B_square))
except:
    print("Ошибка вычисления многочлена от B")

# 11. Вычислите значения функции 1 и функции 2 из Таблицы 2 для матриц A и B
# Таблица 2, Вариант 1:
# Функция 1: y(x) = sin(3x)
# Функция 2: y(x) = 2cos(x)

print("\n11. Функция 1 (y = sin(3x)) для матрицы A:")
print(np.sin(3 * A_small))

print("\n11. Функция 2 (y = 2cos(x)) для матрицы B:")
print(2 * np.cos(B_small))

# 12. Вычислите значения функции 3 из Таблицы 2, приняв:
# переменная «у» — это матрица A, переменная «x» — это матрица B.
# Формула: Z(x, y) = (x! - y!) / x!

print("\n12. Функция 3: Z(x, y) = (x! - y!) / x! где x = B, y = A:")

print("\n12. Функция 3: Z(x, y) = (x! - y!) / x! где x = B, y = A:")

def factorial_safe(mat):
    """Вычисление факториала с защитой от переполнений"""
    mat_int = np.clip(mat.astype(int), 0, 170)  # факториалы >170 не считаем
    return np.vectorize(math.factorial, otypes=[float])(mat_int)

try:
    # Отображаем значения до округления
    print("A_small (как y):\n", np.round(A_small, 2))
    print("B_small (как x):\n", np.round(B_small, 2))

    # Считаем факториалы
    x_fact = factorial_safe(B_small)
    y_fact = factorial_safe(A_small)

    with np.errstate(divide='ignore', invalid='ignore', over='ignore'):
        Z = (x_fact - y_fact) / x_fact
        Z[np.isnan(Z)] = 0
        Z[np.isinf(Z)] = 0
        Z = np.where(x_fact == 0, 0, Z)  # защита от деления на 0

    print("Z = (x! - y!) / x!:\n", np.round(Z, 3))

except Exception as e:
    print("Ошибка при вычислении функции 3:", e)



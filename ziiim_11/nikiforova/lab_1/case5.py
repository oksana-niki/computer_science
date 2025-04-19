"""
3.1.5 Задача 5: Факториал

Напишите функцию вычисления факториала заданного числа.
Она должна принимать на вход число и возвращать его факториал.

Факториал `n!` для целого `n >= 0` определяется как:
    n! = 1 × 2 × 3 × ... × n
    0! = 1 по определению

Для вещественных (и даже отрицательных) значений используется
обобщение факториала через **гамма-функцию**:
    x! = Γ(x + 1), где Γ — гамма-функция Эйлера.

Примеры:
    Ввод: 4      → Вывод: 24
    Ввод: 4.2    → Вывод: 32.57809605
    Ввод: 0      → Вывод: 1
    Ввод: -1     → Вывод: inf
    Ввод: -0.4   → Вывод: 1.489192
"""

import math


def generalized_factorial(x):
    """
    Возвращает факториал числа:
    - для целых n ≥ 0: обычный факториал
    - для всех остальных: через гамма-функцию
    """
    try:
        if x == int(x) and x >= 0:
            return math.factorial(int(x))
        else:
            return math.gamma(x + 1)
    except (ValueError, OverflowError):
        return float('inf')


# ======= Тесты =======
test_cases = {
    4: 24,
    4.2: 32.57809605,
    0: 1,
    -1: float('inf'),
    -0.4: 1.489192,
}

print("\n--- Tests::start ---")
for inp, expected in test_cases.items():
    result = generalized_factorial(inp)
    if isinstance(expected, float):
        match = math.isclose(result, expected, rel_tol=1e-5)
    else:
        match = result == expected
    print(f"Ввод: {inp:<4} → Результат: {result:<.6f} → {'✅ OK' if match else '❌ Ошибка'}")
print("\n--- Tests::end ---")

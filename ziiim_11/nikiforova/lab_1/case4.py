"""
3.1.4 Задача: Поиск простых чисел меньше заданного N
"""

def is_prime(n):
    """Проверка, является ли число простым"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # делители до √n
        if n % i == 0:
            return False
    return True

def primes_less_than(n):
    """Возвращает список простых чисел меньше n"""
    return [x for x in range(2, n) if is_prime(x)]

# ======= Тесты =======
print("\n--- Tests::start ---")
test_cases = {
    10: [2, 3, 5, 7],
    30: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
    1: [],
}

for test_input, expected_output in test_cases.items():
    result = primes_less_than(test_input)
    print(f"Вход: {test_input} → Результат: {result} → {'✅ OK' if result == expected_output else '❌ Ошибка'}")
print("\n--- Tests::end ---")

# ======= Input =======
N = int(input("Максимальное число: "))
print(primes_less_than(N))

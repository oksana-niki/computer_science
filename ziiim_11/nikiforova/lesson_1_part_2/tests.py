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

import counter

import random
import numpy as np
import sys
import traceback

# Глобальный список тестов
tests = []

def addTest():
    # Целые числа от -100 до 100
    intVal1 = random.randint(-100, 100)
    intVal2 = random.randint(-100, 100)

    # Вещественные числа по нормальному распределению (среднее 0, стандартное отклонение 1)
    floatVal1 = random.normalvariate(0, 1)
    floatVal2 = random.normalvariate(0, 1)

    # Комплексные числа с вещественной и мнимой частями из нормального распределения
    compVal1 = complex(random.normalvariate(0, 1), random.normalvariate(0, 1))
    compVal2 = complex(random.normalvariate(0, 1), random.normalvariate(0, 1))

    # Двумерные массивы (матрицы) 4x3 со случайными значениями от 0 до 1
    arrayVal1 = np.random.rand(4, 3)
    arrayVal2 = np.random.rand(4, 3)

    # Векторы (одномерные массивы) с числами от 0 до 3
    vecVal1 = np.array(np.arange(0, 4))
    vecVal2 = np.array(np.arange(0, 4))

    # Предположим, у нас есть объект counter с методом add, который умеет складывать разные типы данных.

    # Сложение целых чисел
    res1 = counter.add(intVal1, intVal2)
    print('sum_int:: \t{0} \t+ \t{1} \t= \t{2}'.format(intVal1, intVal2, res1))
    
    # Сложение чисел с плавающей точкой (float)
    res2 = counter.add(floatVal1, floatVal2)
    print('sum_float:: \t{0} \t+ \t{1} \t= \t{2}'.format(floatVal1, floatVal2, res2))
    
    # Сложение комплексных чисел (например, 1+2j)
    res3 = counter.add(compVal1, compVal2)
    print('sum_comp:: \t{0} \t+ \t{1} \t= \t{2}'.format(compVal1, compVal2, res3))
    
    # Сложение numpy-массивов (numpy array)
    res4 = counter.add(arrayVal1, arrayVal2)
    print('sum_array:: \t{0} \t+ \t{1} \t= \t{2}'.format(arrayVal1, arrayVal2, res4))
    
    # Сложение numpy-векторов (то же, что массивы, просто другой стиль задания)
    res5 = counter.add(vecVal1, vecVal2)
    print('sum_vec:: \t{0} \t+ \t{1} \t= \t{2}'.format(arrayVal1, arrayVal2, res5))  # Тут, похоже, ошибка: должно быть vecVal1, vecVal2


tests.append(addTest)

# Тест для функции вычитания
def subTest():
    pass

tests.append(subTest)

# Тест для функции умножения
def mulTest():
    pass

tests.append(mulTest)

# Тест для функции деления
def divTest():
    pass

tests.append(divTest)

for test in tests:
    test()  # Вызов каждой тестовой функции

# Эта функция запускает серию тестов, которые хранятся в списке tests
def test():
    print('#########################')
    print('Autotester 1.0')
    count = 0

    if len(tests) == 0:
        print('None tests available by now.')
    for test in tests:
        print('* Running test №{0}...'.format(count+1,tests[count]))
        try:
            test()
        except:
            print('Error!')
            print(sys.last_value)
            try:
                inp = int(input('Want traceback? 1-Yes, 2-No:'))
            except:
                pass  # если ввели что-то не то — молча пропускаем
            else:
                if (inp) == 1:
                    try:
                        lim = int(input('How long? (int):'))
                    except:
                        lim = 2
                    finally:
                        exc_type, exc_value, exc_traceback = sys.exc_info()
                        traceback.print_exception(exc_type, exc_value,
                            exc_traceback,
                            limit=lim, file=sys.stdout)
        else:
            print('No errors found.')
        finally:
            print('{0} test completed.'.format(tests[count]))
            count = count + 1
            print('........Done.')
    print('#########################')

# Если этот файл запускается как основная программа — запускаем тесты
if __name__ == '__main__':
    test()


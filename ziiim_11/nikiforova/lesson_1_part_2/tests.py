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
"""
# -*- coding: utf-8 -*-

import counter

import random
import numpy as np
import sys
import traceback

# Глобальный список тестов
tests = []

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

def addTest():
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
    print('sum_vec:: \t{0} \t+ \t{1} \t= \t{2}'.format(arrayVal1, arrayVal2, res5)) 


tests.append(addTest)

# Тест для функции вычитания
def subTest():
    # Вычитание целых чисел
    res1 = counter.subs(intVal1, intVal2)
    print('sub_int:: \t{0} \t+ \t{1} \t= \t{2}'.format(intVal1, intVal2, res1))
    
    # Вычитание чисел с плавающей точкой (float)
    res2 = counter.subs(floatVal1, floatVal2)
    print('sub_float:: \t{0} \t+ \t{1} \t= \t{2}'.format(floatVal1, floatVal2, res2))
    
    # Вычитание комплексных чисел (например, 1+2j)
    res3 = counter.subs(compVal1, compVal2)
    print('sub_comp:: \t{0} \t+ \t{1} \t= \t{2}'.format(compVal1, compVal2, res3))
    
    # Вычитание numpy-массивов (numpy array)
    res4 = counter.subs(arrayVal1, arrayVal2)
    print('sub_array:: \t{0} \t+ \t{1} \t= \t{2}'.format(arrayVal1, arrayVal2, res4))
    
    # Вычитание numpy-векторов (то же, что массивы, просто другой стиль задания)
    res5 = counter.subs(vecVal1, vecVal2)
    print('sub_vec:: \t{0} \t+ \t{1} \t= \t{2}'.format(arrayVal1, arrayVal2, res5))  

tests.append(subTest)

# Тест для функции умножения
def mulTest():
    # Умножение целых чисел
    res1 = counter.multiply(intVal1, intVal2)
    print('mul_int:: \t{0} \t+ \t{1} \t= \t{2}'.format(intVal1, intVal2, res1))
    
    # Умножение чисел с плавающей точкой (float)
    res2 = counter.multiply(floatVal1, floatVal2)
    print('mul_float:: \t{0} \t+ \t{1} \t= \t{2}'.format(floatVal1, floatVal2, res2))
    
    # Умножение комплексных чисел (например, 1+2j)
    res3 = counter.multiply(compVal1, compVal2)
    print('mul_comp:: \t{0} \t+ \t{1} \t= \t{2}'.format(compVal1, compVal2, res3))
    
    # Умножение numpy-массивов (numpy array)
    res4 = counter.multiply(arrayVal1, arrayVal2)
    print('mul_array:: \t{0} \t+ \t{1} \t= \t{2}'.format(arrayVal1, arrayVal2, res4))
    
    # Умножение numpy-векторов (то же, что массивы, просто другой стиль задания)
    res5 = counter.multiply(vecVal1, vecVal2)
    print('mul_vec:: \t{0} \t+ \t{1} \t= \t{2}'.format(arrayVal1, arrayVal2, res5))  

tests.append(mulTest)

# Тест для функции деления
def divTest():
    # Деление целых чисел
    res1 = counter.div(intVal1, intVal2)
    print('div_int:: \t{0} \t+ \t{1} \t= \t{2}'.format(intVal1, intVal2, res1))
    
    # Деление чисел с плавающей точкой (float)
    res2 = counter.div(floatVal1, floatVal2)
    print('div_float:: \t{0} \t+ \t{1} \t= \t{2}'.format(floatVal1, floatVal2, res2))
    
    # Деление комплексных чисел (например, 1+2j)
    res3 = counter.div(compVal1, compVal2)
    print('div_comp:: \t{0} \t+ \t{1} \t= \t{2}'.format(compVal1, compVal2, res3))
    
    # Деление numpy-массивов (numpy array)
    res4 = counter.div(arrayVal1, arrayVal2)
    print('div_array:: \t{0} \t+ \t{1} \t= \t{2}'.format(arrayVal1, arrayVal2, res4))
    
    # Деление numpy-векторов (то же, что массивы, просто другой стиль задания)
    res5 = counter.div(vecVal1, vecVal2)
    print('div_vec:: \t{0} \t+ \t{1} \t= \t{2}'.format(arrayVal1, arrayVal2, res5)) 

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

# counter.blank('Hello', 2333, 3, 5, 'A', var3=3, p='No')

# Если этот файл запускается как основная программа — запускаем тесты
if __name__ == '__main__':
    test()


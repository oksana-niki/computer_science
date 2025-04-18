"""
Created on Mon Mar 31 13:30:06 2025

    Демонстрационный файл лабораторных работ по Информатике,

    студента: Никифорова О.В.
    группы: ЗИИИм-11

    каф. АСОиУ.

    Лабораторная работа 1, Основы Python
    Упражнение 2, Исследование циклов.

@licence: GPL
@author: Никифорова О.В.
"""
# -*- coding: utf-8 -*-

import random
import numpy

def step_if():  # Тестирование ветвления if - этап 1 && 2
   
    print('##############################\n'
          'Branching demonstration file\n')
    
    print('1. If construction test')
    value = input('Enter Yes(y) or Not(n) to continue:')
    
    # Проверяем, ввёл ли пользователь "Yes" или "Y"
    if (value.capitalize() == 'Yes') | (value.capitalize() == 'Y'):
        print('You have chosen yes')
    
        # Запрашиваем окно (границу) и значение
        window = float(input('Enter the non-zero value window:'))
        value = float(input('Enter the value:'))
    
        # Проверка: находится ли value в диапазоне [-window; window]
        if -1 * window <= value <= window:
            print('Value does fit the window!')
        else:
            print('Value does not fit the window!')
    
    # Если ввели "No" или "N"
    elif (value.capitalize() == 'No') | (value.capitalize() == 'N'):
        print('You have chosen no')
    
    # Всё остальное — неподходящий ввод
    else:
        print('You have chosen \'{val}\' and this value is not appropriate!'.format(val=value))

    
step_if()


def step_while():  # Тестирование цикла while
    window = float(input('Enter the non-zero value window:'))
    value = float(input('Enter the value:'))
    
    if -1 * window <= value <= window:
        print('Value does fit the window!')
    
        value2 = float(input('input another value:'))
    
        print('\tN№ \t\t1(t) \t+ \t\tv2 \t= \t\tv1(t+1)')
        counter = 1
    
        while -1 * window <= value <= window:
            val = value + value2
            print('\t{count} \t{value} \t+ \t{value2} \t= \t{val}'.format(
                count=counter,
                value=value,
                value2=value2,
                val=val
            ))
            value = val
            counter += 1
    
        print('while made {count} iterations'.format(count=counter - 1))
    else:
        print('Value does not fit the window!')

step_while()

def step_for():
    value = float(input('input value for FOR step:'))
    array = [random.normalvariate(0,1) for i in range(10)]  # список из 10 случайных чисел
    print('Before processing:')
    print('Print first five numbers from array :', array[:5])  # показываем первые 5 значений

    counter = 0
    for i in range(len(array)):
        print('Processing {elem}...'.format(elem=array[i]))
    
        if array[i] >= 0:
            print('Continued.')
            counter += 1
            continue  # пропускаем оставшуюся часть цикла
    
        elif array[i] >= value:  
            print('Breacked')    
            break
    
        else:
            array[i] = numpy.abs(array[i])  # делаем число положительным
            print('Processed: {elem}.'.format(elem=array[i]))
            counter += 1

    else:
        print('All the values processed properly.')  # else от цикла: сработает, если цикл не был прерван через break
    print('After processing:')
    print(array[:5])

step_for()

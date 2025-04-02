"""
Created on Mon Mar 31 13:30:06 2025

    Демонстрационный файл лабораторных работ по Информатике,

    студента: Никифорова О.В.
    группы: ЗИИИм-11

    каф. АСОиУ.

    Лабораторная работа 1, Основы Python
    Упражнение 3, Консольное меню.

@licence: GPL
@author: Никифорова О.В.
"""# -*- coding: utf-8 -*-

def step_try_except():
# Открываем файл с именем '1.txt' для чтения
    f = open('1.txt')
    
    # Создаём пустой список, в который будем добавлять числа
    ints = []
    
    try:
        # Проходимся по каждой строке в файле
        for line in f:
            # Пробуем преобразовать строку в целое число и добавить в список
            ints.append(int(line))
    
    # Если строку нельзя преобразовать в число (например, "abc"), произойдёт ошибка ValueError
    except ValueError:
        print('Это не число. Выходим.')  # Сообщаем об ошибке
    
    # Если произошла какая-то другая непредвиденная ошибка
    except Exception:
        print('Это что ещё такое?')  # Сообщаем, что ошибка неизвестная
    
    # Если всё прошло хорошо и ошибок не было
    else:
        print('Всё хорошо.')  # Сообщаем об этом
    
    # Этот блок выполняется всегда — была ошибка или нет
    finally:
        f.close()  # Закрываем файл
        print('Я закрыл файл.')  # Подтверждаем, что файл закрыт
    
    # Комментарий: блоки выполняются в таком порядке — сначала try,
    # если ошибка — срабатывает подходящий except,
    # если ошибок не было — выполняется else,
    # finally выполняется всегда в любом случае

step_try_except()


def step_menu_items():
    # Глобальная переменная — список пунктов меню
    global menuitems
    
    # Создаём список пунктов меню
    menuitems = [
        'Item 1',
        'Item 2',
        'Item 3',
        'Item 4'
    ]
    
    # Просто печатаем заголовок
    print('##############################\n\
    Menu demonstration file\n')
    
    # Бесконечный цикл — программа будет крутиться, пока мы её не прервём через меню
    while True:
        count = 1  # Счётчик для нумерации пунктов меню
        print('Type a number of the menu item to make a choice:')
        print('----------')
    
        # Печатаем все пункты меню с номерами
        for item in menuitems:
            print('{count} {item}'.format(item=item, count=count))
            count = count + 1  # Увеличиваем счётчик после каждого пункта
    
        # Добавляем последний пункт — "Выход"
        print('{count} {item}'.format(item='Exit', count=count))
        print('----------')
    
        # Спрашиваем у пользователя выбор
        choice = input('Choice: ')
        try:
            # Пробуем преобразовать введённое в число
            choice = int(choice)
    
            # Если ввели номер, соответствующий выходу
            if choice == count:
                print('You\'ve chosen Exit. Exiting...')
                break  # Прерываем цикл
    
            # Если выбор — это номер одного из пунктов меню
            elif (choice <= len(menuitems)) & (choice > 0):
                print('You\'ve chosen {0}.'.format(menuitems[choice - 1]))
    
            # Если номер вне диапазона
            else:
                print('There no such menu item!')
    
        # Если пользователь ввёл не число, ловим ошибку
        except ValueError:
            print('Your choice is not an int!')
    
        # Просим нажать Enter, чтобы продолжить (например, чтобы пользователь успел прочитать)
        input('Enter anything to continue...')

step_menu_items()

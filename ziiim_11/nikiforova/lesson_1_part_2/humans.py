"""
Created on Mon Apr 07 21:12:03 2025

    Демонстрационный файл лабораторных работ по Информатике,

    студента: Никифорова О.В.
    группы: ЗИИИм-11

    каф. АСОиУ.

    Лабораторная работа 2, Расширенные возможности
    Упражнение 1, Классы.

@licence: GPL
@author: Никифорова О.В.
"""
# -*- coding: utf-8 -*-

import random

class driopitecus(object):

    __slots__ = ('name', 'hair', 'walk', 'clever', '__age')

    def __init__(self, name):
        self.name = name
        self.hair = 'Hairy'
        self.walk = 'No'
        self.clever = 'Not'
        self.__age = random.normalvariate(30, 1)


    def introduce(self):
        print('Joking? He cannot talk!')

    def talk(self):
        print('HOOAOA!')

    def __think(self):
        print('<Sound of thinking>')

   # Метод, который вызывает "мышление" и создание примитивного инструмента
    def _make_tool(self):
        self.__think()  # приватный метод "думания"
        print('<Doing something with rocks and stics>')  # примитивное поведение
    
    # Статический метод: для созда­ния статичных методов, 
    # не требующих инициализированного экземпляра
    @staticmethod
    def fromparam(name, age, hair, clever, walk):
        person = driopitecus(name)  # создаём экземпляр с именем
        person.age = age            # устанавливаем возраст через property setter
        person.hair = hair
        person.clever = clever
        person.walk = walk
        return person
    
    # Классовый метод: позволяющего работать с любым экземпляром,
    # а не только с тем, из которого был вызван
    @classmethod
    def createson(cls, name):
        person = driopitecus(name)  # создаём экземпляр
        person.age = 0              # возраст — младенец
        person.hair = cls.hair      # наследуем характеристики от класса
        person.clever = cls.clever
        person.walk = cls.walk
        return person
    
    # Свойство: доступ к приватному полю __age
    @property
    def age(self):
        return self.__age
    
    # Сеттер: устанавливает возраст, но только в пределах [0, 100]
    # Если выходит за пределы — назначается случайное значение из нормального распределения
    @age.setter
    def age(self, value):
        if 100 >= value >= 0:
            self.__age = value
        else:
            self.__age = random.normalvariate(30, 1)  # "разумный" дефолт




gorm = driopitecus('Gorm')
print('We just created {}!'.format(gorm.name))
gorm.introduce()
gorm.talk()
# gorm.__think()

class australopitecus(driopitecus):

    __slots__ = ('name', 'hair', 'walk', 'clever', '__age')

    def __init__(self, name):
        super().__init__(name)
        self.hair = 'Hairy'
        self.walk = 'Sometimes'
        self.clever = 'A bit'
        self.__age = random.normalvariate(30, 1)
        

# hob = australopitecus('Hob')
# AttributeError: 'australopitecus' object has no attribute 'color'
# hob.color = 'Ping'
# print('We just created {}!'.format(hob.color))

class homohabilis(australopitecus):
    hair = 'Lesser'
    walk = 'Yes'

    def __init__(self, name):
        super().__init__(name)


class homoerectus(homohabilis):
    walk = 'Good'
    clever = 'A little'

    def __init__(self, name):
        super().__init__(name)

    def introduce(self):
        print('I am {}'.format(self.name))

    def talk(self):
        print('Tas ca\' taaahlk')


class neanderthal(homoerectus):
    hair = 'A bit'
    clever = 'Clever'

    def __init__(self, name):
        super().__init__(name)

    def talk(self):
        print('Whee\'s my goat??')
        
class cromanion(homoerectus):
    hair = 'On head'
    clever = 'Very clever'

    def __init__(self, name):
        super().__init__(name)

    def introduce(self):
        print('I am {}, you?'.format(self.name))

    def talk(self):
        print('Hi!')

# cromanion будет использоваться только если нужного метода не найдётся в цепочке выше
class homosapiens(neanderthal, cromanion):
    # hair = 'On head'
    clever = 'Very clever'

    def __init__(self, name):
        super().__init__(name)

    def introduce(self):
        print('Good afternoon, sir or m\'am! My name is {}'.format(self.name))

    def talk(self):
        print('Best regards!')

gorm = driopitecus('Gorm')
print('We just created {}!'.format(gorm.name))
gorm.introduce()
gorm.talk()

hob = australopitecus('Hob')
print('We just created {}!'.format(hob.name))
hob.introduce()
hob.talk()

grunt = homohabilis('Grunt')
print('We just created {}!'.format(grunt.name))
grunt.introduce()
grunt.talk()

dog = homoerectus('Dog')
print('We just created {}!'.format(dog.name))
dog.introduce()
dog.talk()

edvard = neanderthal('Edvard')
print('We just created {}!'.format(edvard.name))
edvard.introduce()
edvard.talk()

jane = cromanion('Jane')
print('We just created {}!'.format(jane.name))
jane.introduce()
jane.talk()

petrov = homosapiens('Mr. Petrov')
print('We just created {}!'.format(petrov.name))
petrov.introduce()
petrov.talk()
print('Is petrov hairy?', petrov.hair)


print(hasattr(petrov, '__dict__'))  # True → значит слоты не работают полностью
petrov.color = 'Blonde'
print(petrov.color)


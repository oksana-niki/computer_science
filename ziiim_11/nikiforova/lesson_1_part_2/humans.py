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

class driopitecus(object):

    name = 'Gorm'
    hair = 'Hairy'
    walk = 'No'
    clever = 'Not'

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print('Joking? He cannot talk!')

    def talk(self):
        print('HOOAOA!')


gorm = driopitecus('Gorm')
print('We just created {}!'.format(gorm.name))
gorm.introduce()
gorm.talk()

class australopitecus(driopitecus):
    walk = 'Sometimes'
    clever = 'A bit'


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


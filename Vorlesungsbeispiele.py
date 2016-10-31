# -*- coding: utf-8 -*-
# Программа вычисляет сколько процентов составляет число х от числа у
# y- меньшее число z.B. (200, 50)

def percents(x, y):

    dez=y*100

    result=dez/x

    return  (result)

def printing(x,y):

    print("число: %d, составляет : %d, от: %d" % (y, percents(x,y),x))

    #print(str(y)+" is " + str(percents(x,y))+" % of " + str(x))

printing(200, 50)

# Программа вычисляет расстояние между двумя точками

from math import sqrt

class Point:
    def __init__(self, _X, _Y):# определяем конструктор(обьект класса), self- обьект который конструируется  инициализируем свойства класса

        self.x=_X     # присвоение значения  параметров _X и _Y атрибутам объекта self
        self.y=_Y



def distance(p1, p2):

    dx=p2.x-p1.x
    dy=p2.y-p1.y

    sqrt(dx*dx+dy*dy)


print (distance(Point(0,0),Point(3,4))) # вызываем обьект класса
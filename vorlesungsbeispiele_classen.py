# Программа вычисляет расстояние между двумя точками



from math import sqrt
'''
class Point:
    def __init__(self, _X, _Y):# определяем конструктор(обьект класса), self- обьект который конструируется  инициализируем свойства класса

        self.x=_X     # присвоение значения  параметров _X и _Y атрибутам объекта self
        self.y=_Y



def distance(p1, p2):

    dx=p2.x-p1.x
    dy=p2.y-p1.y

    sqrt(dx*dx+dy*dy)


print (distance(Point(0,0),Point(3,4))) # вызываем обьект класса
'''
class Point:
    def __init__(self, _X, _Y):# определяем конструктор(обьект класса), self- обьект который конструируется  инициализируем свойства класса

        self.x=_X     # присвоение значения  параметров _X и _Y атрибутам объекта self
        self.y=_Y

    def distance(self, p2): #self обьект которым этот метод вызывается

        dx=p2.x-self.x
        dy=p2.y-self.y

        return sqrt(dx*dx+dy*dy)

'''
    def __eq__(self, other): # сравниваем координаты обеих точек
        return self.x==other.x and self.y== other.y
'''


print ((Point(0,0).distance(Point(3,4)))) # distance принимает два параметра   первый это тот обьект в которам она вызывается
                                        # а второй тот что внутри круглых скобок

'''
a=Point(0,0)
b=Point(3,4)
print(a.distance(b))
'''
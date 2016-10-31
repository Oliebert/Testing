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



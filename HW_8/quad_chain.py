# -*- coding: utf-8 -*-
"""
Цепь состоит из прямых отрезков различной целой длины,
соединённых попарно в замкнутую ломаную. Ввести строку
целых чисел через запятую — длины отрезков цепи.
Вывести YES, если цепь можно превратить в прямоугольник
с вершинами вершинах ломаной. Если нельзя, вывести NO.
"""
__author__ = 'oks'


chain = map(int, raw_input().split(u','))

perimeter = sum(chain)
half = perimeter / 2
point = ()


def get_points(chain):
    global point
    ml = len(chain)
    for i in xrange(ml):
        s = sum(chain[:i+1])
        p = half - s
        if p == 0:
            point = ()
            return
        for j in xrange(ml):
            t = sum(chain[ml-j-1:])

            if ml - j == i or t > p:
                point = ()
                break
            if t == p:
                point = (i, ml - j - 1)
                return


def rectangle_chain(chain):
    global point
    if len(chain) < 4 or perimeter % 2:
        return u'NO'
    get_points(chain)
    if point:
        get_points(chain[point[0]+1:point[1]])
        if point:
            return u'YES'
    return u'NO'

print rectangle_chain(chain)
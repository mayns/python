# -*- coding: utf-8 -*-

import math
__author__ = 'oks'


class Trigon(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def square(self):
        p = self.perimeter() / 2.0
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c


class Pea(object):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_rad(self):
        p = (self.a + self.b + self.c) / 2.0
        heron = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        return (self.a * self.b * self.c) / (4 * heron)

    def square(self):
        r = self.calc_rad()
        return math.pi * r ** 2

    def perimeter(self):
        r = self.calc_rad()
        return 2 * math.pi * r


class TrigonPea(Trigon, Pea):
    def __init__(self, a, b, c):
        super(TrigonPea, self).__init__(a, b, c)

    def volume(self):
        perimeter = Trigon.perimeter(self)
        square = Pea.square(self)
        return perimeter * square

# t = Trigon(3, 4, 5)
# p = Pea(3, 4, 5)
# z = TrigonPea(3, 4, 5)
# print "{:.6f}".format(t.square())
# print "{:.6f}".format(t.perimeter())
# print "{:.6f}".format(p.square())
# print "{:.6f}".format(z.volume())
# print "{:.6f}".format(z.square())
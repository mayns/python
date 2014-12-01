# -*- coding: utf-8 -*-

import math
__author__ = 'oks'


class Trigon(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def square(self):
        h = 0
        return self.c + 0.5 * h

    def perimeter(self):
        return self.a + self.b + self.c


class Pea(object):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def square(self):
        pass

    def perimeter(self):
        r = 0
        return 2 * math.pi * r


class TrigonPea(Trigon, Pea):

    def volume(self):
        pass
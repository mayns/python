# -*- coding: utf-8 -*-

__author__ = 'oks'


class Vector(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    __rmul__ = __mul__

    def __str__(self):
        return u'|{},{}|'.format(self.x, self.y)
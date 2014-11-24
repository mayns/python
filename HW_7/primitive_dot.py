# -*- coding: utf-8 -*-

__author__ = 'oks'


class Dot(object):
    def __init__(self, *args):
        self.point = args

    def __str__(self):
        return u','.join(self.point)

    def distance(self, other):
        if len(self.point) != len(other.point):
            raise ValueError
        return

    def middle(self, other):
        if len(self.point) != len(other.point):
            raise ValueError
        return
# -*- coding: utf-8 -*-

__author__ = 'oks'


class Comparator(object):

    def __init__(self, x):
        self.value = x

    def compare(self, other):
        try:
            return cmp(self.value, other.value)
        except AttributeError:
            return 1
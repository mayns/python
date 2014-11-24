# -*- coding: utf-8 -*-

__author__ = 'oks'


class Vovel(object):

    def __getattribute__(self, item):
        """

        :type item: str
        """
        vowels = set(u'aeiou')
        if item.islower() and set(item).union(vowels) == vowels:
            return item.swapcase()
        raise AttributeError(u"Vovel instance has no attribute '{}'".format(item))
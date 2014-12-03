# -*- coding: utf-8 -*-

"""
Определить класс MTuple, проксирующий тип tuple, с добавлением
в него единственной операции — унарного минуса (операция
возвращает MTuple с элементами в обратном порядке).
Прочие операции также должны возвращать MTuple вместо tuple.
"""

__author__ = 'oks'


class Meta(type):

    def __new__(cls, name, bases, dct):

        dct.update()
        for k, v in dct.iteritems():
            print k, v
            if hasattr(name, k):
                try:
                    setattr(name, k, v)
                except AttributeError:
                    continue
        return super(Meta, cls).__new__(cls, name, bases, dct)


class MTuple(tuple):
    __metaclass__ = Meta

    def __init__(self, seq=()):
        super(MTuple, self).__init__()
        self._seq = seq

    def __neg__(self):
        return self.__class__(self._seq[::-1])


c = MTuple(range(10))
print -c
print type(-c)
print c[2:6]
print type(c[2:6])
# print -(-c[2:6]+c[-1:2:-2])
# print -c[7:9]+("Bdyshch", "Bdyshch")
# print {-c[3:5]:"QQ"}
# -*- coding: utf-8 -*-

"""
Определить класс MTuple, проксирующий тип tuple, с добавлением
в него единственной операции — унарного минуса (операция
возвращает MTuple с элементами в обратном порядке).
Прочие операции также должны возвращать MTuple вместо tuple.
"""

__author__ = 'oks'


def selfish_tuple(f):
    def wrap(self, *args, **kwargs):
        res = f(self, *args, **kwargs)
        if isinstance(res, tuple):
            res = MTuple(res)
        return res
    return wrap


class MTuple(tuple):

    def __init__(self, seq=()):
        super(MTuple, self).__init__()
        self._seq = seq

    def __neg__(self):
        return MTuple(self._seq[::-1])

    @selfish_tuple
    def count(self, value):
        return super(MTuple, self).count(value)

    def index(self, value, start=None, stop=None):
        return super(MTuple, self).index(value, start, stop)

    @selfish_tuple
    def __add__(self, other):
        return super(MTuple, self).__add__(other)

    @selfish_tuple
    def __getitem__(self, item):
        return super(MTuple, self).__getitem__(item)

    @selfish_tuple
    def __contains__(self, item):
        return super(MTuple, self).__contains__(y)

    @selfish_tuple
    def __eq__(self, y):
        return super(MTuple, self).__eq__(y)

    @selfish_tuple
    def __getattribute__(self, name):
        return super(MTuple, self).__getattribute__(name)

    @selfish_tuple
    def __getnewargs__(self, *args, **kwargs):
        return super(MTuple, self).__getnewargs__(args, kwargs)

    @selfish_tuple
    def __getslice__(self, i, j):
        return super(MTuple, self).__getslice__(i, j)

    @selfish_tuple
    def __ge__(self, y):
        return super(MTuple, self).__ge__(y)

    @selfish_tuple
    def __gt__(self, y):
        return super(MTuple, self).__gt__(y)

    @selfish_tuple
    def __hash__(self):
        return super(MTuple, self).__hash__()

    @selfish_tuple
    def __iter__(self):
        return super(MTuple, self).__iter__()

    @selfish_tuple
    def __len__(self):
        return super(MTuple, self).__len__()

    @selfish_tuple
    def __le__(self, y):
        return super(MTuple, self).__le__(y)

    @selfish_tuple
    def __lt__(self, y):
        return super(MTuple, self).__lt__(y)

    @selfish_tuple
    def __mul__(self, y):
        return super(MTuple, self).__mul__(y)

    @selfish_tuple
    def __ne__(self, y):
        return super(MTuple, self).__ne__(y)

    @selfish_tuple
    def __rmul__(self, n):
        return super(MTuple, self).__rmul__(n)

    @selfish_tuple
    def __sizeof__(self):
        return super(MTuple, self).__sizeof__()



if __name__ == u'__main__':
    c = MTuple()
    c = MTuple(range(10))
    print dir(c)
    print -c
    print type(-c)
    print c[2:6]
    print type(c[2:6])
    print -(-c[2:6]+c[-1:2:-2])
    print -c[7:9]+("Bdyshch", "Bdyshch")
    print {-c[3:5]:"QQ"}
    print '---------'
    print -(-c[2:6]+c[-1:2:-2])
    print -c[7:9]+("Bdyshch","Bdyshch")
    print {-c[3:5]:"QQ"}
# -*- coding: utf-8 -*-

"""
Определить класс MTuple, проксирующий тип tuple, с добавлением
в него единственной операции — унарного минуса (операция
возвращает MTuple с элементами в обратном порядке).
Прочие операции также должны возвращать MTuple вместо tuple.
"""

__author__ = 'oks'

excluded = ['__iter__', '__repr__', '__hash__']


class Meta(type):
    def __new__(mcs, name, bases, dct):

        def selfish_tuple(f):
            def wrap(self, *args, **kwargs):
                res = cls(f(self, *args, **kwargs))
                return res
            return wrap

        cls = type.__new__(mcs, name, bases, dct)

        for meth in bases[0].__dict__:
            if u'tuple' in unicode(getattr(tuple, meth)) and meth not in excluded:
                setattr(cls, meth, selfish_tuple(getattr(bases[0], meth)))
                continue
            setattr(cls, meth, getattr(bases[0], meth))

        return cls


class MTuple(tuple):
    __metaclass__ = Meta

    def __neg__(self):
        return MTuple(self[::-1])


if __name__ == u'__main__':
    c = MTuple()
    c = MTuple(range(10))
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
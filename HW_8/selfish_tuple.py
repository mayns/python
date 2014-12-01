# -*- coding: utf-8 -*-

"""
Определить класс MTuple, проксирующий тип tuple, с добавлением
в него единственной операции — унарного минуса (операция
возвращает MTuple с элементами в обратном порядке).
Прочие операции также должны возвращать MTuple вместо tuple.
"""

__author__ = 'oks'


class Meta(type):
    pass


class MTuple(tuple):

    def __init__(self, seq=()):
        super(MTuple, self).__init__(seq)
        self.seq = seq

    def __neg__(self):
        return MTuple(self.seq[::-1])



c = MTuple(range(10))
print c[2:6]
# print -(-c[2:6]+c[-1:2:-2])
# print -c[7:9]+("Bdyshch", "Bdyshch")
# print {-c[3:5]:"QQ"}
# -*- coding: utf-8 -*-

__author__ = 'mayns'

s = raw_input()
s = map(int, s.split(u','))

m, n = s


def s_count(num):
    f = 1
    c = 1
    while f:
        num = num / 10
        c += 1 if num else 0
        if not num:
            f = 0
    return c
p = s_count(m * n)
n_f = s_count(n)

for i in xrange(1, n+1):
    print u'{:_>{P}}_=_{:_>{K}}_*_{}'.format(i * m, i, m, P = p, K = n_f)
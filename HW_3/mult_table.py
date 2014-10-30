# -*- coding: utf-8 -*-

__author__ = 'mayns'

s = raw_input()
s = map(int, s.split(u','))

m, n = s

p = len(str(m * n))
n_f = len(str(n))

for i in xrange(1, n+1):
    print u'{:_>{P}}_=_{:_>{K}}_*_{}'.format(i * m, i, m, P = p, K = n_f)
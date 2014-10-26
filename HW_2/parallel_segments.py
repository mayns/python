# -*- coding: utf-8 -*-

__author__ = 'mayns'

c = raw_input()
c = map(int, c.split(u','))

A1 = c[2] - c[0]
B1 = c[3] - c[1]

A2 = c[6] - c[4]
B2 = c[7] - c[5]

print u'YES' if A1 * B2 == A2 * B1 else u'NO'
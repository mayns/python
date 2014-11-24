# -*- coding: utf-8 -*-

from itertools import product

__author__ = 'oks'

k, n = map(int, raw_input().split(u','))

bases = {
    0: u'0',
    1: u'1',
    2: u'2',
    3: u'3',
    4: u'4',
    5: u'5',
    6: u'6',
    7: u'7',
    8: u'8',
    9: u'9',
    10: u'A',
    11: u'B',
    12: u'C',
    13: u'D',
    14: u'E',
    15: u'F',
    16: u'G',
}

b = [bases[k] for k in xrange(n)]

r = product(b, repeat=k)

for i in r: print u''.join(i)
# -*- coding: utf-8 -*-

from math import *

__author__ = 'mayns'

func = raw_input()
ab = raw_input()
a, b = map(int, ab.split(u','))

min_f = None
max_f = None
for x in xrange(a, b+1):
    try:
        f = eval(func)
    except (ArithmeticError, ValueError):
        continue
    if (f < min_f) or (min_f is None):
        min_f = f
    if (f > max_f) or (max_f is None):
        max_f = f

print u'{} {}'.format(min_f, max_f)
# -*- coding: utf-8 -*-

__author__ = 'mayns'

from math import *
from itertools import product

func = raw_input()

params = raw_input().split(u' ')
params_keys = []
params_values = []
f_max = None

for param in params:
    p = param.split(u'=')
    point = p[1].split(u',')
    params_keys.append(p[0])
    params_values.append(xrange(int(point[0]), int(point[1])+1) if len(point) > 1 else [int(point[0])])

combs = product(*params_values)

l = eval(u'lambda ' + u', '.join(params_keys) + u': ' + func)

for j in combs:
    c = l(*j)
    if c > f_max:
        f_max = c

print f_max
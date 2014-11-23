# -*- coding: utf-8 -*-

__author__ = 'oks'

k, n = map(int, raw_input().split(u','))

gen = (int(str(l), base=n) for l in xrange(100))

for i in gen:
    print i
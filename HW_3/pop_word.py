# -*- coding: utf-8 -*-

from collections import defaultdict

__author__ = 'mayns'

f = 1
s = []
while f:
    a = raw_input()
    if not a:
        f = 0
    else:
        s.extend(a.rsplit())

d = defaultdict(int)

for w in s:
    d[w] += 1

t = sorted(d.items(), key=lambda x: x[1], reverse=1)

if len(t) > 1 and t[0][1] == t[1][1]:
    print u'---'
else:
    print t[0][0]
# -*- coding: utf-8 -*-

from collections import defaultdict

__author__ = 'mayns'

s = raw_input()
s = s.rsplit()
d = defaultdict(list)

for w in s:
    d[len(set(w))].append(w)
print u' '.join(reduce(lambda x, y: x+y, d.values()))

# print u' '.join(sorted(raw_input().split(), key=lambda s: len(set(s))))

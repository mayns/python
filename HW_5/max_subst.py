# -*- coding: utf-8 -*-

__author__ = 'oks'

r = raw_input()

a = [r.find(v, i+1) - i for i, v in enumerate(r)]
print a
max_a = [k for i, k in enumerate(a[:-1]) if
         (a[i+1] >= k) and (k > 0) or ((k < 0) and
          a[i:a.index(filter(lambda x: x > 0, a[i:])[0]) if any([y > 0 for y in a[i:]]) else -1])]

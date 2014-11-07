# -*- coding: utf-8 -*-

s = raw_input()

l = len(s)

d = (x for x in xrange(1, l/2+1) if not l % x)

for i in d:
    sliced = s[:i]
    k = s.count(sliced)
    sc = len(sliced)
    if sliced == s[i:i+sc] and sc * k == l:
        print k
        break
else:
    print 1

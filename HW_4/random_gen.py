# -*- coding: utf-8 -*-

__author__ = 'mayns'

params = raw_input()
y = int(raw_input())

x0, a, c, m = map(int, params.split(u','))


def gen(xn):
    for i in xrange(m):
        x_next = (a*xn + c) % m
        yield x_next
        xn = x_next

g = gen(x0)
for i in xrange(m):
    try:
        if g.next() == y:
            print u'YES'
            break
    except StopIteration:
        print u'NO'
        break
else:
    print u'NO'
g.close()
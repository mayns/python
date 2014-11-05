# -*- coding: utf-8 -*-

__author__ = 'mayns'

costs = raw_input()
step = int(raw_input())
costs = map(int, costs.split(u','))
k = len(costs)
amin = []


def min_pay(ak, klist):

    global amin

    if 1 < len(klist) <= step:
        return min(klist) + ak

    for i in xrange(1, step):
        amin.append(ak + min_pay(klist[-i], klist[:-i]))
    print amin
    return ak + min(amin)

print min_pay(costs[-1], costs[:-1])
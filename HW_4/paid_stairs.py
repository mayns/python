# -*- coding: utf-8 -*-

from functools import wraps
from collections import defaultdict
import time

__author__ = 'mayns'

costs = raw_input()
step = int(raw_input())
costs = map(int, costs.split(u','))

mins = defaultdict(list)
cache = {}


def memoize(f):
    @wraps(f)
    def memf(*x):
        global cache
        y = tuple(*x)
        if y in cache:
            return cache[y]
        r = f(y)
        if len(y) > 15:
            cache[y] = r
        # print len(''.join(''.join([str(i) for i in cache.keys()])))
            return cache[y]
        return r
    return memf


@memoize
def paid_stairs(costs):

    if not costs:
        return 0
    if len(costs) == 1:
        return costs[0]

    for s in xrange(step):
        # if mins[s]:
        #     mins[s] = []
        mins[s].append(paid_stairs(costs[:-s-1]))
    # print mins
    m = [i.pop() for i in mins.values() if i]
    time.sleep(10)
    return costs[-1] + min(m)

if len(costs) <= step:
    print costs[-1]
else:
    print paid_stairs(costs)
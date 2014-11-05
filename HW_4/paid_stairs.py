# -*- coding: utf-8 -*-

import functools
from collections import defaultdict

__author__ = 'mayns'

costs = raw_input()
step = int(raw_input())
costs = map(int, costs.split(u','))

mins = defaultdict(list)


def memoize(f):
    cache = {}
    @functools.wraps(f)
    def memf(*x):
        y = tuple(*x)
        if y not in cache:
            cache[y] = f(y)
        return cache[y]
    return memf

@memoize
def paid_stairs(costs):

    if not costs:
        return 0
    if len(costs) == 1:
        return costs[0]
    # try:
    # if step > 5:
    #     mins.clear()
    for s in xrange(step):
        mins[s].append(paid_stairs(costs[:-s-1]))
    # except MemoryError:
    #     return 0
    # else:
    m = [i.pop() for i in mins.values() if i]

    return costs[-1] + min(m)

if len(costs) <= step:
    print costs[-1]
else:
    print paid_stairs(costs)
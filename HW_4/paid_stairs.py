# -*- coding: utf-8 -*-

from collections import defaultdict

__author__ = 'mayns'

costs = raw_input()
step = int(raw_input())
costs = map(int, costs.split(u','))
k = len(costs)

mins = defaultdict(list)


def paid_stairs(costs):

    if not costs:
        return 0
    if len(costs) == 1:
        return costs[0]

    for s in xrange(1, step+1):
        mins[s].append(paid_stairs(costs[:-s]))

    return costs[-1] + min([i.pop() for i in mins.values()])

if len(costs) < step:
    print costs[-1]
elif len(costs) == step:
    print costs[-1] + min(costs)
else:
    print paid_stairs(costs[:])
# -*- coding: utf-8 -*-

__author__ = 'oks'


costs = raw_input()
step = int(raw_input())
costs = map(int, costs.split(u','))

if len(costs) < step:
    print costs[-1]
else:
    for i, v in enumerate(costs):
        if i < step:
            continue
        else:
            p = min(costs[i-step:i])
            costs[i] += p

    print costs[-1]
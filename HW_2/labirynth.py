# -*- coding: utf-8 -*-

__author__ = 'oks'

m = {}

nodes = {}

m[0] = raw_input()

c = len(m[0])

path = []

for i in xrange(1, c):
    m[i] = raw_input()

for k, v in m.iteritems():
    for e, j in enumerate(v):
        if j == u'.':
            nodes[(k, e)] = dict(
                visited=False
            )

start_node = (0, 0)
final_node = (c-1, c-1)
path = [x for x in sorted(nodes.keys())]

for el in path:
    i, j = el
    if (i, j+1) in nodes:
        nodes[el].setdefault(u'children', []).append((i, j+1))
    if (i+1, j) in nodes:
        nodes[el].setdefault(u'children', []).append((i+1, j))
    if (i-1, j) in nodes:
        nodes[el].setdefault(u'children', []).append((i-1, j))
    if (i, j-1) in nodes:
        nodes[el].setdefault(u'children', []).append((i, j-1))


way_out = {}


def findaway(current_node):
    try:
        if current_node == final_node:
            return 1
        next_nodes = nodes[current_node].get(u'children', [])
        for node in next_nodes:
            if (node not in nodes) or nodes[node][u'visited']:
                continue
            else:
                next_node = node
                break
        else:
            next_node = 0
        if next_node:
            nodes[next_node][u'parent'] = current_node
            nodes[current_node][u'visited'] = 1
            return findaway(next_node)
        else:
            next_node = nodes[current_node].get(u'parent', u'')
            nodes.pop(current_node)
            if not next_node:
                return 0
            return findaway(next_node)
    except Exception:
        return u'NO'

print u'NO' if (start_node not in nodes) or (final_node not in nodes) or not findaway(start_node) else u'YES'
# -*- coding: utf-8 -*-

__author__ = 'mayns'


n = int(raw_input())
l = raw_input()
l = map(int, l.split(u','))


def req_sum(k, i, l):
    if i >= len(l):
        return 1 if k == 0 else 0
    count = req_sum(k, i + 1, l)
    count += req_sum(k - l[i], i + 1, l)
    return count


def sniffer(k, l):
    for i in xrange(0, len(l)-1):
        for j in xrange(1, len(l)):
            if j > i:
                print l[i], l[j]


def summer(k, s):
    if s:
        m = s.pop()
        if k - m in s:
            return True

        return summer(k - m, [i for i in s if i <= k - m])
    return False


def sum_checker(k, s):
    if k in s:
        return u'YES'
    if k > sum(s):
        return u'NO'
    s = sorted([i for i in s if i < k])
    check_ok = False
    sl = len(s)
    for c in reversed(range(sl)):
        slices = s[:c+1]
        check_ok = summer(k, slices)
        if check_ok:
            break
        if not slices:
            break
        slices.pop()
    return u'YES' if check_ok else u'NO'

import timeit
start = timeit.default_timer()
print sniffer(n, l)
# print req_sum(n, 0, l)
# print sum_checker(n, l)
print timeit.default_timer() - start
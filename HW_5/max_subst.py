# -*- coding: utf-8 -*-

__author__ = 'oks'

r = raw_input()

a = [r.find(v, i+1) - i for i, v in enumerate(r)]
print len(a)
cur_max = 0
max_ind = 0
tester = a[:]

counter = 1

while tester[:-1]:
    c = tester.pop(0)

    if (c > 0) and (tester[0] >= c) and (c > cur_max):
        # print u'(c > 0) and (tester[0] > c) and (c > cur_max): ', c
        cur_max = c
        max_ind = len(tester)
    if (c > 0) and (tester[0] < 0):
        pass
    if (c < 0) and (tester[0] > 0) and (c + counter > cur_max):
        # print u'(c < 0) and (tester[0] > 0) and (c + counter > cur_max)', c, tester[0]
        cur_max = c + counter
        max_ind = len(tester)
    if (c < 0) and (tester[0] > 0):
        counter = 1
    if (c < 0) and (tester[0] < 0):
        # print u'(c < 0) and (tester[0] < 0): ', c, tester[0], counter
        counter += 1
    else:
        # print u'ELSE'
        continue

cur_max = counter if counter > cur_max else cur_max
print r[max_ind:max_ind+cur_max]

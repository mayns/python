# -*- coding: utf-8 -*-

__author__ = 'oks'

r = raw_input()

a = [r.find(v, i+1) - i for i, v in enumerate(r)]

cur_max = 0
max_ind = 0
tester = a[:]

counter = 1

while tester[:-1]:
    c = tester.pop(0)
    print cur_max

    if (c > 0) and (tester[0] >= c) and (c > cur_max):
        print u'(c > 0) and (tester[0] > c) and (c > cur_max): ', c
        cur_max = c
        max_ind = len(tester)
    if (c < 0) and (tester[0] > 0) and (c + counter > cur_max):
        print u'(c < 0) and (tester[0] > 0) and (c + counter > cur_max)', c, tester[0]
        cur_max = c + counter
        max_ind = len(tester)
    if (c < 0) and (tester[0] > 0):
        counter = 1
    if (c < 0) and (tester[0] < 0):
        print u'(c < 0) and (tester[0] < 0): ', c, tester[0], counter
        counter += 1
    else:
        print u'ELSE'
        continue

print counter
print cur_max
print max_ind


#
# m = [k for i, k in enumerate(a[:-1]) if (a[i+1] >= k) and (k > 0)]
# if m:
#     cur_max = max(m) if m > cur_max else cur_max
#     max_ind = a.index(max(m))
#
# j = [1 + a[i+1] for i, k in enumerate(a[:-1]) if (k < 0) and (a[i+1] > 0)]
#
# if j:
#     cur_max = max(j) + 1 if max(j) + 1 > cur_max else cur_max
#     max_ind = a.index(max(j))
#
# n = [k for i, k in enumerate(a[:-1]) if
#      (k > 0) or ((k < 0) and a[i:a.index(filter(lambda x: x > 0, a[i:])[0]) if any([y > 0 for y in a[i:]]) else -1])]
#
# c = n.pop(0)
#
# counter = 1
# while n:
#     nextt = n.pop(0)
#     if (nextt > 0) and (counter + nextt) > cur_max:
#         cur_max = counter + nextt
#         print u'counter + next', cur_max
#     elif nextt < 0:
#         counter += 1
#     else:
#         counter = 0
#         continue
# if counter > cur_max:
#     cur_max = counter
#
# print cur_max

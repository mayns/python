# -*- coding: utf-8 -*-

__author__ = 'oks'

r = raw_input()

a = [r.find(v, i+1) - i for i, v in enumerate(r)]

m = [k for i, k in enumerate(a[:-1]) if (a[i+1] >= k) and (k > 0)]
j = [1 + a[i+1] for i, k in enumerate(a[:-1]) if (a[i+1] > 0) and (k < 0)]
n = [k for i, k in enumerate(a[:-1]) if (k > 0) or ((k < 0) and a[i:a.index(filter(lambda x: x > 0, a[i:])[0]) if any([y > 0 for y in a[i:]]) else -1])]
print a
# print max(j)
# print max(m)
print n
cur_max = max([max(j), max(m)])
# print cur_max, u'<---current max'
c = n.pop(0)

counter = 1
while n:
    nextt = n.pop(0)
    print nextt
    if (nextt > 0) and (counter + nextt) > cur_max:
        cur_max = counter + nextt
        print u'counter + next', cur_max
    elif nextt < 0:
        counter += 1
    else:
        counter = 1
        continue
if counter > cur_max:
    cur_max = counter

print cur_max

# -*- coding: utf-8 -*-

alist = list(input())
if alist:
    m = max(alist)
    new_list = [l for l in alist if l < m]
    if new_list:
        print max([l for l in alist if l < m])
    else:
        print u'NO'
print u'NO'
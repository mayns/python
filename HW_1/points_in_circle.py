# -*- coding: utf-8 -*-

circle = list(input())
points = list(input())

points = zip([x for x in points[::2]], [y for y in points[1::2]])

for i in points:
    if (i[0] - circle[0])**2 + (i[1] - circle[1])**2 > circle[2]**2:
        print u'NO'
        break
else:
    print u'YES'
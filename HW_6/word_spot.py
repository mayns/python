# -*- coding: utf-8 -*-

"""
Ввести строку (слова через пробел), вывести её таким образом,
что все вхождения слов, кроме первого, опущены. В случае,
если слово встречалось в исходной строке более одного раза,
после слова в скобках без пробела следует номер — позиция
последнего вхождения.
"""
__author__ = 'mayns'
# import timeit

words = raw_input().split(' ')
# s = timeit.default_timer()
l = len(words)
met = []
d = {}

for i in xrange(l):
    if words[i] in met:
        d[words[i]] = str(i)
        continue
    met.append(words[i])

string = ''
for m in met:
    if d.get(m):
        string += m + '(' + d[m] + ')' + ' '
        continue
    string += m + ' '

print string

# print u' '.join(map(lambda x: u'{}({})'.format(x, d[x]) if x in d else x, met))
# print u' '.join(map(lambda x: x + '(' + str(d[x]) + ')' if x in d else x, met))
# print timeit.default_timer() - s

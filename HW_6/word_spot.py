# -*- coding: utf-8 -*-

"""
Ввести строку (слова через пробел), вывести её таким образом,
что все вхождения слов, кроме первого, опущены. В случае,
если слово встречалось в исходной строке более одного раза,
после слова в скобках без пробела следует номер — позиция
последнего вхождения.
"""
__author__ = 'mayns'
from itertools import dropwhile
from collections import Counter

words = raw_input().split(u' ')

l = len(words)
w = Counter(words)

w1 = map(lambda x: (x[0], dropwhile(lambda y: words[y] != x[0], reversed(xrange(l))).next())
         if x[1] > 1 else x[0], w.items())

print u' '.join(map(lambda w: u'{}({})'.format(w[0], w[1]) if isinstance(w, tuple) else w,
                    sorted(w1, key=lambda x: words.index(x[0]) if isinstance(x, tuple) else words.index(x))))


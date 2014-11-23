# -*- coding: utf-8 -*-

"""
Ввести строку (слова через пробел), вывести её таким образом,
что все вхождения слов, кроме первого, опущены. В случае,
если слово встречалось в исходной строке более одного раза,
после слова в скобках без пробела следует номер — позиция
последнего вхождения.
"""

__author__ = 'mayns'
from itertools import compress

# qwe sdf tyu qwe sdf try sdf qwe sdf rty sdf wer sdf wer

words = raw_input().split(u' ')
l = len(words)

massive = {}

for i, w in enumerate(reversed(words)):
    if w not in massive.keys() and words.count(w) > 1:
        massive.setdefault(w, l - i - 1)
        continue

selectors = map(lambda x: 1 if words.count(x[1]) == 1 or words.index(x[1]) == x[0] else 0, enumerate(words))

print u' '.join(compress(map(lambda w: u'{}({})'.format(w, massive[w]) if massive.get(w) else w, words), selectors))
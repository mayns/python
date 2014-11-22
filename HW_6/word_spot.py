# -*- coding: utf-8 -*-

__author__ = 'mayns'

words = raw_input().split(u' ')

# rev_words = list(reversed(words))
#
# l = map(lambda word: u'{}({})'.format(word, (len(words) - rev_words.index(word)) - 1) if
#        (words.count(word) > 1) else word, words)
#
# print reduce(lambda x, y: unicode(x) + u' ' + unicode(y) if y not in unicode(x) else unicode(x), l)
f = []
w = words[:]
for i in words:
    c = words.count(i)
    if c == 1:
        f.append(c)
        continue
    words.append(u'{}({})'.format(i, w))
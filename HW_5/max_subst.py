# -*- coding: utf-8 -*-

__author__ = 'oks'

s = raw_input()

max_substr = u''
frame = []

for c in s:
    if c not in frame:
        frame.append(c)
        continue
    if len(frame) > len(max_substr):
        max_substr = u''.join(frame)
    frame = frame[frame.index(c)+1:]
    frame.append(c)

print max_substr if max_substr else u''.join(frame)
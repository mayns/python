# -*- coding: utf-8 -*-

__author__ = 'oks'

l = raw_input()
l = l.split(u' ')

operators = [u'+', u'-', u'*', u'/']
ops = []
opd = []

try:
    while 1:
        if not l:
            break
        n = l.pop(0)
        if n not in operators:
            opd.append(n)
            continue
        new_expr = eval(opd.pop(-2) + n + opd.pop())
        opd.append(str(new_expr))
    if len(opd) != 1:
        raise
    else:
        print int(opd.pop())
except:
    print u'ERROR'
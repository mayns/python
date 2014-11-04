# -*- coding: utf-8 -*-

__author__ = 'oks'

l = raw_input()
l = l.split(u' ')

operators = [u'+', u'-', u'*', u'/']
ops = []
opd = []

try:
    while len(l):
        x = l.pop()
        if x in operators:
            ops.append(x)
        else:
            opd.append(x)
            if l:
                n_op = l.pop()
                if n_op in operators:
                    ops.append(n_op)
                else:
                    new_exp = eval(n_op + ops.pop() + opd.pop())
                    opd.append(str(new_exp))
            else:
                while ops:
                    new_exp = eval(opd.pop() + ops.pop() + opd.pop())
                    opd.append(str(new_exp))
    if len(opd) > 1:
        raise
    else:
        print int(opd.pop())
except:
    print u'ERROR'
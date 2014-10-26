# -*- coding: utf-8 -*-

obj = input()

print u'\n'.join([i for i in dir(obj) if i[0] != u'_'])
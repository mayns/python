# -*- coding: utf-8 -*-

__author__ = 'oks'

mod = raw_input()

try:
    module = __import__(mod)
    dirs = dir(module)
    counter = [m for m in dirs if type(getattr(module, m)) == type(module)]
    print len(counter)
except ImportError:
    print -1
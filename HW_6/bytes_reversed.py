# -*- coding: utf-8 -*-

import struct

__author__ = 'oks'

words = raw_input()

words = map(int, words.split(u','))

key = struct.pack(len(words)*'l', *words)

val = struct.unpack(len(words)*'l', key[::-1])

print list(val)
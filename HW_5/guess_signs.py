# -*- coding: utf-8 -*-

__author__ = 'oks'

"""
Ввести последовательность натуральных чисел через пробел (не более 12),
и вывести YES, если можно ли между этими числами вставить произвольные
знаки сложения или вычитания и один знак "=", чтобы получилось равенство.
Вывести NO, если нельзя. Унарные операции и пропуск знака не допускаются.

спойлер: Поскольку чисел не больше 12, можно довольствоваться не очень
эффективным алгоритмом и функцией eval().
"""

numbers = raw_input()

numbers = numbers.split(u' ')

complexity = len(numbers)

signs = [u'+', u'-']

# 123 234 345 12

from itertools import product

combs = list(product(signs, repeat=complexity-2))

enough = 0

for comb in combs:
    for i, number in enumerate(numbers[:-1]):
        c = list(comb[:])
        c.insert(i, u'==')
        equation = u''.join(reduce(lambda x, y: x + y, zip(numbers, c))) + numbers[-1]
        if eval(equation):
            print u'YES'
            enough = 1
            break
    if enough:
        break
else:
    print u'NO'
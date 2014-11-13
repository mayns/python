# -*- coding: utf-8 -*-

__author__ = 'oks'


"""
Первая строка ввода — правило сборки агрегата вида «название_агрегата деталь1 деталь2 …»,
в ней сказано, из каких деталей можно собрать агрегат. Последующие строки ввода — либо
аналогичные правила сборки деталей вида «деталь1 деталь2 …», либо состоят из одного слова
«деталь» — в знак того, что такие детали есть на складе. Последняя строка пуская. Вывести YES,
если из деталей на складе можно собрать агрегат, и NO, если нельзя.

Если детали на складе есть, то их там бесконечно много. Никакая деталь ни на каком этапе не
включает саму себя. Каждая деталь собирается не более, чем единственным способом.
"""

automaton = []

while True:
    d = raw_input()
    if not d:
        break
    automaton.append(d)

automaton = [a.split(u' ') for a in automaton]
automaton_details = {auto.pop(0): auto[1:] for auto in automaton[1:] if len(auto[1:]) > 0}
atoms = [a for a in automaton if len(a) == 1]
atoms = reduce(lambda x, y: x + y, atoms) if atoms else []

is_constructable = 1


def parse_automaton(details):
    global is_constructable
    if isinstance(details, list):
        for detail in details:
            parse_automaton(detail)
    elif isinstance(details, unicode) and (details in atoms):
        is_constructable &= 1
    elif isinstance(details, unicode) and (details in automaton_details):
        parse_automaton(automaton_details[details])
    else:
        is_constructable &= 0

parse_automaton(automaton[0][1:])
print u'YES' if is_constructable else u'NO'
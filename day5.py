# -*- coding: utf-8 -*-

import collections
import itertools
import datetime
import re
from functools import reduce

with open('day5/input', 'r') as f:
    reaction = f.read().strip('\n')
alphabet = 'abcdefghijklmnopqrstuvwxyz'


# functional solution


def join(a, b):
    if a and b:
        react = (
            (a[-1].upper() == b[0] and a[-1] == b[0].lower()) or
            (a[-1].lower() == b[0] and a[-1] == b[0].upper()))
        if react:
            return join(a[:-1], b[1:])
    return a + b


# 1
print(len(reduce(join, reaction)))
# 2
print(min((
    (c, len(reduce(join, (reaction.replace(c, '').replace(c.upper(), '')))))
    for c in alphabet), key=lambda x: x[1]))


# naiive solution

pairs = [p for c in alphabet for p in [c.upper() + c, c + c.upper()]]


def react(reaction):
    length = None
    remaining = reaction
    while len(remaining) != length:
        length = len(remaining)
        for p in pairs:
            remaining = remaining.replace(p, "")
    return length


# 1
print(react(reaction))
# 2
print(min(((c, react(reaction.replace(c, '').replace(c.upper(), '')))
      for c in alphabet), key=lambda x: x[1]))
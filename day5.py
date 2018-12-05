# -*- coding: utf-8 -*-

import collections
import itertools
import datetime
import re


with open('day5/input', 'r') as f:
    reaction = f.read().strip('\n')

alphabet = 'abcdefghijklmnopqrstuvwxyz'
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
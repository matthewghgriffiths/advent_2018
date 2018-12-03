# -*- coding: utf-8 -*-
from itertools import chain
from collections import Counter

# First star

with open('day2/input', 'r') as f:
    ids = f.read().split('\n')[:-1]

counts = Counter(chain(*(
        set(Counter(id_).values()) for id_ in ids)))

checksum = counts[2] * counts[3]

print("checksum = {:d}".format(checksum))


# second star

def diff(pair):
    return sum(xc != yc for xc, yc in zip(*pair))

pair = min((
    (x, y) for i, x in enumerate(ids) for y in ids[:i]),
    key=diff)

box = "".join(xc for xc, yc in zip(*pair) if xc==yc)

print("correct box = {:s}".format(box))
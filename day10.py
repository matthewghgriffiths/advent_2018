# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import collections
import itertools
import datetime
import re
from functools import reduce
import numpy as np
import networkx as nx

with open('day10/input.txt', 'r') as f:
    lines = f.read().strip('\n').split("\n")

X, Y, vX, vY = zip(*
   (map(int, re.findall(r'[-+]?\d+', line)) for line in lines))

pos = np.array([X, Y]).T
v = np.array([vX, vY]).T

def extent(time):
    new_pos = pos + time * v
    return new_pos.max(0) - new_pos.min(0)


extents = [(np.abs(extent(i).prod()), i) for i in range(0,20000,100)]
_, tbroad = min(extents)
extents = [(np.abs(extent(i).prod()), i) for i in
               range(tbroad - 100,tbroad + 100)]
time = min(extents)[1]

def plot(time):
    new_pos = pos + time * v
    new_pos -= new_pos.min()
    im = np.zeros(new_pos.max(0) + 1, dtype=int)
    im[tuple(new_pos.T)] = 1
    im_str = "\n".join("".join(
            '#' if i else ' ' for i in line) for line in im.T)
    print(im_str)
    return im


im = plot(time)


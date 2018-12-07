# -*- coding: utf-8 -*-

import collections
import itertools
import datetime
import re
from functools import reduce
import numpy as np

with open('day6/input.txt', 'r') as f:
    coords = np.array([
        [int(n) for n in line.split(", ")]
        for line in f.read().strip('\n').split("\n")])

# 1
X, Y = zip(*coords)
xhi, xlo = max(X), min(X)
yhi, ylo = max(Y), min(Y)
areas = collections.defaultdict(list)
infinite = set()
for x in range(xlo, xhi + 1):
    for y in range(ylo, yhi + 1):
        dists = np.linalg.norm(coords - [[x,y]], ord=1, axis=1)
        asort = dists.argsort()
        if dists[asort[0]] != dists[asort[1]]:
            areas[asort[0]].append([x,y])
        if any((x == xlo, x == xhi, y == ylo, y == yhi)):
            infinite.add(asort[0])

print(max((len(area) for i, area in areas.items() if i not in infinite)))

# 2
grid = np.array(np.meshgrid(np.arange(xlo, xhi+1),
                            np.arange(ylo, yhi+1))).reshape(2, -1).T
dists = np.linalg.norm(grid[:,None,:] - coords[None,:,:], ord=1, axis=2)
print(np.sum(dists.sum(1) < 10000))


import matplotlib.pyplot as plt

gradient = np.linspace(0, 1, 50)
cs = plt.get_cmap('viridis')(gradient)
for i, area in areas.items():
    plt.scatter(*zip(*area), c=cs[i], marker='s')

c = ['r' if i in infinite else 'g' for i in range(len(coords))]
plt.scatter(*coords.T, c=c)
plt.show()

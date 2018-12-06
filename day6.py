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

X, Y = zip(*coords)
xhi, xlo = max(X), min(X)
yhi, ylo = max(Y), min(Y)

areas = collections.defaultdict(list)
for x in range(xlo, xhi + 1):
    for y in range(ylo, yhi + 1):
        dists = np.linalg.norm(coords - [[x,y]], ord=1, axis=1)
        asort = dists.argsort()
        if dists[asort[0]] != dists[asort[1]]:
            areas[asort[0]].append([x,y])

infinite = set()
for x in range(xlo -1, xhi + 2):
    y = ylo - 1
    infinite.add(
        np.linalg.norm(coords - [[x,y]], ord=1, axis=1).argmin())
    y = yhi + 1
    infinite.add(
        np.linalg.norm(coords - [[x,y]], ord=1, axis=1).argmin())
for y in range(ylo -1, yhi + 2):
    x = xlo - 1
    infinite.add(
        np.linalg.norm(coords - [[x,y]], ord=1, axis=1).argmin())
    x = xhi + 1
    infinite.add(
        np.linalg.norm(coords - [[x,y]], ord=1, axis=1).argmin())

print(max((len(area) for i, area in areas.items() if i not in infinite)))

# day 2
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

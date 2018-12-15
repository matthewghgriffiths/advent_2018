# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import collections
import itertools
import datetime
import re
from functools import reduce
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

with open('day13/input.txt', 'r') as f:
    lines = f.read().strip('\n').split("\n")

lines2 = [
 '/->-\\        ',
 '|   |  /----\\',
 '| /-+--+-\\  |',
 '| | |  | v  |',
 '\\-+-/  \\-+--/',
 '  \\------/   ']
lines3 = ['/>-<\\  ',
 '|   |  ',
 '| /<+-\\',
 '| | | v',
 '\\>+</ |',
 '  |   ^',
 '  \\<->/']

dims = len(lines), len(lines[-1])
grid = np.empty(dims, dtype='U1')
grid[:] = list(map(list, lines))

carts = np.array(['<', '>', '^', 'v'])
equiv = np.array(['-', '-', '|', '|'])
velocity = np.array(
        [[0, -1], [0, 1], [-1, 0], [1, 0]])
curves = ['/', '\\']
curves = {
    '/': {
        '<': 'v', '>': '^', '^': '>', 'v': '<'},
    '\\': {
        '<': '^', '>': 'v', '^': '<', 'v': '>'}}
intersections = {
    '<': ['v', '<', '^'],
    '>': ['^', '>', 'v'],
    '^': ['<', '^', '>'],
    'v': ['>', 'v', '<']}


cart_locations = np.array(np.isin(grid, carts).nonzero())
cart_dir = grid[tuple(cart_locations)]
cart_count = np.zeros(cart_dir.size, dtype=int)

base_grid = grid.copy()
base_grid[tuple(cart_locations)] = \
    equiv[carts.searchsorted(grid[tuple(cart_locations)])]


def join_grid(grid):
    return "\n".join(map("".join, grid))


def new_grid(cart_locations, cart_dir):
    new_grid = base_grid.copy()
    new_grid[tuple(cart_locations)] = cart_dir
    return new_grid


def update_pos(cart_locations, cart_dir):
    cart_locations += velocity[carts.searchsorted(cart_dir)].T


# print(join_grid(new_grid(cart_locations, cart_dir)))
n_carts = len(cart_dir)


while True:
    update_pos(cart_locations, cart_dir)
    for i, (x,y) in enumerate(cart_locations.T):
        p = base_grid[x, y]
        if p in ("\\", "/"):
            cart_dir[i] = curves[base_grid[x, y]][cart_dir[i]]
        elif p == '+':
            cart_dir[i] = intersections[cart_dir[i]][cart_count[i] % 3]
            cart_count[i] += 1

    if len(set(map(tuple, cart_locations.T))) != n_carts:
        break


pos = [pos for pos, c in
       collections.Counter(map(tuple, cart_locations.T)).items()
       if c > 1]
print("{1},{0}".format(*pos[0]))

cart_locations = np.array(np.isin(grid, carts).nonzero())
cart_dir = grid[tuple(cart_locations)]
cart_count = np.zeros(cart_dir.size, dtype=int)
n_carts = len(cart_dir)

while True:
    asort = (cart_locations[0, :]*grid.shape[0]
             + cart_locations[1, :]).argsort()
    pos = dict((tuple(p), i) for i, p in enumerate(cart_locations.T))
    for i, j in enumerate(asort):
        p = tuple(cart_locations[:, j])
        if p in pos:
            pos.pop(p)
            cart_locations[:, j] += \
                velocity[carts.searchsorted(cart_dir[j])]
            p = tuple(cart_locations[:, j])
            if p in pos:
                pos.pop(p)
            else:
                pos[p] = j

    to_keep = list(pos.values())
    n_carts = len(pos)
    cart_locations = cart_locations[:, to_keep]
    cart_dir = cart_dir[to_keep]
    cart_count = cart_count[to_keep]
    if n_carts <= 1:
        break

    for i, (x, y) in enumerate(cart_locations.T):
        p = base_grid[x, y]
        if p in ("\\", "/"):
            cart_dir[i] = curves[base_grid[x, y]][cart_dir[i]]
        elif p == '+':
            cart_dir[i] = intersections[cart_dir[i]][cart_count[i] % 3]
            cart_count[i] += 1

print("{1},{0}".format(*cart_locations.T[0]))

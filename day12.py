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

with open('day12/input.txt', 'r') as f:
    lines = f.read().strip('\n').split("\n")

initial_state = dict(enumerate(lines[0].split(" ")[-1]))

def group(state):
    imin = min(state)
    while state[imin] == '.':
        imin += 1
    imin -= 4
    imax = max(state)
    while state[imax] == '.':
        imax -= 1
    imax += 5

    for i in range(imin, imax):
        yield i, "".join(state.get(j,'.') for j in range(i-2, i+3))

def state_to_string(state):
    imin = min(state)
    imax = max(state)
    return "".join(state[i] for i in range(imin, imax+1))


def get_next_state(state):
    return dict((i, rules.get(pent, '.')) for i, pent in group(state))

states = [initial_state]
for i in tqdm(range(10000)):
    states.append(get_next_state(states[-1]))

def state_sum(state):
    return sum(i for i, c in state.items() if c == '#')

print(sum(i for i, c in states[20].items() if c == '#'))
sums = list(map(state_sum, states))
total = (50000000000 - 2000) * (sums[-1] - sums[-2]) + sums[2000]
print(total)
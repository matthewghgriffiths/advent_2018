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

n = 323081

def new_pos(elfs, recipes):
    return ((i + recipes[i] + 1) % len(recipes) for i in elfs)

def new_recipes(elfs, recipes):
    return map(int, str(sum(recipes[i] for i in elfs)))

recipes = list(map(int, str(37)))
elfs = [0, 1]
while len(recipes) < n + 10:
    elfs[:] = new_pos(elfs, recipes)
    recipes.extend(new_recipes(elfs, recipes))
print("".join(map(str, recipes[5: 15])))
print("".join(map(str, recipes[18: 28])))
print("".join(map(str, recipes[2018: 2028])))
print("".join(map(str, recipes[n: n + 10])))

"""
After 5 recipes, the scores of the next ten would be 0124515891.
After 18 recipes, the scores of the next ten would be 9251071085.
After 2018 recipes, the scores of the next ten would be 5941429882.
"""


recipes = list(map(int, str(37)))
elfs = [0, 1]
seq = list(map(int, str(n)))
len_seq = len(seq)
loop = True
while loop:
    elfs[:] = new_pos(elfs, recipes)
    for i in new_recipes(elfs, recipes):
        recipes.append(i)
        if all(j==k for j, k in zip(recipes[-len_seq:], seq)):
            loop = False
            break

print(len(recipes)-len_seq)

"""
51589 first appears after 9 recipes.
01245 first appears after 5 recipes.
92510 first appears after 18 recipes.
59414 first appears after 2018 recipes.
"""



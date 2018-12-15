# -*- coding: utf-8 -*-

import collections
import itertools
import datetime
import re
from functools import reduce
import numpy as np
import networkx as nx
from tqdm import tqdm
from scipy.signal import convolve2d, fftconvolve

serial = 9435

n = 300
x = list(range(1, n + 1))

grid = np.zeros((n, n))
Y, X = np.meshgrid(x, x)
rack_ID = X + 10
power_level = Y * rack_ID
power_level += serial
power_level *= rack_ID
power = power_level//100 - 10*(power_level//1000) - 5

kern = np.ones((3,3), dtype=int)
total = convolve2d(power, kern, mode="valid")

max_square = np.unravel_index(total.argmax(), total.shape)
print("{},{}".format(max_square[0]+1, max_square[1]+1))

convs = ((fftconvolve(power, np.ones((i, i)), mode="valid"), i) for i in tqdm(x))
score, pos, size = max(
        (total.max(), np.unravel_index(total.argmax(), total.shape), size)
        for total, size in convs)
print("{},{},{}".format(pos[0]+1, pos[1]+1, size))
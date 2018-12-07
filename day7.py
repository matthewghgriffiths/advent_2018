# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import collections
import itertools
import datetime
import re
from functools import reduce
import numpy as np
import networkx as nx

with open('day7/input.txt', 'r') as f:
    lines = f.read().strip('\n').split("\n")

pairs = [(line[5], line[-12]) for line in lines]
nodes = set(n for pair in pairs for n in pair)
in_edges = dict()
for (P, C) in pairs:
    in_edges.setdefault(C, set()).add(P)

active_nodes = nodes - in_edges.keys()
unfinished_nodes = nodes - active_nodes
completed = []
while unfinished_nodes or active_nodes:
    new_node = min(active_nodes)
    completed.append(new_node)
    active_nodes.remove(new_node)
    for node in list(unfinished_nodes):
        if not in_edges[node].difference(completed):
            active_nodes.add(node)
            unfinished_nodes.remove(node)
print("".join(completed))


time_delta = dict((c, i+1) for i, c in enumerate(sorted(nodes)))
n_workers = 5
active_nodes = nodes - in_edges.keys()
unfinished_nodes = nodes - active_nodes
worker_out = [None] * n_workers
worker_ttc = [0 for c in worker_out]
time = 0
completed = []

while unfinished_nodes or np.isfinite(worker_ttc).any():
    i, ttc = min(enumerate(worker_ttc), key=lambda x: x[1])
    time = ttc
    c = worker_out[i]
    if c in nodes:
        completed.append(c)

    worker_ttc[i] = np.inf
    for node in list(unfinished_nodes):
        if not in_edges[node].difference(completed):
            active_nodes.add(node)
            unfinished_nodes.remove(node)

    for i, ttc in enumerate(worker_ttc):
        if active_nodes and ttc == np.inf:
            c = min(active_nodes)
            active_nodes.remove(c)
            ttc = time + 60 + time_delta[c]
            worker_ttc[i] = ttc
            worker_out[i] = c

print("".join(completed))
print(time)


# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import collections
import itertools
import datetime
import re
from functools import reduce
import numpy as np
import networkx as nx

with open('day8/input.txt', 'r') as f:
    stack = list(map(int, f.read().strip('\n').split(" ")))

tree = dict()
current_node = ()
headers = {(): [1, 0]}
metadata = {(): []}
state = 0
for node, i in enumerate(stack):
    if state == 0:
        parent_trees = [tree]
        for parent in current_node:
            parent_trees.append(parent_trees[-1][parent])
        parent_tree = parent_trees.pop()

        while len(parent_tree) == headers[current_node][0]:
            if len(metadata[current_node]) < headers[current_node][1]:
                metadata[current_node].append(i)
                break
            parent_tree = parent_trees.pop()
            current_node = current_node[:-1]
        else:
            current_node = current_node + (node,)
            parent_tree[node] = dict()

            headers[current_node] = [i, None]
            metadata[current_node] = []
            state = 1

    elif state == 1:
        headers[current_node][1] = i
        state = 0

for node in headers:
    assert headers[node][1] == len(metadata[node])

# 1
print(sum(m for ms in metadata.values() for m in ms))

node_values = dict()


def calc_node(node):
    children = tree
    for n in node:
        children = children[n]

    if children:
        nodes = metadata[node]
        _children = (node + (child, ) for child in children)
        child_values = [node_values.setdefault(child, calc_node(child))
                        for child in _children]
        return sum(
            child_values[i-1] for i in nodes if i-1 < len(child_values))
    else:
        return sum(metadata[node])
# 2
print(calc_node((0,)))

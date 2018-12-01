# -*- coding: utf-8 -*-
import itertools

with open('input', 'r') as f:
    data = f.read().split("\n")

delta_freq = list(map(int, filter(bool, data)))

# first input
total = sum(delta_freq)
print(total)


freq = 0
frequencies = set([freq])
for d in itertools.cycle(delta_freq):
    freq += d
    if freq in frequencies:
        print(freq)
        break
    else:
        frequencies.add(freq)

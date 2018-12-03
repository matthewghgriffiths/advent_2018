# -*- coding: utf-8 -*-
import itertools

with open('day1/input', 'r') as f:
    data = f.read().split("\n")
delta_freq = list(map(int, filter(bool, data)))

# first star
total = sum(delta_freq)
print(total)


# second star
freq = 0
frequencies = set([freq])
for d in itertools.cycle(delta_freq):
    freq += d
    if freq in frequencies:
        print(freq)
        break
    else:
        frequencies.add(freq)

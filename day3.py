# -*- coding: utf-8 -*-

from collections import Counter

with open('day3/input', 'r') as f:
    lines = f.read().split('\n')[:-1]


def parse_line(line):
    elf, _, coords, dims = line.split(" ")
    x, y = map(int, coords.rstrip(":").split(","))
    w, h = map(int, dims.split("x"))
    return (x, y), (w, h)


square_counts = Counter(
        (i, j) for (x, y), (w, h) in map(parse_line, lines)
        for i in range(x, x + w) for j in range(y, y + h))

double_counts = [
        coords for coords, count in square_counts.items() if count > 1]
print("{:d} pieces overlap with other claims".format(len(double_counts)))

for line in lines:
    claim = line.split(" ")[0]
    (x, y), (w, h) = parse_line(line)
    counts = set(square_counts[(i, j)]
                 for i in range(x, x + w) for j in range(y, y + h))
    if counts == set([1]):
        print("claim {:s} does not overlap with any others".format(claim))
        break
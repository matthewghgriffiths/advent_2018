# -*- coding: utf-8 -*-

import collections
import itertools
import datetime
import re


with open('day4/input', 'r') as f:
    lines = f.read().split('\n')[:-1]

dates_guards = []

for line in lines:
    datestr, otherstr = line[1:].split(']')
    date = datetime.datetime.strptime(datestr, "%Y-%m-%d %H:%M")
    if 'Guard' in otherstr:
        guard, = re.findall(r'\d+', otherstr)
        dates_guards.append((date, guard))
    elif 'asleep' in otherstr:
        dates_guards.append((date, 'asleep'))
    elif 'wakes up' in otherstr:
        dates_guards.append((date, 'wakes up'))

dates_guards.sort()

guard_asleep = dict()
for date, state in dates_guards:
    if state == 'asleep':
        asleep = date
    elif state == 'wakes up':
        guard_asleep.setdefault(guard, []).append([date, asleep])
    else:
        guard = int(state)


def tot_asleep(x):
    return sum((awake - asleep for awake, asleep in x), datetime.timedelta())


guard, state = max(guard_asleep.items(), key=lambda x: tot_asleep(x[1]))


def find_max_min_asleep(state):
    min_asleep = collections.Counter((i for w, s in state
                                  for i in range(s.minute, w.minute)))
    return max(min_asleep.items(), key=lambda x: x[1])


m, tot = find_max_min_asleep(state)
print("answer1 = {:d}".format(guard * m))

guard, (m, tot) = max(
    ((guard, find_max_min_asleep(state))
     for guard, state in guard_asleep.items()), key=lambda x: x[1][1])
print("answer2 = {:d}".format(guard * m))
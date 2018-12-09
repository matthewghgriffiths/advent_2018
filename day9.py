# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import itertools
from tqdm import tqdm

nplayers = 465
last_marble = 71498


class Marble(object):
    __slots__ = ['value', 'next', 'prev']
    # use slots to decrease creation time

    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = self if next is None else next
        self.prev = self if prev is None else prev
        self.next.prev = self
        self.prev.next = self


class Circle(object):
    """Doubly linked list"""
    def __init__(self, current):
        self.current = current

    def seek(self, index):
        if index > 0:
            current = self.current
            for _ in range(index):
                current = current.next
        else:
            current = self.current
            for _ in range(-index):
                current = current.prev
        return current

    def insert(self, index, value):
        prev = self.seek(index)
        next_ = prev.next
        self.current = Marble(value, next_, prev)

    def pop(self, index):
        removed = self.seek(index)
        prev, next_ = removed.prev, removed.next
        prev.next = next_
        next_.prev = prev
        self.current = next_
        return removed.value

    def __iter__(self):
        start = self.current
        yield start.value
        current = start.next
        while current != start:
            yield current.value
            current = current.next


def play_game(nplayers, last_marble):
    circle = Circle(Marble(0))
    players = itertools.cycle(range(nplayers))
    scores = [0 for _ in range(nplayers)]
    for marble, player in tqdm(
            zip(range(1, last_marble + 1), players), total=last_marble):
        if marble % 23:
            circle.insert(1, marble)
        else:
            removed = circle.pop(-7)
            scores[player] += removed + marble
    print(max(enumerate(scores), key=lambda x: x[1]))


play_game(nplayers, last_marble)
# play_game(nplayers, last_marble * 100)

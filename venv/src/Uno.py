#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Card.py
# @Author: jesse
# @Date  : 2018/8/2
# @Desc  : Uno class


import collections
from colorama import Back


class Card(collections.namedtuple('Card', ['color', 'rank'])):

    def __new__(cls, color, rank):
        self = super(Card, cls).__new__(cls, color, rank)
        return self

    def __repr__(self):
        _ = '%s,%s' % self
        prop = _.split(',')
        return getattr(Back, prop[0].upper()) + ' ' + prop[1] + ' ' + Back.RESET


class Uno(object):
    color = "Red Green Blue Yellow".split()
    rank = [str(n) for n in range(1, 10)] + "skip draw reverse".split()
    
    def __init__(self):
        self._cards = [Card(c, r) for c in self.color
                       for r in self.rank] * 2
        self._cards += [Card(c, '0') for c in self.color]
        self._cards += [Card('Black', r) for r in ('wild', 'wild_draw')]*4
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]

    def __iter__(self):
        return iter(self._cards)

    def __repr__(self):
        return repr(self._cards)

    def __setitem__(self, key, value):
        self._cards[key] = value
    
    def __add__(self, cards):
        return self._cards + cards

    def append(self, card):
        return self._cards.append(card)

    def pop(self):
        return self._cards.pop(0)


if __name__ == '__main__':
    uno = Uno()
    print len(uno)
    print uno[-1]
    print uno
    #c = UnoCard('Card', ['color', 'rank'])

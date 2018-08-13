#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Card.py
# @Author: jesse
# @Date  : 2018/8/2
# @Desc  : Uno class


import collections
from colorama import init, Fore, Back, Style
#init(autoreset=True)
uno_card = collections.namedtuple('Card', ['color', 'rank'])


class Card(uno_card):

    def __new__(cls, color, rank):
        self = super(Card, cls).__new__(cls, color, rank)
        return self

    def __repr__(self):
        _ = '%s,%s' % self
        prop = _.split(',')
        color_map = {
            'red': Back.RED,
            'green': Back.GREEN,
            'blue': Back.BLUE,
            'yellow': Back.YELLOW,
            'black': Back.BLACK,
            'reset': Back.RESET
        }
        return color_map[prop[0].lower()] + ' ' + prop[1] + ' ' + color_map['reset']


class Uno(object):
    color = "Red Green Blue Yellow".split()
    rank = [str(n) for n in range(1, 10)] + "skip draw reverse".split()
    
    def __init__(self):
        # Card = collections.namedtuple('Card', ['color', 'rank'])
        # Card = UnoCard('Card', ['color', 'rank'])
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
    
    def pop(self):
        return self._cards.pop(0)
    

if __name__ == '__main__':
    uno = Uno()
    print len(uno)
    print uno[-1]
    print uno
    #c = UnoCard('Card', ['color', 'rank'])

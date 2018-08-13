#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Dealer.py
# @Author: jesse
# @Date  : 2018/8/2
# @Desc  : Dealer class


from Uno import Uno
import random


class Dealer(object):
    cards = []
    dealt_cards = []

    def __init__(self):
        self.cards = Uno()
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        if len(self.cards) != 0:
            dealt_card = self.cards.pop()
            return dealt_card
        else:
            self.cards.append(self.dealt_cards)
            self.dealt_cards = []
            self.shuffle()
            self.deal()

    def dealt(self, card):
        self.dealt_cards.append(card)
        return card
        
    def prepare(self):
        self.__init__()
        self.dealt_cards = []


if __name__ == '__main__':
    dealer = Dealer()
    print dealer.tmp()
    dealer.shuffle()
    print dealer.tmp()
    print dealer.deal()


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Player.py
# @Author: jesse
# @Date  : 2018/8/2
# @Desc  :

from colorama import Fore, Back
from collections import Counter


class Player(object):
    name = ''
    score = 0

    def __init__(self, name=''):
        self.name = name
        self.cards = []

    def play_card(self, dealt_cards, last_call_card):
        can_play_cards = [c for c in self.cards if self.card_is_match(c, last_call_card)]
        if len(can_play_cards) == 0:
            return None, last_call_card

        can_play_cards_count = Counter([c.color for c in can_play_cards if c.color != 'Black'])

        if not can_play_cards_count:
            cards_color_count = Counter([c.color for c in self.cards if c.color != 'Black'])
            max_color = max(cards_color_count)
            new_card = can_play_cards[0]
            call_card = can_play_cards[0]._replace(color=max_color)
        else:
            can_play_max_color = max(can_play_cards_count)
            can_play_color_cards = [c for c in can_play_cards if c.color == can_play_max_color]
            new_card = max(can_play_color_cards, key=lambda x: self.is_number(x.rank))
            call_card = new_card
        self.cards.remove(new_card)
        return new_card, call_card

    def draw(self, card):
        self.cards.append(card)

    def played_cards(self):
        return self.played_cards
        
    def check_is_uno(self):
        if not bool(len(self.cards)-1): print Fore.RED + '%s用尽力气大喊: UNOOOOOOOOOOOOOOOOO!!!!' % self.name + Fore.RESET

    def check_cards_num(self):
        return len(self.cards)
    
    @staticmethod
    def card_is_match(card1, card2):
        return card1.color == card2.color or card1.rank == card2.rank or card1.color == 'Black'

    @staticmethod
    def is_number(s):
        try:
            int(s)
            return int(s)
        except ValueError:
            return None

    def get_score(self):
        for card in self.cards:
            if self.is_number(card.rank):
                self.score += self.is_number(card.rank)
            elif card.color == 'Black':
                self.score += 50
            else:
                self.score += 20
        return self.score


class HumanPlayer(Player):
    
    def __init__(self, name='Me'):
        Player.__init__(self, name)
    
    def play_card(self, dealt_cards, last_call_card):
        print '\n已出过的牌:', dealt_cards
        print '上家出牌:', last_call_card
        print '你手上的牌:',
        for i, card in enumerate(self.cards):
            print '{}-{}'.format(i, card),
        print '{}-pass'.format(i+1)

        while True:
            card_idx = self.is_number(raw_input('到你了，请出牌:'))
            if 0 <= card_idx < len(self.cards):
                if self.card_is_match(self.cards[card_idx], last_call_card):
                    played_card = self.cards[card_idx]
                    call_card = played_card
                    if played_card.color == 'Black':
                        color = ('RED', 'GREEN', 'BLUE', 'YELLOW')
                        for i, element in enumerate(color):
                            print getattr(Back, element) + ' {} '.format(i) + Back.RESET
                        idx = self.is_number(raw_input('选择你的颜色:'))
                        while not (0 <= idx <= 4):
                            idx = raw_input('选错了！！重新选择:')
                        call_card = call_card._replace(color=color[idx])
                    self.cards.remove(played_card)
                    return played_card, call_card
                else:
                    print '出错牌了!',
            elif card_idx == len(self.cards):
                return None, last_call_card
            else:
                print '出错牌了!',




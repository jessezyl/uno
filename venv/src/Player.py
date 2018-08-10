#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Player.py
# @Author: jesse
# @Date  : 2018/8/2
# @Desc  :


class Player(object):
    name = ''
    score = 0
    is_uno = False

    def __init__(self, name=''):
        self.name = name
        self.cards = []

    def play_card(self, dealt_cards, last_call_card):
        can_play_cards = [c for c in self.cards if self.card_is_match(c, last_call_card)]
        if len(can_play_cards) == 0:
            return None, last_call_card

        can_play_cards_count = (
            (len([c for c in can_play_cards if c.color == 'Red']), 'Red'),
            (len([c for c in can_play_cards if c.color == 'Green']), 'Green'),
            (len([c for c in can_play_cards if c.color == 'Blue']), 'Blue'),
            (len([c for c in can_play_cards if c.color == 'Yellow']), 'Yellow')
        )
        can_play_max = max(can_play_cards_count)
        
        if can_play_max[0] == 0:
            cards_color_count = (
                (len([c for c in self.cards if c.color == 'Red']), 'Red'),
                (len([c for c in self.cards if c.color == 'Green']), 'Green'),
                (len([c for c in self.cards if c.color == 'Blue']), 'Blue'),
                (len([c for c in self.cards if c.color == 'Yellow']), 'Yellow')
            )
            max_color = max(cards_color_count)[1]
            new_card = can_play_cards[0]
            call_card = can_play_cards[0]._replace(color=max_color)
        else:
            can_play_color_cards = [c for c in can_play_cards if c.color == can_play_max[1]]
            new_card = max(can_play_color_cards, key=lambda x: self.is_number(x.rank))
            call_card = new_card
        self.cards.remove(new_card)
        self.check_is_uno()
        return new_card, call_card

    def draw(self, card):
        self.cards.append(card)
        self.is_uno = False
        
    def played_cards(self):
        return self.played_cards
        
    def sort_cards(self):
        for card in self.cards:
            if card.color == 'Red':
                if card.rank in '0123456789':
                    self.red_num_cards.append(card)
                else:
                    self.red_action_cards.append(card)
            elif card.color == 'Green':
                if card.rank in '0123456789':
                    self.green_num_cards.append(card)
                else:
                    self.green_action_cards.append(card)
            elif card.color == 'Blue':
                if card.rank in '0123456789':
                    self.blue_num_cards.append(card)
                else:
                    self.blue_action_cards.append(card)
            elif card.color == 'Black':
                self.black_cards.append(card)
    
    def check_is_uno(self):
        self.is_uno = bool(len(self.cards)-1)
        print ['UNO!', ''][self.is_uno]
    
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


class HumanPlayer(Player):
    
    def __init__(self, name='Me'):
        Player.__init__(self, name)
    
    def play_card(self, dealt_cards, last_call_card):
        print 'cards played:', dealt_cards
        print 'you should follow this card to play:', last_call_card
        print 'your cards in hand, choose one to play:'
        for i, card in enumerate(self.cards):
            print '{}-{}'.format(i, card),
        print '{}-pass'.format(i+1)

        while True:
            card_idx = self.is_number(raw_input(self.name + '-play your card:'))
            if 0 <= card_idx < len(self.cards):
                if self.card_is_match(self.cards[card_idx], last_call_card):
                    played_card = self.cards[card_idx]
                    call_card = played_card
                    if played_card.color == 'Black':
                        color = ('Red', 'Green', 'Blue', 'Yellow')
                        for i, element in enumerate(color):
                            print '{}-{}, '.format(i, element)
                        idx = self.is_number(raw_input('choose color you call:'))
                        while not (0 <= idx <= 4):
                            idx = raw_input('wrong choice!choose your color:')
                        call_card = call_card._replace(color=color[idx])
                    self.cards.remove(played_card)
                    self.check_is_uno()
                    return played_card, call_card
                else:
                    print 'play wrong card!',
            elif card_idx == len(self.cards):
                return None, last_call_card
            else:
                print 'wrong input!',




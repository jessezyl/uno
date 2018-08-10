#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Controller.py
# @Author: jesse
# @Date  : 2018/8/3
# @Desc  : 

from Player import Player,HumanPlayer
from Dealer import Dealer
from collections import deque
from random import shuffle 


class Game(object):
    
    def __init__(self):
        self.players = deque([HumanPlayer('Me')])
        self.dealer = Dealer()

    def play(self):
        if len(self.players) > 1:
            self.pick_banker()
            self.deal_cards()
            start_card = self.dealer.dealt(self.dealer.deal())
            while start_card.rank == 'wild_draw' or start_card.rank == 'wild':
                print 'start card is {}, '.format(start_card.rank) + 'try again.'
                start_card = self.dealer.dealt(self.dealer.deal())
                
            last_card = start_card   
            is_end = False
            while not is_end:
                new_card, last_card = self.next_player(last_card)
                if self.players[-1].check_cards_num() == 0:
                    is_end = True
                    print 'game over, winner is', self.players[-1].name

            self.score()
        else:
            print 'add some player'

    def deal_cards(self):
        print 'deal cards'
        while len(self.dealer.cards) > 108-len(self.players)*7:
            for player in self.players:
                player.draw(self.dealer.deal())
            
    def add_player(self):
        if len(self.players) <= 10:
            player_name = raw_input('player name:')
            self.players.append(Player(player_name))
        else:
            print 'only 2-10 players'

    def next_player(self, last_card):
        if last_card.rank == 'skip':
            self.players.rotate(-1)
        elif last_card.rank == 'reverse':
            self.players.reverse()
            self.players.rotate(-1)
        elif last_card.rank == 'draw':
            for i in range(2):
                self.players[0].draw(self.dealer.deal())
            self.players.rotate(-1)
        elif last_card.rank == 'wild_draw':
            for i in range(4):
                self.players[0].draw(self.dealer.deal())
            self.players.rotate(-1)
        new_card, call_card = self.players[0].play_card(self.dealer.dealt_cards, last_card)
        
        while not new_card:
            self.players[0].draw(self.dealer.deal())
            new_card, call_card = self.players[0].play_card(self.dealer.dealt_cards, last_card)

        print self.players[0].name + ' played: ', new_card
        self.dealer.dealt(new_card)
        self.players.rotate(-1)
            
        return new_card, call_card
        
    def pick_banker(self):
        shuffle(self.players)
        print 'banker is: ' + self.players[0].name

    def score(self):
        pass
    
    @staticmethod
    def exit():
        exit(0)

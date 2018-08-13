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
from colorama import Fore


class Game(object):
    
    def __init__(self):
        self.players = deque([HumanPlayer('ME')])
        self.score = dict({'ME': 0})
        self.dealer = Dealer()

    def play(self):
        self.dealer.prepare()
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
                    print Fore.RED + 'Game over, winner is ' + self.players[-1].name + '!!!!!' + Fore.RESET

            self.calc_score()
        else:
            print 'add some player'

    def deal_cards(self):
        print '开始发牌'
        while len(self.dealer.cards) > 108-len(self.players)*7:
            for player in self.players:
                player.draw(self.dealer.deal())
            
    def add_player(self):
        if len(self.players) <= 10:
            player_name = raw_input('请起名:')
            self.players.append(Player(player_name))
            self.score.update({player_name: 0})
        else:
            print 'only 2-10 players'

    def next_player(self, last_card):
        if last_card.rank == 'skip':
            print Fore.RED + '跳过', self.players[0].name + Fore.RESET
            self.players.rotate(-1)
        elif last_card.rank == 'reverse':
            print Fore.RED + '反转出牌顺序' + Fore.RESET
            self.players.reverse()
            self.players.rotate(-1)
        elif last_card.rank == 'draw':
            print Fore.RED + 'DRAW!!下家' + self.players[0].name + '罚牌两张！！' + Fore.RESET
            for i in range(2):
                self.players[0].draw(self.dealer.deal())
            self.players.rotate(-1)
        elif last_card.rank == 'wild_draw':
            print Fore.RED + 'WILD DRAW!!!下家' + self.players[0].name + '罚牌四张！！' + Fore.RESET
            for i in range(4):
                self.players[0].draw(self.dealer.deal())
            self.players.rotate(-1)
        new_card, call_card = self.players[0].play_card(self.dealer.dealt_cards, last_card)
        
        while not new_card:
            print Fore.RED + self.players[0].name + '选择pass,抽一张牌。' + Fore.RESET
            self.players[0].draw(self.dealer.deal())
            new_card, call_card = self.players[0].play_card(self.dealer.dealt_cards, last_card)

        print self.players[0].name + '出牌: ', new_card
        if new_card.color != call_card.color:
            print self.players[0].name + '选择了颜色:', call_card
        self.players[0].check_is_uno()
        self.dealer.dealt(new_card)
        self.players.rotate(-1)
            
        return new_card, call_card
        
    def pick_banker(self):
        shuffle(self.players)
        print '庄家:' + self.players[0].name

    def calc_score(self):
        for player in self.players:
            self.score[self.players[-1].name] += player.get_score()

        print self.score
    
    @staticmethod
    def exit():
        exit(0)

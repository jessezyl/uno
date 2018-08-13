#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : main.py
# @Author: jesse
# @Date  : 2018/8/2
# @Desc  :

from Game import Game


def main_ui():
    print '1-add player'
    print '2-start game'
    print '3-show score'
    print '4-exit game'
    # todo: read player input
    player_input = raw_input('choose one option:')
    if player_input not in '1234':
        player_input = raw_input('input again:')
    return player_input


def end_ui():
    print '1-continue'
    print '2-add player'
    print '3-clear & return main'
    print '4-exit'
    player_input = raw_input('choose one option:')
    if player_input not in '1234':
        player_input = raw_input('input again:')
    return player_input


if __name__ == '__main__':
    game = Game()
    while True:
        user_choice = main_ui()
        if user_choice == '1':
            game.add_player()
        elif user_choice == '2':
            while True:
                game.play()
                user_choice = end_ui()
                if user_choice == '1':
                    continue
                elif user_choice == '2':
                    game.add_player()
                elif user_choice == '3':
                    game = Game()
                    break
                elif user_choice == '4':
                    game.exit()
        elif user_choice == '3':
            game.score()
        elif user_choice == '4':
            game.exit()

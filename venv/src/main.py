#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : main.py
# @Author: jesse
# @Date  : 2018/8/2
# @Desc  :

from Game import Game


def main_ui():
    print '\n'
    print '1-添加电脑'
    print '2-开始游戏'
    print '3-分数'
    print '4-退出'
    # todo: read player input
    player_input = raw_input('请选择:')
    if player_input not in '1234':
        player_input = raw_input('选错了，再选:')
    return player_input


def end_ui():
    print '\n'
    print '1-继续'
    print '2-添加电脑'
    print '3-回菜单'
    print '4-退出'
    player_input = raw_input('请选择:')
    if player_input not in '1234':
        player_input = raw_input('选错了，再选:')
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

#!/usr/bin/python3
from sys import exit
from curses import wrapper

import Game
from Game.Renderer import Renderer

from tools import get_user_input_ch
from tools import get_player_name
from tools import get_player_race
from tools import get_player_job
from tools import translate_race_str_to_enum
from tools import translate_job_str_to_enum
from tools import generate_random_stats
from tools import handle_new_game_stats
from tools import new_character
from tools import quick_new_character 

def game_loop(game, pc):
    while True:
        game.renderer.draw_main_screen(game, pc)
        key = game.renderer.s.getkey()
        ##################################################################
        # what are our movement keys by default?                         #
        # Left-handed mode:                                              #
        # A  S  D  F                                                     #
        # Left  = A J Left                                               #
        # Up    = S K Up                                                 #
        # Down  = D L Down                                               #
        # Right = F ; Right                                              #
        ##################################################################
        rows, cols = game.renderer.s.getmaxyx()
        do_incr_turns = game.handle_input(pc, key)
        if do_incr_turns:
            game.incrTurns()

def main(stdscr):
    renderer = Renderer(screen=stdscr)
    game = Game.Game(renderer=renderer)
    renderer.startup()
    renderer.draw_titlescreen()
    cc = get_user_input_ch(stdscr, ['n', 'q'])
    if cc=='n':
        pc = quick_new_character(game, renderer.s)
        pc.y = 0
        pc.x = 0 # when drawing pc or anything in dungeon, have to account for offset of borders
        game_loop(game, pc)
    elif cc=='q':
        exit(0)

if __name__=='__main__':
    wrapper(main) # needed for curses


#!/usr/bin/python3
from sys import exit
from curses import wrapper, \
    KEY_RESIZE
from tools import get_user_input_ch, \
    get_player_name, \
    get_player_race, \
    get_player_job, \
    translate_race_str_to_enum, \
    translate_job_str_to_enum, \
    generate_random_stats, \
    handle_new_game_stats,  \
    new_character, \
    handle_input 
import Game
import Renderer

def game_loop(game, renderer, pc):
    while True:
        renderer.draw_main_screen(game, pc)
        cc2 = renderer.s.getkey()
        #######################################################################
        #                                                                     #
        # what are our movement keys by default?                              #
        #                                                                     #
        # Left-handed mode:                                                   #
        #                                                                     #
        # A  S  D  F                                                          #
        #                                                                     #
        # Left  = A                                                           #
        # Up    = S                                                           #
        # Down  = D                                                           #
        # Right = F                                                           #
        #                                                                     #
        #######################################################################
        rows, cols = renderer.s.getmaxyx()
        handle_input(game, renderer, pc, cc2)

def main(stdscr):
    renderer = Renderer.Renderer(screen=stdscr)
    game = Game.Game()
    renderer.startup()
    renderer.draw_titlescreen()
    cc = get_user_input_ch(stdscr, ['n', 'q'])
    if cc=='n':
        pc = new_character(renderer.s)
        pc.y = 3
        pc.x = 1
        # this is the beginning of the main game loop
        game_loop(game, renderer, pc)
    elif cc=='q':
        exit(0)

if __name__=='__main__':
    wrapper(main) # needed for curses


#!/usr/bin/python3
from sys import exit
from curses import wrapper
from tools import get_user_input_ch, \
    get_player_name, \
    get_player_race, \
    get_player_job, \
    translate_race_str_to_enum, \
    translate_job_str_to_enum, \
    generate_random_stats, \
    handle_new_game_stats,  \
    new_character, \
    handle_input, \
    quick_new_character 
import Game, Renderer

def game_loop(game, renderer, pc):
    while True:
        renderer.draw_main_screen(game, pc)
        cc2 = renderer.s.getkey()
        ##################################################################
        # what are our movement keys by default?                         #
        # Left-handed mode:                                              #
        # A  S  D  F                                                     #
        # Left  = A J Left                                               #
        # Up    = S K Up                                                 #
        # Down  = D L Down                                               #
        # Right = F ; Right                                              #
        ##################################################################
        rows, cols = renderer.s.getmaxyx()
        # what are we passing to cc2 exactly?
        do_incr_turns = handle_input(game, renderer, pc, cc2)
        if do_incr_turns:
            game.incrTurns()

def main(stdscr):
    renderer = Renderer.Renderer(screen=stdscr)
    #game = Game.Game(screen=stdscr)
    game = Game.Game(renderer=renderer)
    renderer.startup()
    renderer.draw_titlescreen()
    cc = get_user_input_ch(stdscr, ['n', 'q'])
    if cc=='n':
        pc = quick_new_character(game, renderer.s)
        pc.y = 0
        pc.x = 0 # when drawing pc or anything in dungeon, have to account for offset of borders
        game_loop(game, renderer, pc)
    elif cc=='q':
        exit(0)

if __name__=='__main__':
    wrapper(main) # needed for curses


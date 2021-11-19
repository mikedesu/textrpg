#!/usr/bin/python3
from curses import wrapper 
from sys import exit
#from tools import startup 
from tools import get_user_input_ch 
from tools import draw_titlescreen
from tools import get_player_name
from tools import get_player_race
from tools import get_player_job
from tools import translate_race_str_to_enum
from tools import translate_job_str_to_enum
from tools import generate_random_stats
from tools import handle_new_game_stats 
from tools import new_character
from tools import draw_main_screen  

import Game
import Renderer

def main(stdscr):
    # we are moving this into Game() 
    renderer = Renderer.Renderer(screen=stdscr)
    game = Game.Game()

    renderer.startup()

    draw_titlescreen(stdscr)

    cc = get_user_input_ch(stdscr, ['n', 'q'])
    if cc=='n':
        pc = new_character(stdscr)
        # this is the beginning of the main game loop
        draw_main_screen(stdscr, pc)
        cc2 = stdscr.getch()
    elif cc=='q':
        exit(0)

if __name__=='__main__':
    wrapper(main) # needed for curses


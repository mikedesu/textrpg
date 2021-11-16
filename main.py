#!/usr/bin/python3
from curses import wrapper 
from tools import startup 
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


from sys import exit

def main(stdscr):
    startup(stdscr)
    draw_titlescreen(stdscr)
    cc = get_user_input_ch(stdscr, ['n', 'q'])
    if cc=='n':
        pc = new_character(stdscr)
        
        stdscr.clear()
        
        rows, cols = stdscr.getmaxyx()
        x = 0
        y = 0
        line = "-" * cols
        stdscr.addstr(y, x, line)
        y += 1
        line = "|" + (" "*(cols-2)) + "|"
        while y < rows-4:
            stdscr.addstr(y, x, line)
            y += 1
        line = "-" * cols
        stdscr.addstr(y, x, line)
        y += 1
        stdscr.addstr(y, x, str(pc))



        #stdscr.addstr(y, x, str(pc))
        stdscr.refresh()
        cc2 = stdscr.getch()
    elif cc=='q':
        exit(0)

if __name__=='__main__':
    wrapper(main) # needed for curses


#!/usr/bin/python3
from Game import Game
from Game.PC import PC
from curses import newwin
from curses import wrapper
from curses import init_pair
from curses import color_pair as c
from curses import start_color
from curses import A_BOLD
from curses import COLOR_BLACK
from curses import COLOR_RED
from curses import COLOR_WHITE
from curses.textpad import Textbox
from curses.textpad import rectangle
from curses import echo
from curses import noecho

def startup(s):
    start_color()
    s.clear()
    init_pair(1, COLOR_WHITE, COLOR_BLACK)
    init_pair(2, COLOR_RED,   COLOR_WHITE)
    init_pair(3, COLOR_BLACK, COLOR_WHITE)

def draw_titlescreen(s):
    s.addstr(0, 0, 'Welcome to the RPG', c(1))
    s.addstr(1, 0, 'By darkmage', c(1))
    s.addstr(2, 0, 'This is error text', c(2) | A_BOLD)
    s.addstr(3, 0, 'Press q to quit', c(3))
    s.addstr(4, 0, 'Press n for new game', c(3))
    s.refresh()

def get_player_name(s):
    echo()
    s.clear()
    input_str = 'What is your name:'
    s.addstr(0,0,input_str,c(1))
    s.refresh()
    name = s.getstr(0, len(input_str)+1, 16).decode('utf-8')
    input_str = f'You entered: {name}'
    s.addstr(1,0,input_str,c(1))
    input_str = 'Press any key to continue'
    s.addstr(2,0,input_str,c(1))
    s.refresh()
    cc = s.getch()
    return name

def get_player_job(s):
    s.clear()
    noecho()
    input_str = 'What is your job? Select from the following:'
    s.addstr(0,0,input_str,c(1))
    input_str = 'q - Fighter'
    s.addstr(1,0,input_str,c(1))
    input_str = 'w - Cleric'
    s.addstr(2,0,input_str,c(1))
    input_str = 'e - Mage'
    s.addstr(3,0,input_str,c(1))
    input_str = 'r - Thief'
    s.addstr(4,0,input_str,c(1))
    s.refresh()
    cc = ''
    current_line = 5
    while cc!='q' and cc!='w' and cc!='e' and cc!='r':
        cc = chr(s.getch())
        s.refresh()
    out_str = f'You entered: '
    a = ''
    if cc=='q':
        a='Fighter'
    elif cc=='w':
        a='Cleric'
    elif cc=='e':
        a='Mage'
    elif cc=='r':
        a='Thief'
    out_str += a
    s.addstr(current_line,0,out_str,c(1))
    current_line += 1
    out_str = 'Press any key to continue'
    s.addstr(current_line,0,out_str,c(1))
    s.refresh()
    cc = s.getch()
    return a 


def new_game(s):
    name = get_player_name(s)
    job  = get_player_job(s)



def main(stdscr):
    player = PC()
    #g = Game()
    #stdscr = curses.initscr()
    #curses.noecho()
    #curses.cbreak()
    #stdscr.keypad(True)
    startup(stdscr)
    draw_titlescreen(stdscr)
    #stdscr.addstr(2, 0, 'This is error text', color_pair(2) | A_BOLD)
    #rect_y = 2
    #rect_x = 1
    #rect_h = 5
    #rect_w = 40
    # rectangle(win, y, x, height, width)
    #rectangle(stdscr, rect_y, rect_x, rect_h, rect_w)
    # newwin(num_rows, num_cols, start_y, start_x)
    #editwin = newwin(1, 30, rect_y+1, rect_x+1)
    #stdscr.refresh()
    #box = Textbox(editwin)
    #box.edit() # Let the user edit until Ctrl-G is struck.
    #message = box.gather() # Get resulting contents
    stdscr.refresh()
    cc = ""
    while cc != 'n' and cc != 'q':
        cc = stdscr.getkey()
        stdscr.addstr(5, 0, f"Entered: {cc}", c(1))
        stdscr.refresh()
    if cc=='n':
        new_game(stdscr)


if __name__=='__main__':
    wrapper(main) # needed for curses


#!/usr/bin/python3
from sys import exit
from curses import wrapper
import Game
from Game.Renderer import Renderer
from tools import get_user_input_ch
from tools import quick_new_character 

from Game.Menu import Menu

def game_loop(game):
    while True:
        game.renderer.draw_main_screen(game)
        key = game.renderer.s.getkey()
        do_incr_turns = game.handleInput(game.pc, key)
        if do_incr_turns:
            game.process_npc_turn()
            game.decrOneHungerUnitPC()
            game.incrTurns()



def newGame(r):
    assert(r!=None)
    game = Game.Game(renderer=r)
    pc = quick_new_character(game, r.s)
    pc.y = 1
    pc.x = 1 # when drawing pc or anything in dungeon, have to account for offset of borders
    game.pc = pc 
    game_loop(game)

def main(stdscr):
    renderer = Renderer(screen=stdscr)
    renderer.startup()

    menuItems=[
        ("New Game", newGame, renderer ),
        ("Exit", None )
    ]

    version = "0.01a"
    title = "darkhack"
    titleMenu = Menu( f"{title} {version}", menuItems, renderer.s )
    titleMenu.display()



    #renderer.draw_titlescreen()
    #cc = get_user_input_ch(stdscr, ['n', 'q'])
    #if cc=='n':
#     
#    pc = quick_new_character(game, renderer.s)
#    pc.y = 1
#    pc.x = 1 # when drawing pc or anything in dungeon, have to account for offset of borders
#    game.pc = pc 
#    game_loop(game)
    
    #elif cc=='q':
    #    exit(0)
    #renderer.draw_titlescreen()
    
#    pc = quick_new_character(game, renderer.s)
#    pc.y = 1
#    pc.x = 1 # when drawing pc or anything in dungeon, have to account for offset of borders
#    game.pc = pc 
#    game_loop(game)

if __name__=='__main__':
    wrapper(main) # needed for curses


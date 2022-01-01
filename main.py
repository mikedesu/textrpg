#!/usr/bin/python3
from sys import exit
from curses import wrapper
from tools import get_user_input_ch
from tools import quick_new_character 
import Game
from Game.Renderer import Renderer
from Game.TitlescreenMenu import TitlescreenMenu 


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
    #pc.hunger = 1
    game.pc = pc 
    game_loop(game)


def constructTitlescreenMenu(renderer):
    renderer.startup()
    title = "darkhack"
    version = "0.01a"
    menuItems=[
        ("New Game", newGame, renderer ),
        ("Exit", None )
    ]
    titlescreenMenu = TitlescreenMenu( f"{title} {version}", menuItems, renderer.s )
    return titlescreenMenu


def main(stdscr):
    renderer = Renderer(screen=stdscr)
    titlescreenMenu = constructTitlescreenMenu(renderer)
    titlescreenMenu.display()
    

if __name__=='__main__':
    wrapper(main) # needed for curses


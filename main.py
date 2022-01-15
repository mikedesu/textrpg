#!/usr/bin/python3
from sys import exit
from curses import wrapper
from tools import get_user_input_ch
from tools import quickNewCharacter 
import Game
from Game.Renderer import Renderer
from Game.TitlescreenMenu import TitlescreenMenu 
from Game.OptionMenu import OptionMenu
from Game.MessageWindow import MessageWindow

def gameLoop(game):
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
    pc = quickNewCharacter(game, r.s)
    pc.y = 1
    pc.x = 1 # when drawing pc or anything in dungeon, have to account for offset of borders
    #pc.hunger = 1
    game.pc = pc 
    gameLoop(game)

def constructTitlescreenMenu(renderer):
    renderer.startup()
    title = "darkhack"
    version = "0.01a"
    titlescreenMenu = TitlescreenMenu( f"{title} {version}", renderer, newGame )
    return titlescreenMenu

def main(stdscr):
    renderer = Renderer(screen=stdscr)
    titlescreenMenu = constructTitlescreenMenu(renderer)
    titlescreenMenu.display()

if __name__=='__main__':
    wrapper(main) # needed for curses


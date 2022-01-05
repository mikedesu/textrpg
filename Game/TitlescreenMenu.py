import curses
from curses import panel
from Game.OptionMenu import OptionMenu
from .getLongestItemLength import getLongestItemLength 
from Game.MessageWindow import MessageWindow

class TitlescreenMenu(object):
    def __init__(self, title, renderer, newGameFunction):
        self.title = title
        self.position = 0
        self.renderer = renderer
        self.items = [
            ("New Game", newGameFunction, renderer),
            ("Options", None),
            ("Exit", None)
        ]
        maxY, maxX = renderer.s.getmaxyx()
        rowPad = 6
        colPad = 20
        rows = len(self.items) + rowPad
        cols = max(len(title) + colPad, getLongestItemLength(self.items) + colPad)
        y = maxY // 2 - (rows//2)
        x = maxX // 2 - (cols//2)
        self.window = renderer.s.subwin(rows, cols , y, x)
        self.window.keypad(1)
        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()

    def navigate(self, n):
        self.position += n
        if self.position < 0:
            self.position = 0
        elif self.position >= len(self.items):
            self.position = len(self.items) - 1

    def display(self):
        self.panel.top()
        self.panel.show()
        self.window.clear()
        rows, cols = self.window.getmaxyx()
        while True:
            self.window.refresh()
            curses.doupdate()
            self.window.border('|','|','-','-','+','+','+','+')
            offsetY = 1
            offsetX = 1
            self.window.addstr( offsetY, offsetX, self.title )
            offsetX += 2
            offsetY += 2

            for index, item in enumerate(self.items):
                mode = curses.A_NORMAL
                if index == self.position:
                    mode = curses.A_REVERSE
                msg = f"{index}. {item[0]}"
                self.window.addstr(offsetY + index, offsetX, msg, mode)

            key = self.window.getch()
            if key in [curses.KEY_ENTER, ord("\n")]:
                selectedItem = self.items[self.position][0]
                if "Exit" in selectedItem:
                    break
                elif "Options" in selectedItem:
                    optionMenu = OptionMenu("Options", self.renderer.s)
                    optionMenu.display()
                    #break # this is what actually kills the menu
                elif "New Game" in selectedItem:
                    

                    msgWin = MessageWindow("Starting a new game...", self.renderer.s)
                    msgWin.display()

                    newGameFunction = self.items[self.position][1]
                    renderer = self.items[self.position][2]
                    newGameFunction(renderer)
                    

                    break
            
            elif key == curses.KEY_UP:
                self.navigate(-1)
            elif key == curses.KEY_DOWN:
                self.navigate(1)
        self.window.clear()
        self.panel.hide()
        panel.update_panels()
        curses.doupdate()


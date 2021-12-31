import curses
from curses import panel

from .EndgameScreen import EndgameScreen

class ScoreScreen(object):
    #def __init__(self, title, items, stdscreen):
    def __init__(self, items, stdscreen):
        assert(items!=None)
        maxY, maxX = stdscreen.getmaxyx()
        self.stdscreen = stdscreen
        self.position = 0
        self.items = items
        rows = 10 + len(items)
        cols = 40
        y = maxY // 2 - (rows//2)
        x = maxX // 2 - (cols//2)
        self.window = stdscreen.subwin(rows, cols , y, x)
        self.window.keypad(1)
        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()
    #def navigate(self, n):
    #    self.position += n
    #    if self.position < 0:
    #        self.position = 0
    #    elif self.position >= len(self.items):
    #        self.position = len(self.items) - 1

    def display(self):
        self.panel.top()
        self.panel.show()
        self.window.clear()
        rows, cols = self.window.getmaxyx()
        self.window.refresh()
        curses.doupdate()
        self.window.border('|','|','-','-','+','+','+','+')
        offsetY = 1
        offsetX = 1
        for line in self.items:
            self.window.addstr( offsetY, offsetX, line )
            offsetY += 1
        key = self.window.getch()
        self.window.clear()
        self.panel.hide()
        panel.update_panels()
        curses.doupdate()

        eg = EndgameScreen(self.stdscreen)
        eg.display()


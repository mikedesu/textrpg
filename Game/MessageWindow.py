import curses
from curses import panel

class MessageWindow(object):
    def __init__(self, message, stdscreen):
        maxY, maxX = stdscreen.getmaxyx()
        self.title = "Game Message"
        self.message = message
        rows = 5
        cols = len(self.message) + 10
        y = maxY // 2 - (rows//2)
        x = maxX // 2 - (cols//2)
        self.window = stdscreen.subwin(rows, cols , y, x)
        self.window.keypad(1)
        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()

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
        self.window.addstr( offsetY, offsetX, self.title )
        offsetX += 2
        offsetY += 2
        self.window.addstr( offsetY, offsetX, self.message )
        key = self.window.getch()
        self.window.clear()
        self.panel.hide()
        panel.update_panels()
        curses.doupdate()


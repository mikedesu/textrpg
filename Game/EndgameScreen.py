import curses
from curses import panel

class EndgameScreen(object):
    #def __init__(self, title, items, stdscreen):
    def __init__(self, stdscreen):
        maxY, maxX = stdscreen.getmaxyx()
        self.position = 0
        
        rows = 10
        cols = 40

        y = maxY // 2 - (rows//2)
        x = maxX // 2 - (cols//2)

        self.content = [
            "THANK YOU FOR PLAYING",
            "",
            "https://linktr.ee/evildojo",
            "https://evildojo.com",
            "https://twitch.tv/darkmage666",
            "https://github.com/mikedesu/textrpg"
        ]
        
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
        
        #while True:
        self.window.refresh()
        curses.doupdate()
        self.window.border('|','|','-','-','+','+','+','+')
        offsetY = 1
        offsetX = 1
 
        for line in self.content:
            self.window.addstr( offsetY, offsetX, line )
            offsetY += 1



        key = self.window.getch()
        #    break

        self.window.clear()
        self.panel.hide()
        panel.update_panels()
        curses.doupdate()


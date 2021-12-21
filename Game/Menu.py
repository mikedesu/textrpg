import curses
from curses import panel

class Menu(object):
    def __init__(self, title, items, stdscreen):
        maxY, maxX = stdscreen.getmaxyx()
        self.title = title
        self.items = items
        self.position = 0

        rowPad = 6
        colPad = 20
        rows = len(items) + rowPad
        cols = max(len(title) + colPad, self.getLongestItemLength() + colPad)
        y = maxY // 2 - (rows//2)
        x = maxX // 2 - (cols//2)
        
        self.window = stdscreen.subwin(rows, cols , y, x)
        self.window.keypad(1)
        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()


    def getLongestItemLength(self):
        longestLen = 0
        for item in self.items:
            if len(item) > longestLen:
                longestLen = len(item)
        return longestLen 


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
            for index, item in enumerate(self.items):
                if index == self.position:
                    mode = curses.A_REVERSE
                else:
                    mode = curses.A_NORMAL
                #msg = "%d. %s" % (index, item[0])
                msg = f"{index}. {item[0]}"
                self.window.addstr(1 + index, 1, msg, mode)
            key = self.window.getch()
            if key in [curses.KEY_ENTER, ord("\n")]:
                if self.position == len(self.items) - 1:
                    break
                else:
                    self.items[self.position][1]()
                    break
            elif key == curses.KEY_UP:
                self.navigate(-1)
            elif key == curses.KEY_DOWN:
                self.navigate(1)
        self.window.clear()
        self.panel.hide()
        panel.update_panels()
        curses.doupdate()


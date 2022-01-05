import curses
from curses import panel
from .getLongestItemLength import getLongestItemLength 

class OptionMenu(object):

    def loadConfigFile(self):
        with open("config.txt", 'r') as infile:
            lines = infile.readlines()
            for line in lines:
                splitLine = line.split('=')
                varName = splitLine[0]
                value = splitLine[1]
                if varName == 'leftHandVim':
                    if value[:-1] == 'True':
                        self.leftHandVim = True
                    else:
                        self.leftHandVim = False
                if varName == 'rightHandVim':
                    if value[:-1] == 'True':
                        self.rightHandVim = True
                    else:
                        self.rightHandVim = False


    def __init__(self, title, stdscreen):
        maxY, maxX = stdscreen.getmaxyx()
        self.title = title
        self.leftHandVim = True
        self.rightHandVim = True
        self.loadConfigFile()
        leftHandVimStr = f"Left-hand Vim-like {self.leftHandVim} "
        rightHandVimStr = f"Right-hand Vim-like {self.rightHandVim} "
        self.items = [
            [leftHandVimStr, None],
            [rightHandVimStr, None],
            ["Exit", None]
        ]
        self.position = 0
        rowPad = 6
        colPad = 20
        rows = len(self.items) + rowPad
        cols = len(rightHandVimStr) + colPad
        y = maxY // 2 - (rows//2)
        x = maxX // 2 - (cols//2)
        self.window = stdscreen.subwin(rows, cols , y, x)
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
                elif "Left-hand Vim-like" in selectedItem:
                    self.leftHandVim = not self.leftHandVim 
                    self.items[self.position][0] = f"Left-hand Vim-like {self.leftHandVim} "
                elif "Right-hand Vim-like" in selectedItem:
                    self.rightHandVim = not self.rightHandVim 
                    self.items[self.position][0] = f"Right-hand Vim-like {self.rightHandVim} "
            elif key == curses.KEY_UP:
                self.navigate(-1)
            elif key == curses.KEY_DOWN:
                self.navigate(1)

        self.writeOptionsToFile()

        self.window.clear()
        self.panel.hide()
        panel.update_panels()
        curses.doupdate()

    def writeOptionsToFile(self):
        with open('config.txt','w') as outfile:
            outfile.write(f"leftHandVim={self.leftHandVim}\n")
            outfile.write(f"rightHandVim={self.rightHandVim}\n")




import curses
from curses import panel
from .Menu import Menu

class Subequipmenu(Menu):
    def display(self):
            self.panel.top()
            self.panel.show()
            self.window.clear()
            offsetY = 2
            offsetX = 2
            success = False
            while True:
                self.window.refresh()
                curses.doupdate()
                self.window.border('|','|','-','-','+','+','+','+')
                offsetY = 2
                offsetX = 2
                self.window.addstr( offsetY, offsetX, self.title )
                offsetX += 2
                offsetY += 2
                for index, item in enumerate(self.items):
                    if index == self.position:
                        mode = curses.A_REVERSE
                    else:
                        mode = curses.A_NORMAL
                    #msg = "%d. %s" % (index, item[0])
                    msg = f"{index}. {item[1]}"
                    self.window.addstr(offsetY + index, offsetX, msg, mode)
                key = self.window.getch()
                if key in [curses.KEY_ENTER, ord("\n")]:
                    if self.position == len(self.items) - 1:
                        break
                    elif len(self.items)==0:
                        break
                    else:
                        bodypart = self.items[self.position][0]
                        item = self.items[self.position][1]
                        helperFunction = self.items[self.position][2]
                        success = helperFunction(bodypart, item)
                        #self.items[self.position][1](bodypart)
                        #helperFunction(bodypart)
                        break
                elif key == curses.KEY_UP:
                    self.navigate(-1)
                elif key == curses.KEY_DOWN:
                    self.navigate(1)
            self.window.clear()
            self.panel.hide()
            panel.update_panels()
            curses.doupdate()
            return success



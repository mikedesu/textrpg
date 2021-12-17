import curses
from curses import panel
from .Menu import Menu

class ItemPickupMenu(Menu):
    def display(self):
            self.panel.top()
            self.panel.show()
            self.window.clear()

            offsetY = 2
            offsetX = 2

            while True:
                self.window.refresh()
                curses.doupdate()

                self.window.addstr( 0, 0, self.title )

                for index, item in enumerate(self.items):
                    if index == self.position:
                        mode = curses.A_REVERSE
                    else:
                        mode = curses.A_NORMAL
                    msg = "%d. %s" % (index, item[0])
                    self.window.addstr(offsetY + index, offsetX, msg, mode)
                key = self.window.getch()
                if key in [curses.KEY_ENTER, ord("\n")]:
                    if self.position == len(self.items) - 1:
                        break
                    else:
                        self.items[self.position][1](self.position)
                        break
                elif key == curses.KEY_UP:
                    self.navigate(-1)
                elif key == curses.KEY_DOWN:
                    self.navigate(1)
            self.window.clear()
            self.panel.hide()
            panel.update_panels()
            curses.doupdate()



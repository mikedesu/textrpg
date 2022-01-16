import curses
from curses import panel
from .Menu import Menu

class InventoryMenu(Menu):
    def display(self):
            self.panel.top()
            self.panel.show()
            self.window.clear()
            offsetY = 2
            offsetX = 2
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
                    msg = "%d. %s" % (index, item[0])
                    self.window.addstr(offsetY + index, offsetX, msg, mode)
                key = self.window.getch()
                #self.game.addLog(f"Key pressed: {key}")
                numberKeysList = [x+48 for x in range(11)]

                if key in [curses.KEY_ENTER, ord("\n"), 113, 27, 
                        *numberKeysList ]:

                    # q or escape
                    if key == 113 or key == 27:
                        break
                    # 0 or higher
                    elif key >= 48 and key < 58:
                        self.items[key-48][1](self.position)
                        break
                    else:
                        self.items[self.position][1](self.position)
                        break
                elif key == curses.KEY_UP or key == 56:
                    self.navigate(-1)
                elif key == curses.KEY_DOWN or key == 50:
                    self.navigate(1)
            self.window.clear()
            self.panel.hide()
            panel.update_panels()
            curses.doupdate()



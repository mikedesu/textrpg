from curses import start_color
from curses import echo
from curses import noecho
from curses import init_pair
from curses import color_pair as c
from curses import COLOR_BLACK
from curses import COLOR_RED
from curses import COLOR_WHITE
from curses import A_BOLD
from curses import use_default_colors

class Renderer:
    def __init__(self, name="Renderer", screen=None):
        self.name = name
        self.s = screen
        assert(screen!=None)
    
    def startup(self):
        use_default_colors()
        start_color()
        self.s.clear()
        init_pair(1, COLOR_WHITE, -1)
        init_pair(4, COLOR_RED,   -1)
        init_pair(2, COLOR_RED,   COLOR_WHITE)
        init_pair(3, COLOR_BLACK, COLOR_WHITE)

    def draw_titlescreen(self):
        self.s.addstr(0, 0, 'Welcome to the RPG', c(1))
        self.s.addstr(1, 0, 'By darkmage', c(1))
        self.s.addstr(2, 0, 'This is error text', c(2) | A_BOLD)
        self.s.addstr(3, 0, 'Press q to quit', c(3))
        self.s.addstr(4, 0, 'Press n for new game', c(3))
        self.s.refresh()


    def draw_main_screen_border(self, pc):
        x, y = 0, 0
        rows, cols = self.s.getmaxyx()
        line = "-" * cols
        self.s.addstr(y, x, line)
        y += 1
        line = "|" + (" "*(cols-2)) + "|"
        while y < rows-4:
            self.s.addstr(y, x, line)
            y += 1
        line = "-" * cols
        self.s.addstr(y, x, line)
        y += 1
        
        # draw pc info at bottom of screen
        self.s.addstr(y, x, str(pc))

    def draw_main_screen_pc(self, pc):
        y = pc.y
        x = pc.x
        self.s.addstr(y, x, "@", c(4) | A_BOLD )

    def draw_main_screen(self,pc):
        # experimental main-game drawing
        self.s.clear()
        self.draw_main_screen_border(pc)
        self.draw_main_screen_pc(pc)
        self.s.refresh()
     

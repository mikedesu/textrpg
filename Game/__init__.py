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


class Game:
    def __init__(self, title='my game'):
        self.title = title
    def __str__(self):
        return self.title

    def startup(self, s):
        use_default_colors()
        start_color()
        s.clear()
        init_pair(1, COLOR_WHITE, -1)
        init_pair(2, COLOR_RED,   COLOR_WHITE)
        init_pair(3, COLOR_BLACK, COLOR_WHITE)



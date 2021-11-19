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


    def draw_main_screen_border(self, game, pc):
        if game==None:
            raise Exception("draw_main_screen_border: game cannot be None")
        if pc==None:
            raise Exception("draw_main_screen_border: pc cannot be None")
        y, x = 2, 0
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
    
    def draw_main_screen_pc_info(self, game, pc):
        rows, cols = self.s.getmaxyx()
        y = rows-3
        x = 0
        # draw pc info at bottom of screen
        self.s.addstr(y, x, str(pc))
        # approximate the middle to drop a turn counter
        # like T:999
        self.s.addstr(y, int(cols/2), f"T:{game.currentTurnCount}")
        
    def draw_main_screen_pc(self, pc):
        y = pc.y
        x = pc.x
        self.s.addstr(y, x, "@", c(4) | A_BOLD )

    def draw_main_screen_logs(self, game):
        # only enough room for last 2 logs
        y, x = 0, 0
        a = len(game.logs)
        if a == 1:
            # only 1 log
            self.s.addstr(y, x, game.logs[a-1])
        elif a >= 2:
            self.s.addstr(y, x, game.logs[a-2])
            self.s.addstr(y+1, x, game.logs[a-1])


    def draw_main_screen_dungeonFloor(self, game):
        # assuming the map is 1-to-1 with the size of screen
        # and, this is gonna def change in the future
        # to accomodate some autistic asshole who will 
        # inevitably try to resize the screen on every keypress
        # so i will have to devise a clever camera system
        # in order to accomodate both them and to have a 
        # convenient way to resize the viewport
        for i in range(3, len(game.dungeonFloor.map_)):
            self.s.addstr(i, 1, game.dungeonFloor.map_[i])

    def draw_main_screen(self,game,pc):
        # experimental main-game drawing
        self.s.clear()
        self.draw_main_screen_logs(game)
        self.draw_main_screen_border(game, pc)
        self.draw_main_screen_pc_info(game, pc)
        
        # order of drawing matters
        # 1. dungeonFloor
        # 2. in-game loot / dropped-objects
        # 3. entities / NPCs
        self.draw_main_screen_dungeonFloor(game)
        self.draw_main_screen_pc(pc)
        self.s.refresh()
     

from curses import start_color, echo, noecho, init_pair
from curses import color_pair as c
from curses import COLOR_BLACK, COLOR_RED, COLOR_WHITE, COLOR_BLUE, COLOR_MAGENTA 
from curses import A_BOLD, use_default_colors

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
        init_pair(2, COLOR_RED,   COLOR_WHITE)
        init_pair(3, COLOR_BLACK, COLOR_WHITE)
        init_pair(4, COLOR_RED,   -1)
        init_pair(5, COLOR_MAGENTA, -1)
        init_pair(6, COLOR_BLUE, -1)
        self.s.keypad(True)

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
        y = 4
        x = 0
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
        x = int( 3 * cols / 4 )
        self.s.addstr(y,   x, f"T:{game.currentTurnCount}")
        self.s.addstr(y+1, x, f"y:{pc.y} x:{pc.x}")
        
    def draw_main_screen_npc(self, npc):
        y = npc.y + 5
        x = npc.x + 1
        options = None
        if npc.is_player:
            options = c(4) | A_BOLD 
        else:
            options = c(5) | A_BOLD 
        self.s.addstr(y, x, npc.symbol, options )


    def draw_main_screen_logs(self, game):
        # only enough room for last 2 logs
        y, x = 0, 0
        a = len(game.logs)
        if a == 1:
            # only 1 log
            self.s.addstr(y, x, game.logs[a-1])
        elif a == 2:
            self.s.addstr(y, x, game.logs[a-2])
            self.s.addstr(y+1, x, game.logs[a-1])
        elif a == 3:
            self.s.addstr(y, x, game.logs[a-3])
            self.s.addstr(y+1, x, game.logs[a-2])
            self.s.addstr(y+2, x, game.logs[a-1])
        elif a >= 4:
            self.s.addstr(y, x, game.logs[a-4])
            self.s.addstr(y+1, x, game.logs[a-3])
            self.s.addstr(y+2, x, game.logs[a-2])
            self.s.addstr(y+3, x, game.logs[a-1])


    def draw_main_screen_dungeonFloor(self, game):
        # assuming the map is 1-to-1 with the size of screen
        # and, this is gonna def change in the future
        # to accomodate some autistic asshole who will 
        # inevitably try to resize the screen on every keypress
        # so i will have to devise a clever camera system
        # in order to accomodate both them and to have a 
        # convenient way to resize the viewport
        df = game.dungeonFloor 
        for i in range(len(df.map_)):
            mapToDraw = df.map_[i]
            self.s.addstr(i+5, 1, mapToDraw)

    def draw_main_screen_dungeonFloor_npcs(self, game):
        npcs = game.dungeonFloor.npcs
        for npc in npcs:
            self.draw_main_screen_npc(npc)
           
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
        self.draw_main_screen_dungeonFloor_npcs(game)
        self.draw_main_screen_npc(pc)
        self.s.refresh()
     

from curses import start_color, echo, noecho, init_pair
from curses import color_pair as c
from curses import COLOR_BLACK, COLOR_RED, COLOR_WHITE, COLOR_BLUE, COLOR_MAGENTA 
from curses import A_BOLD, use_default_colors
from curses import curs_set
from .Camera import Camera

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
        curs_set(False)

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
        # dungeon border
        line = "-" * cols
        self.s.addstr(y, x, line)
        y += 1
        # border on sides
        while y < rows-4:
            self.s.addstr(y, 0, "|")
            self.s.addstr(y, cols-1, "|")
            y += 1
        # border on bottom
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
        
    def draw_main_screen_npc(self, game, npc):
        y = npc.y + 5
        x = npc.x + 1
        cx = game.camera.x
        cy = game.camera.y 
        rows, cols = self.s.getmaxyx()
        
        endOfDungeonDisplay = rows - 4
        mapRowOffset = 5
        beginDisplayX = 1
        endDisplayX = cols-1
        
        if y > rows-5:
            return
        options = None
        if npc.is_player:
            options = c(4) | A_BOLD 
        else:
            options = c(5) | A_BOLD 
        if y+cy >= mapRowOffset and y+cy <= endOfDungeonDisplay and x+cx >= beginDisplayX and x+cx <= endDisplayX :
            self.s.addstr(y + cy, x + cx, npc.symbol, options )

    def process_log(self, y, x, log):
        
        if "ERROR:" in log:
            self.s.addstr(y, x, log, c(2))
        else:
            self.s.addstr(y, x, log)

    def draw_main_screen_logs(self, game):
        # only enough room for last 2 logs
        y, x = 0, 0
        a = len(game.logs)
        if a == 1:
            # only 1 log
            self.process_log(y,   x, game.logs[a-1])
        elif a == 2:
            self.process_log(y,   x, game.logs[a-2])
            self.process_log(y+1, x, game.logs[a-1])
        elif a == 3:
            self.process_log(y,   x, game.logs[a-3])
            self.process_log(y+1, x, game.logs[a-2])
            self.process_log(y+2, x, game.logs[a-1])
        elif a >= 4:
            self.process_log(y,   x, game.logs[a-4])
            self.process_log(y+1, x, game.logs[a-3])
            self.process_log(y+2, x, game.logs[a-2])
            self.process_log(y+3, x, game.logs[a-1])


















    def draw_main_screen_dungeonFloor(self, game):
        df = game.dungeonFloor
        rows, cols = self.s.getmaxyx()
        d_rows = game.dungeonFloor.rows
        d_cols = game.dungeonFloor.cols
        # camera offsets
        cx = game.camera.x
        cy = game.camera.y 
        # this is always 9 to accomodate for the 4 rows of logs,
        # 2 rows of dungeon window border
        # and 5 of the text on the bottom i believe
        # same w/ mapRowOffset
        numRowsToSubtract = 9
        mapRowOffset = 5
        endOfDungeonDisplay = rows - 4

        beginDisplayX = 1
        endDisplayX = cols-1
        # y index
        for i in range( len(df.map_) ):
            rowToDraw = df.map_[i]
            # to draw using tiles now...
            # x index
            for j in range( len(rowToDraw) ):
                tileToDraw = rowToDraw[j]
                tileToDrawStr = str( tileToDraw )
                y = i + mapRowOffset + cy
                x = j + 1 + cx
                if y >= mapRowOffset and y <= endOfDungeonDisplay and x >= beginDisplayX and x <= endDisplayX :
                    self.s.addstr( y, x, tileToDrawStr )



    def draw_main_screen_dungeonFloor_npcs(self, game):
        npcs = game.dungeonFloor.npcs
        for npc in npcs:
            self.draw_main_screen_npc(game, npc)
           
    def draw_main_screen(self,game,pc):
        # experimental main-game drawing
        self.s.clear()
        self.draw_main_screen_logs(game)
        self.draw_main_screen_pc_info(game, pc)
        # order of drawing matters
        # 1. dungeonFloor
        # 2. in-game loot / dropped-objects
        # 3. entities / NPCs
        # 4. border
        self.draw_main_screen_dungeonFloor(game)
        self.draw_main_screen_dungeonFloor_npcs(game)
        self.draw_main_screen_npc(game, pc)
        self.draw_main_screen_border(game, pc)
        self.s.refresh()
     
    def draw_quit_screen(self):
        self.s.clear()
        a = None
        rows, cols = self.s.getmaxyx()
        filename="txt/quitscreen.txt"
        with open(filename, "r") as infile:
            a = infile.readlines()
        y = 0
        for y in range(len(a)):
            line = a[y]
            if y < rows:
                self.s.addstr(y, 0, line, c(1))
            #y += 1
        self.s.refresh()
        self.s.getkey()



import curses
from curses import start_color, echo, noecho, init_pair
from curses import color_pair as c
from curses import COLOR_BLACK, COLOR_RED, COLOR_WHITE, COLOR_BLUE, COLOR_MAGENTA , COLOR_GREEN
from curses import A_BOLD, use_default_colors
from curses import curs_set
from .Camera import Camera
from .Tiletype import Tiletype
from .ModTable import ModTable
from math import sqrt

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

        init_pair(7, COLOR_GREEN, -1)
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
    
    def draw_main_screen_pc_info(self, game):
        rows, cols = self.s.getmaxyx()
        y = rows-3
        x = 0
        # draw pc info at bottom of screen
        self.s.addstr(y, x, str(game.pc))
        # approximate the middle to drop a turn counter like T:999
        x = int( 24 * cols / 32 )
        
        # handle hunger string
        hunger = game.pc.hunger
        maxhunger = game.pc.maxhunger
        hungerStr = f"H:{hunger}/{maxhunger}"
        options = None
        if hunger < (maxhunger / 4):
            options = c(4) | A_BOLD 
        elif hunger < (maxhunger / 2):
            options = c(1) 
        else:
            options = c(7) | A_BOLD
        self.s.addstr(y, x, hungerStr, options )

        offset = len(hungerStr)+1
        str0 = f"M:{game.currentMode} T:{game.currentTurnCount}"
        self.s.addstr(y,   x+offset, str0)
        str1 = f"cy: {game.camera.y} cx: {game.camera.x} y:{game.pc.y} x:{game.pc.x}"
        self.s.addstr(y+1, x, str1)

        
    def draw_main_screen_entity(self, game, e):
        
        if not e.is_player:
            distToPC = self.getDistance( e.y, e.x, game.pc.y, game.pc.x )
        if e.is_player or distToPC <= game.pc.lightradius:
            rows, cols = self.s.getmaxyx()
            mapRowOffset = 5
            beginDisplayX = 1
            y = e.y + mapRowOffset
            x = e.x + beginDisplayX
            endDisplayX = cols-1
            endDisplayY = rows-4
            cx = game.camera.x
            cy = game.camera.y 
            options = None
            if e.is_player:
                options = c(4) | A_BOLD 
            else:
                options = c(5) | A_BOLD 
            y_check0 = y+cy >= mapRowOffset 
            y_check1 = y+cy <= endDisplayY 
            #if not y_check0:
            #    game.addLog("Error: y_check0 failed")
            #if not y_check1:
            #    game.addLog("Error: y_check1 failed")
            y_check = y_check0 and y_check1
            x_check0 = x+cx >= beginDisplayX 
            x_check1 = x+cx <= endDisplayX
            x_check = x_check0 and x_check1
            all_checks = y_check and x_check 
            if all_checks :
                self.s.addstr(y + cy, x + cx, e.symbol, options )


    def draw_main_screen_item(self, game, item):
        y = item.y + 5
        x = item.x + 1
        cx = game.camera.x
        cy = game.camera.y 
        rows, cols = self.s.getmaxyx()
        endOfDungeonDisplay = rows - 4
        mapRowOffset = 5
        beginDisplayX = 1
        endDisplayX = cols-1
        #options = None
        #if npc.is_player:
        #    options = c(4) | A_BOLD 
        #else:
        #    options = c(5) | A_BOLD 
        if y+cy >= mapRowOffset and y+cy <= endOfDungeonDisplay and x+cx >= beginDisplayX and x+cx <= endDisplayX :
            self.s.addstr(y + cy, x + cx, item.symbol )



    def process_log(self, y, x, log):
        
        if "ERROR:" in log:
            self.s.addstr(y, x, log, c(2))
        else:
            self.s.addstr(y, x, log)

    def draw_main_screen_logs(self, game):
        # only enough room for last 2 logs
        y, x = 1, 1
        a = len(game.logs)
        b = game.logger_offset 
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
            self.process_log(y,   x, game.logs[a-4+b])
            self.process_log(y+1, x, game.logs[a-3+b])
            self.process_log(y+2, x, game.logs[a-2+b])
            self.process_log(y+3, x, game.logs[a-1+b])












    def getDistance(self, y, x, y0, x0):
        return sqrt((x0 - x)**2) + ((y0 - y)**2)





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
                options = None

                if tileToDraw.tiletype == Tiletype.GRASS:
                    options = c(7)

                tileToDrawStr = str( tileToDraw )

                # the actual tile (y,x) is (i, j) in the dungeon
                distToPC = self.getDistance( i, j, game.pc.y, game.pc.x )
                if distToPC <= game.pc.lightradius:

                    y = i + mapRowOffset + cy
                    x = j + 1 + cx
                    if y >= mapRowOffset and y <= endOfDungeonDisplay and x >= beginDisplayX and x <= endDisplayX :
                        if options:
                            self.s.addstr( y, x, tileToDrawStr, c(7) )
                        else:
                            self.s.addstr( y, x, tileToDrawStr )



    def draw_main_screen_dungeonFloor_npcs(self, game):
        npcs = game.dungeonFloor.npcs
        for npc in npcs:
            self.draw_main_screen_entity(game, npc)
     
    def draw_main_screen_dungeonFloor_items(self, game):
        items = game.dungeonFloor.items
        for item in items:
            self.draw_main_screen_item(game, item)
           
    def drawMainScreenDungeonFloorDoors(self, game):
        assert(game!=None)
        doors = game.dungeonFloor.doors
        for door in doors:
            self.drawMainScreenDoor(game, door)

    def drawMainScreenDoor(self, game, door):
        assert(game!=None)
        assert(door!=None)

        distToPC = self.getDistance( door.y, door.x, game.pc.y, game.pc.x )
        if distToPC <= game.pc.lightradius:
            y = door.y + 5
            x = door.x + 1
            cx = game.camera.x
            cy = game.camera.y 
            rows, cols = self.s.getmaxyx()
            endOfDungeonDisplay = rows - 4
            mapRowOffset = 5
            beginDisplayX = 1
            endDisplayX = cols-1
            symbol = '+' # if isClosed
            if not door.isClosed:
                symbol = '-'
            if y+cy >= mapRowOffset and y+cy <= endOfDungeonDisplay and x+cx >= beginDisplayX and x+cx <= endDisplayX :
                self.s.addstr(y + cy, x + cx, symbol )



    
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



    def drawDebugPanel(self, game):
        assert(game!=None)
        rows, cols = self.s.getmaxyx()
        rowOffset = 4
        y = rows//4 - rowOffset 
        x = cols*3//4
        debugPanel = [
            "-"*(cols//8),
            f"Current Turn: {game.currentTurnCount}",
            f"Number of NPCs in the dungeon: {len(game.dungeonFloor.npcs)}",
            f"Number of items in the dungeon: {len(game.dungeonFloor.items)}",
            "",
            f"Your Base AC: {game.pc.baseAC}",
            f"Dexterity Modifier: {ModTable.getModForScore(game.pc.abilities[1])}",
            f"AC: {game.pc.ac}",
            f"Your Base Attack: {game.pc.baseAttack}",
            "-"*(cols//8),
        ]

        for line in debugPanel:
            self.s.addstr(y, x, line)
            y += 1



    #def draw_main_screen(self,game,pc):
    def draw_main_screen(self,game):
        # experimental main-game drawing
        self.s.clear()

        self.s.border('|','|','-','-','+','+','+','+')

        # order of drawing matters
        # 1. dungeonFloor
        # 2. in-game loot / dropped-objects
        # 3. entities / NPCs
        # 4. border
        
        self.draw_main_screen_logs(game)
        self.draw_main_screen_pc_info(game)
        self.draw_main_screen_dungeonFloor(game)

        self.drawMainScreenDungeonFloorDoors(game)
        

        self.draw_main_screen_dungeonFloor_items(game)
        self.draw_main_screen_dungeonFloor_npcs(game)
        self.draw_main_screen_entity(game, game.pc)

        if game.debugPanel:
            self.drawDebugPanel(game)

        self.s.refresh()
     

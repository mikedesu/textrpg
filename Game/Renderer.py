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
from .EndgameScreen import EndgameScreen
from .ScoreScreen import ScoreScreen

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


    def drawMainscreenBorder(self, game, pc):
        if game==None:
            raise Exception("drawMainscreenBorder: game cannot be None")
        if pc==None:
            raise Exception("drawMainscreenBorder: pc cannot be None")
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

    def drawMainscreenPCInfo(self, game):
        rows, cols = self.s.getmaxyx()
        offsetY = 0
        offsetX = 1
        rootY = rows-3
        rootX = 0
        y = rootY + offsetY
        x = rootX + offsetX
        # draw pc info at bottom of screen
        self.s.addstr(y, x, str(game.pc))
        self.s.addstr(y+1, x, str(game.pc.abilityString()))
        # approximate the middle to drop a turn counter like T:999
        x = int( 23 * cols / 32 )
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


    def drawMainscreenEntity(self, game, e):
        if not e.is_player:
            distToPC = self.getDistance( e.y, e.x, game.pc.y, game.pc.x )
        if e.is_player or distToPC <= game.pc.lightradius:
            rows, cols = self.s.getmaxyx()
            mapRowOffset = 1
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


    def drawMainscreenItem(self, game, item):
        mapRowOffset = 1
        y = item.y + mapRowOffset
        x = item.x + 1
        cx = game.camera.x
        cy = game.camera.y
        rows, cols = self.s.getmaxyx()
        endOfDungeonDisplay = rows - 4
        beginDisplayX = 1
        endDisplayX = cols-1
        check1 = y+cy >= mapRowOffset and y+cy <= endOfDungeonDisplay
        check2 = x+cx >= beginDisplayX and x+cx <= endDisplayX
        if check1 and check2  :
            self.s.addstr(y + cy, x + cx, item.symbol )


    def process_log(self, y, x, log):

        if "ERROR:" in log:
            self.s.addstr(y, x, log, c(2))
        else:
            self.s.addstr(y, x, log)

    def drawMainscreenLogs(self, game):
        # only enough room for last 2 logs
        maxLen = 40
        y, x = 1, 1
        c = 0
        rows, cols = self.s.getmaxyx()
        offset = 0
        #bottomLogs = game.logs[ : row-4 ]
        maxRows = rows-4
        if len(game.logs) > maxRows:
            bottomLogs = game.logs[ -(maxRows):: ]
        else:
            bottomLogs = game.logs

        c = len(bottomLogs)-1
        while c >= 0 and y < maxRows:
            log = ""
            try:
                log = bottomLogs[c]
            except:
                pass
            # handles line-wrapping at a length of 40
            for i in range(0, len(log), maxLen):
                try:
                    line = f"{log[i:i+maxLen]:40}|"
                    self.s.addstr(y, x, line)
                except:
                    pass
                y += 1
            c -= 1







    def getDistance(self, y, x, y0, x0):
        return sqrt((x0 - x)**2) + ((y0 - y)**2)


    def drawMainscreenDungeonFloorTile(self, game, tileToDraw, i, j):
        mapRowOffset = 1
        cx = game.camera.x
        cy = game.camera.y
        rows, cols = self.s.getmaxyx()
        beginDisplayX = 1
        endDisplayX = cols-1
        endOfDungeonDisplay = rows - 4
        options = None
        distToPC = self.getDistance( i, j, game.pc.y, game.pc.x )

        if distToPC <= game.pc.lightradius:
            tileToDraw.isDiscovered = True
        if tileToDraw.isDiscovered:
            if tileToDraw.tiletype == Tiletype.GRASS:
                options = c(7)
            if distToPC <= game.pc.lightradius:
                options = A_BOLD
            tileToDrawStr = str( tileToDraw )
            y = i + mapRowOffset + cy
            x = j + 1 + cx
            check1 = y >= mapRowOffset and y <= endOfDungeonDisplay
            check2 = x >= beginDisplayX and x <= endDisplayX

            if check1 and check2:
                if options:
                    self.s.addstr( y, x, tileToDrawStr, options )
                else:
                    self.s.addstr( y, x, tileToDrawStr )



    def drawMainscreenDungeonFloor(self, game):
        df = game.dungeonFloor
        rows, cols = self.s.getmaxyx()
        d_rows = game.dungeonFloor.rows
        d_cols = game.dungeonFloor.cols
        # camera offsets
        # this is always 9 to accomodate for the 4 rows of logs,
        # 2 rows of dungeon window border
        # and 5 of the text on the bottom i believe
        # same w/ mapRowOffset
        numRowsToSubtract = 9
        beginDisplayX = 1
        endDisplayX = cols-1
        for i in range( len(df.map_) ):
            rowToDraw = df.map_[i]

            for j in range( len(rowToDraw) ):
                tileToDraw = rowToDraw[j]
                self.drawMainscreenDungeonFloorTile(game, tileToDraw, i, j)



    def drawMainscreenDungeonFloorNpcs(self, game):
        npcs = game.dungeonFloor.npcs
        for npc in npcs:
            self.drawMainscreenEntity(game, npc)

    def drawMainscreenDungeonFloorItems(self, game):
        items = game.dungeonFloor.items
        for item in items:
            self.drawMainscreenItem(game, item)

    def drawMainscreenDungeonFloorDoors(self, game):
        assert(game!=None)
        doors = game.dungeonFloor.doors
        for door in doors:
            self.drawMainscreenDoor(game, door)

    def drawMainscreenDoor(self, game, door):
        assert(game!=None)
        assert(door!=None)
        distToPC = self.getDistance( door.y, door.x, game.pc.y, game.pc.x )
        if distToPC <= game.pc.lightradius:
            mapRowOffset = 1
            y = door.y + mapRowOffset
            x = door.x + 1
            cx = game.camera.x
            cy = game.camera.y
            rows, cols = self.s.getmaxyx()
            endOfDungeonDisplay = rows - 4
            beginDisplayX = 1
            endDisplayX = cols-1
            symbol = '+' # if isClosed

            if not door.isClosed:
                symbol = '-'

            if y+cy >= mapRowOffset and y+cy <= endOfDungeonDisplay and x+cx >= beginDisplayX and x+cx <= endDisplayX :
                self.s.addstr(y + cy, x + cx, symbol )


    def draw_quit_screen(self):
        self.s.clear()
        scoreItems = [
            "Score Screen",
            "",
            "More here later"
        ]
        ss = ScoreScreen(scoreItems, self.s)
        ss.display()


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
            f"Your Kill Count: {game.pc.killcount}",
            f"Your Light Radius: {game.pc.lightradius}",
            "-"*(cols//8),
        ]
        for line in debugPanel:
            self.s.addstr(y, x, line)
            y += 1


    #def draw_main_screen(self,game,pc):
    def drawMainscreen(self,game):
        # experimental main-game drawing
        self.s.clear()
        self.s.border('|','|','-','-','+','+','+','+')
        # order of drawing matters
        # 1. dungeonFloor
        # 2. in-game loot / dropped-objects
        # 3. entities / NPCs
        # 4. border
        self.drawMainscreenLogs(game)
        self.drawMainscreenPCInfo(game)
        self.drawMainscreenDungeonFloor(game)
        self.drawMainscreenDungeonFloorDoors(game)
        self.drawMainscreenDungeonFloorItems(game)
        self.drawMainscreenDungeonFloorNpcs(game)
        self.drawMainscreenEntity(game, game.pc)
        if game.debugPanel:
            self.drawDebugPanel(game)
        self.s.refresh()


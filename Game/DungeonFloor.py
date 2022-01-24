from random import randint
from .Entity import Entity
from .Tile import Tile
from .Door import Door
from .Doortype import Doortype
from .Tiletype import Tiletype
from .Item import Item
from .ItemClass import ItemClass
from .NameGenerator import NameGenerator


class DungeonFloor:
    def __init__(self, game=None, rows=0, cols=0):
        # SUPER-basic beginning example
        # assert(game is not None)
        assert(rows > 0)
        assert(cols > 0)
        self.rows = rows
        self.cols = cols
        self.game = game
        self.items = []
        self.npcs = []
        self.doors = []
        self.superBasicDungeon1(rows, cols)

    def __str__(self):
        s = ''
        for i in range(len(self.map_)):
            row = self.map_[i]
            for j in range(len(row)):
                tile = row[j]
                s += str(tile)
                # s += str('x')
            s += '\n'
        return s

    def addDoor(self, y, x):
        d = Door(name="Door1", y=y, x=x, doortype=Doortype.Wooden)
        self.doors.append(d)
        self.map_[y][x].tiletype = Tiletype.STONE_FLOOR

    def updateRowOfTilesYX(self, y, x, cols, tiletype):
        for i in range(cols):
            self.map_[y][x + i].tiletype = tiletype

    def addRowOfTiles(self, cols, tiletype):
        assert(tiletype is not None)
        row = []
        for i in range(cols):
            tile = Tile(tiletype)
            row.append(tile)
        self.map_.append(row)

    def drawBasicRoom(self, tiletype, y, x, rows, cols):
        assert(isinstance(tiletype, Tiletype))
        assert(self.map_ is not None)
        assert(rows > 0)
        assert(cols > 0)
        for i in range(y, y+rows):
            if i < len(self.map_):
                row = self.map_[i]
                for j in range(x, x+cols):
                    tile = row[j]
                    tile.tiletype = tiletype

    def drawBasicHall(self, tiletype, y, x, rows, cols):
        assert(isinstance(tiletype, Tiletype))
        assert(self.map_ is not None)
        assert(isinstance(y, int))
        assert(y >= 0)
        assert(isinstance(x, int))
        assert(x >= 0)
        assert(isinstance(rows, int))
        assert(rows >= 0)
        assert(isinstance(cols, int))
        assert(cols >= 0)
        for row in range(rows):
            self.addRowOfTiles(cols, tiletype)

    def fleshOutMap(self, rows, cols, tiletype):
        for i in range(rows):
            self.addRowOfTiles(cols, tiletype)

    def constructRooms(self, y, x, h, w, walltype, floortype):
        self.drawBasicRoom(walltype, y, x, h, w)
        self.drawBasicRoom(floortype, y+1, x+1, h-2, w-2)

    def addRandomDoor(self, y, x, h, w):
        side = randint(0, 3)
        if side == 0:
            myy = randint(y+1, y+h-2)
            myx = x
        elif side == 1:
            myy = y
            myx = randint(x+1, x+w-2)
        elif side == 2:
            myy = randint(y+1, y+h-2)
            myx = x + w - 1
        elif side == 3:
            myy = y + h - 1
            myx = randint(x+1, x+w-2)
        self.addDoor(myy, myx)

    def superBasicDungeon1Helper(self, rows, cols):
        self.map_ = []
        # 1. flesh out the map with a base tile
        self.fleshOutMap(rows, cols, Tiletype.STONE_FLOOR)
        # 2. construct rooms
        # a hard-coded room at (0,0) of size (12,12)
        y, x = 0, 0
        h, w = 12, 12
        self.constructRooms(y, x, h, w, Tiletype.STONE_WALL,
                            Tiletype.STONE_FLOOR)
        self.addDoor(3, 11)
        # a randomly-placed room at (y,x) of size (5,5)
        numRooms = 3
        for i in range(numRooms):
            h, w = randint(5, 8), randint(5, 8)
            y, x = 0, 0
            y = randint(y+w+1, len(self.map_)-h)
            x = randint(x+h+1, len(self.map_[0])-w)
            self.constructRooms(y, x, h, w, Tiletype.STONE_WALL,
                                Tiletype.STONE_FLOOR)
            # adds a door to a random side at a random point on that side
            self.addRandomDoor(y, x, h, w)

    def superBasicDungeon1(self, rows, cols):
        self.superBasicDungeon1Helper(rows, cols)
        y = 2
        x = 1
        x += 1
        self.items = [
            Item("Short Sword", itemclass=ItemClass.WEAPON, y=y, x=x,
                 weight=1, damage=(1, 6, 0)),
            Item("Long Sword", itemclass=ItemClass.WEAPON, y=y, x=x, weight=1,
                 damage=(1, 8, 0)),
            Item("Mace", itemclass=ItemClass.WEAPON, y=y, x=x, weight=1,
                 damage=(1, 4, 0)),
            Item("Wand", itemclass=ItemClass.WEAPON, y=y, x=x, weight=1,
                 damage=(1, 1, 0)),
            Item("Ration", itemclass=ItemClass.FOOD, y=y, x=x, weight=1,
                 hungerpoints=50)
        ]
        self.npcs = []
        ng = NameGenerator()
        filenames = [
            "monsters/weak-goblin-fighter.json"
        ]
        for i in range(5):
            x = randint(2, 6)
            y = randint(2, 6)
            randomFilename = filenames[randint(0, len(filenames)-1)]
            npc = Entity.loadFromFile(randomFilename)
            npc.x = x
            npc.y = y
            npc.name = ng.generateName()
            npc.is_player = False
            npc.game = self.game
            self.npcs.append(npc)

    def superBasicDungeon0(self, rows, cols):
        self.map_ = []
        self.addRowOfTiles(cols, Tiletype.GRASS)
        self.addRowOfTiles(cols, Tiletype.GRASS)
        for i in range(rows-4):
            self.addRowOfTiles(cols, Tiletype.GRASS)
        self.addRowOfTiles(cols, Tiletype.STONE_FLOOR)
        self.addRowOfTiles(cols, Tiletype.STONE_FLOOR)
        # random_y = 1
        # random_x = 0
        # npc0 = NPC(self.game, name="John", y=5, x=5)
        # self.npcs = [npc0]
        self.npcs = []
        # experimenting with 2 items 1 tile
        item0 = Item("Short Sword", itemclass=ItemClass.WEAPON, y=4, x=0,
                     weight=1)
        item1 = Item("Long Sword", itemclass=ItemClass.WEAPON, y=4, x=0,
                     weight=1)
        item2 = Item("Mace", itemclass=ItemClass.WEAPON, y=4, x=0,
                     weight=1)
        item3 = Item("Wand", itemclass=ItemClass.WEAPON, y=4, x=0,
                     weight=1)
        self.items = [
            item0,
            item1,
            item2,
            item3
        ]

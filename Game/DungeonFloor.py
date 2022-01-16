#from .NPC import NPC 
from random import randint
import sys
from .Entity import Entity
from .Tile import Tile
from .Door import Door 
from .Doortype import Doortype
from .Tiletype import Tiletype 
from .Item import Item
from .ItemClass import ItemClass
from .Race import Race
from .PersonalityTrait import PersonalityTrait
from .NameGenerator import NameGenerator 

class DungeonFloor:
    def __init__(self, game=None, rows=0, cols=0):
        # SUPER-basic beginning example
        assert(game != None)
        assert(rows > 0)
        assert(cols > 0)
        self.rows = rows
        self.cols = cols
        self.game = game
        self.items = []
        self.npcs = []
        self.doors = []
        self.superBasicDungeon1(rows, cols)

    def addDoor(self, y, x):
        d = Door(name="Door1", y=y, x=x, doortype=Doortype.Wooden)
        self.doors.append(d)

    def updateRowOfTilesYX(self, y, x, cols, tiletype):
        for i in range(cols):
            self.map_[y][x + i].tiletype = tiletype

    def addRowOfTiles(self, cols, tiletype):
        assert(tiletype != None)
        row = []
        for i in range(cols):
            tile = Tile(tiletype)
            row.append(tile)
        self.map_.append(row)

    def drawBasicRoom(self, tiletype, y, x, rows, cols):
        assert(isinstance(tiletype, Tiletype))
        assert(self.map_ != None)
        #assert(y >= 0 and y < len(self.map_))
        #assert(x >= 0 and x < len(self.map_[0]))
        assert(rows > 0)
        assert(cols > 0)
        for i in range(y,y+rows):
            if i < len(self.map_):
                row=self.map_[i]
                for j in range(x,x+cols):
                    tile=row[j]
                    tile.tiletype=tiletype

    def drawBasicHall(self, tiletype, y, x, rows, cols):
        assert(isinstance(tiletype, Tiletype))
        assert(self.map_ != None)
        assert(isinstance(y,int))
        assert(y >= 0)
        assert(isinstance(x,int))
        assert(x >= 0)
        assert(isinstance(rows,int))
        assert(rows >= 0)
        assert(isinstance(cols,int))
        assert(cols >= 0)
        for row in range(rows):
            self.addRowOfTiles(cols, tiletype)

    def superBasicDungeon1(self, rows, cols):
        self.map_ = []
        for i in range(rows):
            self.addRowOfTiles(cols, Tiletype.STONE_WALL)
        y=1
        x=1
        h=10
        w=10
        self.drawBasicRoom(Tiletype.STONE_FLOOR, y, x, h, w)
        h=6
        w=6
        y = 1
        x = 6
        for i in range(0,5):
            #y += w + 5
            x += (2*w)
            self.drawBasicRoom(Tiletype.STONE_FLOOR, y, x, h, w)
        y = 3
        x = 11
        h = 1
        w = 7*8
        self.drawBasicRoom(Tiletype.STONE_FLOOR, y, x, h, w)
        y = 2
        x = 1
        item0 = Item( "Short Sword", itemclass=ItemClass.WEAPON, y=y, x=x, weight=1, damage=(1,6,0) )
        item1 = Item( "Long Sword", itemclass=ItemClass.WEAPON, y=y, x=x, weight=1,  damage=(1,8,0) )
        item2 = Item( "Mace", itemclass=ItemClass.WEAPON, y=y, x=x, weight=1,        damage=(1,4,0) )
        item3 = Item( "Wand", itemclass=ItemClass.WEAPON, y=y, x=x, weight=1,        damage=(1,1,0) )

        x += 1
        item4 = Item( "Ration", itemclass=ItemClass.FOOD, y=y, x=x, weight=1)
        item5 = Item( "Ration", itemclass=ItemClass.FOOD, y=y, x=x, weight=1)


        self.items = [ 
            item0,
            item1,
            item2,
            item3,
            item4,
            item5
        ]
        self.addDoor(3,11)
        self.npcs = [   ]
        #npc0 = Entity( self.game, name="John", y=5, x=5 )   
        #self.npcs = [  npc0 ]
        ng = NameGenerator()
        #npc = Entity( self.game, name=n, y=y, x=x )   
        filenames = [
            #"monsters/weak-human-fighter.json",
            #"monsters/weak-elf-fighter.json",
            #"monsters/strong-human-fighter.json",
            "monsters/weak-goblin-fighter.json"
        ]
        for i in range(5):
            x = randint(2,6)
            y = randint(2,6)
            randomFilename = filenames[ randint(0, len(filenames)-1) ]
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
        random_y = 1
        random_x = 0
        npc0 = NPC( self.game, name="John", y=5, x=5 )   
        self.npcs = [  npc0 ]
        #npc1 = NPC( self.game, name="Mike", y=2, x=0 )   
        #npc2 = NPC( self.game, name="Carlos", y=3, x=0, race=Race.ELF, personalityTraits=[PersonalityTrait.SPECIEST_TOWARDS_DWARVES] )   
        #npc2 = NPC( self.game, name="Carlos", y=3, x=0, race=Race.ELF, personalityTraits=[PersonalityTrait.SPECIEST_TOWARDS_DWARVES] )   
        #self.npcs = [ npc0, npc1, npc2 ]
        #self.npcs = [  ]
        # experimenting with 2 items 1 tile
        item0 = Item( "Short Sword", itemclass=ItemClass.WEAPON, y=4, x=0, weight=1 )
        item1 = Item( "Long Sword", itemclass=ItemClass.WEAPON, y=4, x=0, weight=1 )
        item2 = Item( "Mace", itemclass=ItemClass.WEAPON, y=4, x=0, weight=1 )
        item3 = Item( "Wand", itemclass=ItemClass.WEAPON, y=4, x=0, weight=1 )
        self.items = [ 
            item0, 
            item1,
            item2,
            item3
        ] 

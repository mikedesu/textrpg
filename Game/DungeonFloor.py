from .NPC import NPC 
from random import randint

from .Tile import Tile
from .Tiletype import Tiletype 

from .Item import Item
from .ItemClass import ItemClass
from .Race import Race
from .PersonalityTrait import PersonalityTrait

class DungeonFloor:
    def __init__(self, game=None, rows=0, cols=0):
        # SUPER-basic beginning example
        assert(game != None)
        assert(rows > 0)
        assert(cols > 0)
        self.rows = rows
        self.cols = cols
        self.game = game
        self.superBasicDungeon0(rows, cols)




    def addRowOfTiles(self, cols, tiletype):
        assert(tiletype != None)
        row = []
        for i in range(cols):
            tile = Tile(tiletype)
            row.append(tile)
        self.map_.append(row)


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
        #npc0 = NPC( self.game, name="John", y=1, x=0 )   
        #npc1 = NPC( self.game, name="Mike", y=2, x=0 )   
        #npc2 = NPC( self.game, name="Carlos", y=3, x=0, race=Race.ELF, personalityTraits=[PersonalityTrait.SPECIEST_TOWARDS_DWARVES] )   
        #npc2 = NPC( self.game, name="Carlos", y=3, x=0, race=Race.ELF, personalityTraits=[PersonalityTrait.SPECIEST_TOWARDS_DWARVES] )   
        #self.npcs = [ npc0, npc1, npc2 ]
        #self.npcs = [  npc0]
        self.npcs = [  ]
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





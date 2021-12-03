from .NPC import NPC 
from random import randint

from .Tile import Tile
from .Tiletype import Tiletype 

class DungeonFloor:
    def __init__(self, game=None, rows=0, cols=0):
        # SUPER-basic beginning example
        assert(game != None)
        assert(rows > 0)
        assert(cols > 0)
        self.rows = rows
        self.cols = cols
        self.game = game
        self.superBasicDungeon(rows, cols)

    def superBasicDungeon(self, rows, cols):
        self.map_ = []
        row = []
        for i in range(cols):
            tile = Tile(tiletype=Tiletype.STONE_FLOOR)
            row.append(tile)
        self.map_.append(row)
        row = []
        for i in range(rows-2):
            row = []
            tile = Tile(tiletype=Tiletype.STONE_FLOOR)
            row.append(tile)
            for j in range(cols-2):
                tile = Tile(tiletype=Tiletype.STONE_WALL)
                row.append(tile)
            tile = Tile(tiletype=Tiletype.STONE_FLOOR)
            row.append(tile)
            self.map_.append(row)

        row = []
        for i in range(cols):
            tile = Tile(tiletype=Tiletype.STONE_FLOOR)
            row.append(tile)
        self.map_.append(row)

        random_y = randint(0,rows-1)
        random_x = randint(0,cols-1)
        npc = NPC( self.game, y=random_y, x=random_x )   
        self.npcs = [ npc ]




from .NPC import NPC 
from random import randint

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

        self.map_.append("."*cols)
        for i in range(rows-2):
            self.map_.append("#"*cols)
        self.map_.append("."*cols)

        random_y = randint(0,rows-1)
        random_x = randint(0,cols-1)

        npc = NPC( self.game, y=random_y, x=random_x )   
        self.npcs = [ npc ]

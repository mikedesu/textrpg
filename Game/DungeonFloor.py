from .NPC import NPC 

class DungeonFloor:
    def __init__(self, game=None, rows=0, cols=0):
        # SUPER-basic beginning example
        assert(game != None)
        assert(rows > 0)
        assert(cols > 0)
        self.game = game
        self.superBasicDungeon(rows, cols)

    def superBasicDungeon(self, rows, cols):
        self.map_ = []
        for i in range(rows):
            self.map_.append("."*cols)
        self.npcs = [ NPC( self.game, y=0, x=1 ) ]

from .NPC import NPC 

class DungeonFloor:
    def __init__(self, rows, cols):
        # SUPER-basic beginning example
        self.superBasicDungeon(rows, cols)

    def superBasicDungeon(self, rows, cols):
        self.map_ = []
        for i in range(rows):
            self.map_.append("."*cols)

        self.npcs = [ NPC( y=0, x=1 ) ]

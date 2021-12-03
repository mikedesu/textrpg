from .Tiletype import Tiletype

class Tile:
    def __init__(self, tiletype=Tiletype.STONE_FLOOR):
        self.tiletype = tiletype       

    def __str__(self):
        a = {
                Tiletype.STONE_FLOOR : ".",
                Tiletype.STONE_WALL  : "#"
            }
        return a[ self.tiletype ] 


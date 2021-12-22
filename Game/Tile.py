from .Tiletype import Tiletype

class Tile:
    def __init__(self, tiletype=Tiletype.STONE_FLOOR):
        self.tiletype = tiletype       

    @property
    def tiletype(self):
        return self._tiletype
    @tiletype.setter
    def tiletype(self, tt):
        assert(tt!=None)
        assert(isinstance(tt, Tiletype))
        self._tiletype=tt

    def __str__(self):
        a = {
            Tiletype.STONE_FLOOR : ".",
            Tiletype.STONE_WALL  : "#",
            Tiletype.GRASS       : "#",
        }
        return a[ self.tiletype ] 


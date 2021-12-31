from .Tiletype import Tiletype

class Tile:
    def __init__(self, tiletype=Tiletype.STONE_FLOOR, isDiscovered=False):
        self.tiletype = tiletype       
        self.isDiscovered = isDiscovered

    @property
    def tiletype(self):
        return self._tiletype
    @tiletype.setter
    def tiletype(self, tt):
        assert(tt!=None)
        assert(isinstance(tt, Tiletype))
        self._tiletype=tt

    @property
    def isDiscovered(self):
        return self._isDiscovered
    @isDiscovered.setter
    def isDiscovered(self,d):
        assert(d!=None)
        assert(isinstance(d,bool))
        self._isDiscovered=d
    

    def __str__(self):
        a = {
            Tiletype.STONE_FLOOR : ".",
            Tiletype.STONE_WALL  : "#",
            Tiletype.GRASS       : "#",
        }
        return a[ self.tiletype ] 


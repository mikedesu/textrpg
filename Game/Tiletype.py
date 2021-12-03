from enum import Enum

class Tiletype(Enum):
    STONE_FLOOR   = 1
    STONE_WALL    = 2

    def __str__(self):
        a = ["STONE_FLOOR", "STONE_WALL"]
        return a[ self.value ]
 

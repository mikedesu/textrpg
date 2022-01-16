from enum import Enum

class ItemClass(Enum):
    WEAPON = 1
    FOOD = 2

    def __str__(self):
        a = [
            '',
            'WEAPON',
            'FOOD'
            ]
        return a[ self.value ]
 

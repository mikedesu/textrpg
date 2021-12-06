from enum import Enum

class ItemClass(Enum):
    WEAPON = 1

    def __str__(self):
        if self.value == 1:
            return "WEAPON"
 

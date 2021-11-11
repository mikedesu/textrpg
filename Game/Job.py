from enum import Enum

class Job(Enum):
    FIGHTER = 1
    CLERIC  = 2
    MAGE    = 3
    THIEF   = 4

    def __str__(self):
        if self.value == 1:
            return "Fighter"
        elif self.value == 2:
            return "Cleric"
        elif self.value == 3:
            return "Mage"
        elif self.value == 4:
            return "Thief"
        

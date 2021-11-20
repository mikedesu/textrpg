from enum import Enum

class Alignment(Enum):
    LAWFUL_GOOD    = 1 
    LAWFUL_NEUTRAL = 2
    LAWFUL_EVIL    = 3
    NEUTRAL_GOOD = 4
    TRUE_NEUTRAL = 5
    NEUTRAL_EVIL = 6
    CHAOTIC_GOOD    = 7
    CHAOTIC_NEUTRAL = 8
    CHAOTIC_EVIL    = 9

    def __str__(self):
        a = "Undefined"
        if self.value == 1:
            a = "Lawful Good"
        elif self.value == 2:
            a = "Lawful Neutral"
        elif self.value == 3:
            a = "Lawful Evil"
        elif self.value == 4:
            a = "Neutral Good"
        elif self.value == 5:
            a = "True Neutral"
        elif self.value == 6:
            a = "Neutral Evil"
        elif self.value == 7:
            a = "Chaotic Good"
        elif self.value == 8:
            a = "Chaotic Neutral"
        elif self.value == 9:
            a = "Chaotic Evil"
        return a

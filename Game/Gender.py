from enum import Enum

class Gender(Enum):
    MALE   = 1
    FEMALE = 2

    def __str__(self):
        if self.value == 1:
            return "Male"
        elif self.value == 2:
            return "Female"
 

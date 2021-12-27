from enum import Enum
class Doortype(Enum):
    Wooden = 0
    def __str__(self):
        a=["Wooden"]
        return a[ self.value ]
 

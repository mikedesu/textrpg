
from enum import Enum

__sizes = ['Humanoid']

class Size(Enum):
    Humanoid = 1

    def __str__(self):
        global __sizes
        return __sizes[self.value]


from enum import Enum


class Bodypart(Enum):
    Righthand = 0
    Lefthand = 1

    def __str__(self):
        bpstrings = [
            "Right hand",
            "Left hand"
        ]
        return bpstrings[self.value]

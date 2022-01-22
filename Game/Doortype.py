from enum import Enum


class Doortype(Enum):
    Wooden = 0
    Iron = 1
    Steel = 2
    Rock = 3

    def __str__(self):
        a = ["Wooden", "Iron", "Steel", "Rock"]
        return a[self.value]

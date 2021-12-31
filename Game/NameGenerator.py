
from random import randint

class NameGenerator:
    def __init__(self):
        # basic start
        self.names = [
            "Mike",
            "John",
            "Satan",
            "Jesus",
            "God"
        ]

    def generateName(self):
        return self.names[ randint( 0,len(self.names)-1 ) ]

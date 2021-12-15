from enum import Enum

class PersonalityTrait(Enum):
    NORMAL = 1
    SPECIEST_TOWARDS_DWARVES = 2
    SPECIEST_TOWARDS_ELVES = 3
    SPECIEST_TOWARDS_GNOMES = 4
    SPECIEST_TOWARDS_GOBLINS = 5
    SPECIEST_TOWARDS_HUMANS = 6

    def __str__(self):
        names = ["", "Normal", 
                "Speciest-Towards-Dwarves",
                "Speciest-Towards-Elves",
                "Speciest-Towards-Gnomes",
                "Speciest-Towards-Goblins",
                "Speciest-Towards-Humans"
                ]
        return names[ self.value ]    
        

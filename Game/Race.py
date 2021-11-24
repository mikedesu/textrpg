from enum import Enum

class Race(Enum):
    HUMAN = 1
    ELF   = 2
    DWARF = 3
    GNOME = 4
    GOBLIN = 5

    def __str__(self):
        names = ["", "Human", "Elf", "Dwarf", "Gnome", "Goblin"]
        return names[ self.value ]    
        

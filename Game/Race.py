from enum import Enum

class Race(Enum):
    HUMAN = 1
    ELF   = 2
    DWARF = 3
    GNOME = 4

    def __str__(self):
        if self.value == 1:
            return "Human"
        elif self.value == 2:
            return "Elf"
        elif self.value == 3:
            return "Dwarf"
        elif self.value == 4:
            return "Gnome"
        

from .Race import Race
from .Job import Job
from .Attribs import Attribs as a
from .Gender import Gender
from .Alignment import Alignment

class ZeroLevelException(Exception):
    pass
class NegativeLevelException(Exception):
    pass
class NegativeAttributeException(Exception):
    pass

###############################################################################
class NPC:
    def __init__(self, name="Unnamed", level=1, race=Race.HUMAN, 
        job=Job.FIGHTER, attribs=[10,10,10,10,10,10], y=0, x=0, 
        gender=Gender.MALE, alignment=Alignment.LAWFUL_GOOD, is_player=False, symbol="@"):
        # basic checks on numeric input parameters
        if level == 0:
            raise ZeroLevelException 
        elif level < 0:
            raise NegativeLevelException 
        for a in attribs:
            if a < 0:
                raise NegativeAttributeException 
        self.name = name
        self.level = level
        self.race = race
        self.job = job
        self.attribs = attribs 
        self.y = y
        self.x = x
        self.gender = gender
        self.alignment = alignment 
        self.is_player = is_player 
        self.symbol = symbol 


    def __str__(self):
        s = f"{self.name} Level {self.level} {self.alignment} {self.race} {self.job}\n"
        s += f"Str: {self.attribs[0]} "
        s += f"Dex: {self.attribs[1]} "
        s += f"Con: {self.attribs[2]} "
        s += f"Int: {self.attribs[3]} "
        s += f"Wis: {self.attribs[4]} "
        s += f"Cha: {self.attribs[5]} "
        return s

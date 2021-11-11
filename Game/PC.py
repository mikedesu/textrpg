from .Race import Race
from .Job import Job
from .Attribs import Attribs 

class PC:
    def __init__(self, name="Unnamed", level=1, race=Race.HUMAN, job=Job.FIGHTER, attribs=[10,10,10,10,10,10]):
        self.name = name
        self.level = level
        self.race = race
        self.job = job
        self.attribs = attribs 

    def __str__(self):
        s = f"{self.name} Level {self.level} {self.race} {self.job} {self.attribs[a.STRENGTH]}/{self.attribs[a.DEXTERITY]}/{self.attribs[a.CONSTITUTION]}/{self.attribs[a.INTELLIGENCE]}/{self.attribs[a.WISDOM]}/{self.attribs[a.CHARISMA]}"
        return s
    def __repr__(self):
        return str(self)

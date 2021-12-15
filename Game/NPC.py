from .Race import Race
from .Job import Job
from .Attribs import Attribs as a
from .Gender import Gender
from .Alignment import Alignment
from .PersonalityTrait import PersonalityTrait 
from random import randint

class ZeroLevelException(Exception):
    pass
class NegativeLevelException(Exception):
    pass
class NegativeAttributeException(Exception):
    pass

###############################################################################
class NPC:
    def __init__(self, game=None, name="Unnamed", level=1, race=Race.HUMAN, 
        job=Job.FIGHTER, attribs=[10,10,10,10,10,10], y=0, x=0, 
        gender=Gender.MALE, alignment=Alignment.LAWFUL_GOOD, is_player=False, 
        symbol="@", hp=10, maxhp=10, ac=10, personalityTraits=[PersonalityTrait.NORMAL] ):
        if game == None:
            raise Exception("Game cannot be None")
        # basic checks on numeric input parameters
        if level == 0:
            raise ZeroLevelException 
        elif level < 0:
            raise NegativeLevelException 
        for a in attribs:
            if a < 0:
                raise NegativeAttributeException 
        self.game = game
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
        self.ac = ac
        self.hp = hp
        self.maxhp = maxhp
        self.xp = 0
        self.hunger = 255
        self.maxhunger = 255
        self.items = []
        self.personalityTraits = personalityTraits 

    def attack(self, target, doLog):
        # traditional dnd 3.0 rules:
        # 1d20 
        roll = randint(1, 20)
        # if the roll is >= player's ac, attack hits
        if roll >= target.ac:
            # for right now, lets just subtract 1 hp until we come back to 
            # properly write the damage calc rules
            target.hp -= 1
            if doLog:
                self.game.addLog(f"{self.game.currentTurnCount}: {self.name}'s attack hit {target.name}!")
        else:
            # we dont need to do anything but we should log both a hit or a 
            # miss so we need a way to pass msgs to the game log
            if doLog:
                self.game.addLog(f"{self.game.currentTurnCount}: {self.name}'s attack missed {target.name}!")

    def __str__(self):
        s = f"{self.name} Level {self.level} {self.alignment} {self.race} {self.job}\n"
        s += f"Str: {self.attribs[0]} "
        s += f"Dex: {self.attribs[1]} "
        s += f"Con: {self.attribs[2]} "
        s += f"Int: {self.attribs[3]} "
        s += f"Wis: {self.attribs[4]} "
        s += f"Cha: {self.attribs[5]} "
        s += f"HP: {self.hp}/{self.maxhp} "
        s += f"XP: {self.xp} "
        #hungerStr = f"H:{self.hunger}/{self.maxhunger}"
        #s += hungerStr 
        return s

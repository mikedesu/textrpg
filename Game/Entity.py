from .Race import Race
from .Job import Job
from .Attribs import Attribs as a
from .Gender import Gender
from .Alignment import Alignment
from .PersonalityTrait import PersonalityTrait 
from .Item import Item
from .ModTable import ModTable

from random import randint
#from . import Game

class ZeroLevelException(Exception):
    pass
class NegativeLevelException(Exception):
    pass
class NegativeAttributeException(Exception):
    pass

###############################################################################
class Entity:
    def __init__(self, game=None, name="Unnamed", level=1, race=Race.HUMAN, 
        job=Job.FIGHTER, abilities=[10,10,10,10,10,10], y=0, x=0, 
        gender=Gender.MALE, alignment=Alignment.LAWFUL_GOOD, is_player=False, 
        symbol="@", hd=(1,4), ac=10, personalityTraits=[PersonalityTrait.NORMAL],
        lightradius=2, baseAttack=0):
        if game == None:
            raise Exception("Game cannot be None")
        # basic checks on numeric input parameters
        if level == 0:
            raise ZeroLevelException 
        elif level < 0:
            raise NegativeLevelException 
        for a in abilities:
            if a < 0:
                raise NegativeAttributeException 
        self.game = game
        self.name = name
        self.level = level
        self.race = race
        self.job = job
        self.abilities = abilities
        self.y = y
        self.x = x
        self.gender = gender
        self.alignment = alignment 
        self.is_player = is_player 
        self.symbol = symbol 

        self.baseAC = ac
        self.baseAttack = baseAttack

        self.hd = hd
        self.hunger = 255
        self.maxhunger = 255
        self.xp = 0
        self.personalityTraits = personalityTraits 
        # construct maxhp by rolling 1d(hd[1]) die hd[0]-times
        self.maxhp = 0
        for i in range( self.hd[0] ):
            self.maxhp += randint( 1, hd[1] )
        self.hp = self.maxhp
        # set entity items
        self.items = []
        self.righthand = None
        self.lefthand = None
        self.lightradius = lightradius



    @property
    def baseAttack(self):
        return self._baseAttack
    @baseAttack.setter
    def baseAttack(self, ac):
        assert(ac!=None)
        #assert(isinstance(ac,int))
        self._baseAttack=ac



    @property
    def baseAC(self):
        return self._baseAC
    @baseAC.setter
    def baseAC(self, ac):
        #assert(isinstance(ac,int))
        self._baseAC=ac

    @property
    def ac(self):
        dexMod = ModTable.getModForScore(self.abilities[1])
        return self.baseAC + dexMod


    @property
    def righthand(self):
        return self._righthand
    @righthand.setter
    def righthand(self, item):
        #assert(item == None or isinstance(item,Item))
        #raise Exception(f"item is {type(item)}")
        self._righthand = item 

    @property
    def lefthand(self):
        return self._lefthand
    @lefthand.setter
    def lefthand(self, item):
        #assert(item == None or isinstance(item,Item))
        #raise Exception(f"item is {type(item)}")
        self._lefthand = item 







    @property
    def level(self):
        return self._level 
    @level.setter
    def level(self, a):
        self._level=a

    @property
    def race(self):
        return self._race
    @race.setter
    def race(self, v):
        assert(v!=None)
        self._race=v

    @property
    def job(self):
        return self._job
    @job.setter
    def job(self, v):
        assert(v!=None)
        self._job=v

    @property
    def abilities(self):
        return self._abilities
    @abilities.setter
    def abilities(self, v):
        assert(v!=None)
        self._abilities=v

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, v):
        assert(v!=None)
        self._y=v

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, v):
        assert(v!=None)
        self._x=v

    @property
    def gender(self):
        return self._gender
    @gender.setter
    def gender(self, v):
        assert(v!=None)
        self._gender=v

    @property
    def alignment(self):
        return self._alignment
    @alignment.setter
    def alignment(self, v):
        assert(v!=None)
        self._alignment=v

    @property
    def is_player(self):
        return self._is_player
    @is_player.setter
    def is_player(self, v):
        assert(v!=None)
        self._is_player=v

    @property
    def symbol(self):
        return self._symbol
    @symbol.setter
    def symbol(self, v):
        assert(v!=None)
        self._symbol=v

    #@property
    #def ac(self):
    #    return self._ac
    #@ac.setter
    #def ac(self, v):
    #    assert(v!=None)
    #    self._ac=v

    @property
    def hd(self):
        return self._hd
    @hd.setter
    def hd(self, v):
        assert(v!=None)
        self._hd=v

    @property
    def hunger(self):
        return self._hunger
    @hunger.setter
    def hunger(self, v):
        assert(v!=None)
        self._hunger=v

    @property
    def maxhunger(self):
        return self._maxhunger
    @maxhunger.setter
    def maxhunger(self, v):
        assert(v!=None)
        self._maxhunger=v

    @property
    def xp(self):
        return self._xp
    @xp.setter
    def xp(self, v):
        assert(v!=None)
        self._xp=v

    @property
    def personalityTraits(self):
        return self._personalityTraits
    @personalityTraits.setter
    def personalityTraits(self, v):
        assert(v!=None)
        self._personalityTraits=v

    @property
    def maxhp(self):
        return self._maxhp
    @maxhp.setter
    def maxhp(self, v):
        assert(v!=None)
        self._maxhp=v

    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self, v):
        assert(v!=None)
        self._hp=v

    @property
    def items(self):
        return self._items
    @items.setter
    def items(self, v):
        assert(v!=None)
        self._items=v
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, n):
        assert(n!=None)
        assert(isinstance(n,str))
        self._name = n

    @property
    def game(self):
        return self._game
    @game.setter
    def game(self, g):
        assert(g!=None)
        #assert(isinstance(g,Game))
        self._game = g




    def addItemToInventory(self, item):
        assert(item != None)
        assert(isinstance(item, Item))
        # make sure item isnt double-added
        if item not in self.items:
            self.items.append(item)

    
    @property
    def baseDamage(self):
        weapon = self.righthand
        numWeaponRolls = 1
        weaponDie      = 1
        weaponMod      = 0
        if weapon != None:
            numWeaponRolls = weapon.damage[0]
            weaponDie      = weapon.damage[1]
            weaponMod      = weapon.damage[2]
        return (numWeaponRolls, weaponDie, weaponMod)


    def attack(self, target, doLog):

        # depends on which hand a weapon is equipped in
        # for right now we shall code for right hand
        #weapon = self.righthand
        #numWeaponRolls = 1
        #weaponDie      = 1
        #weaponMod      = 0
        #if weapon != None:
        #    numWeaponRolls = weapon.damage[0]
        #    weaponDie      = weapon.damage[1]
        #    weaponMod      = weapon.damage[2]
        baseDamage = self.baseDamage
        numWeaponRolls = baseDamage[0]
        weaponDie      = baseDamage[1]
        weaponMod      = baseDamage[2]

        # traditional dnd 3.0 rules:
        # 1d20 for attack
        roll = randint(1, 20)
        total = roll + self.baseAttack

        # if the roll is >= player's ac, attack hits
        if total >= target.ac:
            # for right now, lets just subtract 1 hp until we come back to 
            # properly write the damage calc rules

            # damage roll
            damage = randint(1, weaponDie)
            for i in range(1,numWeaponRolls-1):
                damage += randint(1, weaponDie)

            target.hp -= damage
            if doLog:
                self.game.addLog(f"{self.game.currentTurnCount}: {self.name}'s attack hit {target.name}!")
        else:
            # we dont need to do anything but we should log both a hit or a 
            # miss so we need a way to pass msgs to the game log
            if doLog:
                self.game.addLog(f"{self.game.currentTurnCount}: {self.name}'s attack missed {target.name}!")












    def __str__(self):
        s = f"{self.name} Level {self.level} {self.alignment} {self.race} {self.job}\n"
        s += f"Str: {self.abilities[0]} "
        s += f"Dex: {self.abilities[1]} "
        s += f"Con: {self.abilities[2]} "
        s += f"Int: {self.abilities[3]} "
        s += f"Wis: {self.abilities[4]} "
        s += f"Cha: {self.abilities[5]} "
        s += f"HP: {self.hp}/{self.maxhp} "
        s += f"XP: {self.xp} "
        #hungerStr = f"H:{self.hunger}/{self.maxhunger}"
        #s += hungerStr 
        return s

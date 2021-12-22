
from .Sizes import Sizes
from .Alignment import Alignment

class MonsterDefinition:
    def __init__(self):
        self.name = "elf"
        self.size = Size.Humanoid
        self.hd = (1, 8)
        self.initiative = 1
        self.speed = 1
        self.armorClass = 15
        self.baseAttack = 1
        self.attack = (1, 8, 1)
        self.reach = 1
        #self.specialAttacks = None
        #self.specialQualities = None
        #self.savingThrows = "Fort +2 Ref +1 Will -1"
        self.savingThrows = [2, 1, -1]
        self.abilities = [13,13,10,10,9,8]
       # self.skills = [
       #     ('hide',   1),
       #     ('listen', 2),
       #     ('search', 3),
       #     ('spot',   2),
       # ]
       # self.feats = [
       #     ('weapon focus', 'long bow')
       # ]
       # self.environments = [
       #     'temperate forest'
       # ]
        self.challengeRating = 0.5
        self.treasure = 'standard'
        self.alignment = Alignment.CHAOTIC_GOOD
    

    @property
    def alignment(self):
        return self._alignment
    @alignment.setter
    def alignment(self,v):
        assert(v!=None)
        assert(isinstance(v,Alignment))
        self._alignment = v




    @property
    def treasure(self):
        return self._treasure
    @treasure.setter
    def treasure(self,v):
        assert(v!=None)
        assert(isinstance(v,str))
        self._treasure = v


     

    @property
    def challengeRating(self):
        return self._challengeRating
    @challengeRating.setter
    def challengeRating(self,v):
        assert(v!=None)
        assert(isinstance(v,float))
        self._challengeRating = v



    @property
    def abilities(self):
        return self._abilities
    @abilities.setter
    def abilities(self,v):
        assert(v!=None)
        assert(isinstance(v,list))
        assert(len(v)==6)
        self._abilities = v


    

    @property
    def savingThrows(self):
        return self._savingThrows
    @savingThrows.setter
    def savingThrows(self,v):
        assert(v!=None)
        assert(isinstance(v,list))
        assert(len(v)==3)
        self._savingThrows = v

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, myattack):
        assert(myattack != None)
        assert(isinstance(myattack, tuple))
        self._attack=myattack
    




    @property
    def hd(self):
        return self._hd

    @hd.setter
    def hd(self, myhd):
        assert(myhd != None)
        assert(isinstance(myhd, tuple))
        self._hd=hd
    

    @property
    def reach(self):
        return self._reach

    @reach.setter
    def reach(self, v):
        assert(v!=None)
        assert(isinstance(v,int))
        self._reach=reach




    @property
    def baseAttack(self):
        return self._baseAttack

    @baseAttack.setter
    def baseAttack(self, v):
        assert(v!=None)
        assert(isinstance(v,int))
        self._baseAttack=baseAttack



    @property
    def armorClass(self):
        return self._armorClass

    @armorClass.setter
    def armorClass(self, v):
        assert(v!=None)
        assert(isinstance(v,int))
        self._armorClass=armorClass




    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, v):
        assert(v!=None)
        assert(isinstance(v,int))
        self._speed=speed




    @property
    def initiative(self):
        return self._initiative

    @initiative.setter
    def initiative(self, v):
        assert(v!=None)
        assert(isinstance(v,int))
        self._initiative=initiative

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,n):
        assert(n!=None)
        assert(isinstance(n,str))
        assert(n!="")
        self._name = n

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, sz):
        assert(sz!=None)
        assert(isinstance(sz,Size))
        self._size=sz

    def loadFromString(self, line):
        assert(line != None)
        assert(isinstance(line, str))
        assert(line != "")
        a = line.split(',')
        self.name = a[0]
        self.size = a[1]
        self.hd = (a[2], a[3])
        self.initiative = a[4]
        self.speed = a[5]
        self.armorClass = a[6]
        self.baseAttack = a[7]
        self.attack = (a[8], a[9], a[10])
        self.reach = a[11]
        self.savingThrows = [a[12], a[13], a[14]]
        self.abilities = [a[15],a[16],a[17],a[18],a[19],a[20]]
        self.treasure = a[21]
        self.challengeRating = a[22]
        self.alignment = Alignment.CHAOTIC_GOOD
    


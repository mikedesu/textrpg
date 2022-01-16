from .ItemClass import ItemClass

class Item:
    def __init__(self, name='Unnamed Item', 
            itemclass=ItemClass.WEAPON, 
            x=0, 
            y=0, 
            weight=0, 
            damage=(1,4,0),
            hungerpoints=0,
            symbol='*' 
        ):
        assert(name != "")
        assert(name != None)
        assert(itemclass != None) 
        self.name = name
        self.itemclass = itemclass 
        self.x = x
        self.y = y
        self.weight = weight
        # future items will have unique symbols based on itemclass and other factors
        self.symbol = symbol
        self.damage = damage
        self.hungerpoints = hungerpoints
        self.updateSymbol()

    @property
    def hungerpoints(self):
        return self._hungerpoints
    @hungerpoints.setter
    def hungerpoints(self,v):
        self._hungerpoints=v
        

    @property 
    def damage(self):
        return self._damage
    @damage.setter
    def damage(self, dmg):
        assert(dmg!=None)
        assert(isinstance(dmg,tuple))
        self._damage=dmg


    def updateSymbol(self):
        assert(self.itemclass!=None)
        symDict = {
            ItemClass.WEAPON : ')',
            ItemClass.FOOD   : '%'
        }
        self.symbol = symDict[ self.itemclass ] 

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,n):
        assert(n!=None)
        assert(isinstance(n,str))
        self._name=n

    @property
    def itemclass(self):
        return self._itemclass
    @itemclass.setter
    def itemclass(self, ic):
        assert(ic!=None)
        assert(isinstance(ic,ItemClass))
        self._itemclass=ic

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, x0):
        assert(x0!=None)
        assert(isinstance(x0,int))
        assert(x0>=0)
        self._x=x0

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, y0):
        assert(y0!=None)
        assert(isinstance(y0,int))
        assert(y0>=0)
        self._y=y0

    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self, w):
        assert(w!=None)
        assert(isinstance(w,int))
        assert(w>=0)
        self._weight=w

    @property
    def symbol(self):
        return self._symbol
    @symbol.setter
    def symbol(self, sym):
        assert(sym!=None)
        assert(isinstance(sym,str))
        self._symbol = sym 

    def __str__(self):
        return self.name 


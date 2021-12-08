
from .ItemClass import ItemClass


class Item:
    def __init__(self, name='Unnamed Item', itemclass=ItemClass.WEAPON, x=0, y=0, weight=0, symbol='*' ):
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

    def __str__(self):
        return self.name 


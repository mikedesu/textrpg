
from .ItemClass import ItemClass


class Item:
    def __init__(self, name="Unnamed Item", itemclass=ItemClass.WEAPON, x=0, y=0 ):
        assert(name != "")
        assert(name != None)
        assert(itemclass != None) 
        self.name = name
        self.itemclass = itemclass 
        self.x = x
        self.y = y

        # future items will have unique symbols based on itemclass and other factors
        self.symbol = "*"

    def __str__(self):
        return self.name 


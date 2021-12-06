
from .ItemClass import ItemClass


class Item:
    def __init__(self, name="Unnamed Item", itemclass=ItemClass.WEAPON):
        assert(name != "")
        assert(name != None)
        assert(itemclass != None) 
        self.name = name
        self.itemclass = itemclass 

    def __str__(self):
        return self.name 


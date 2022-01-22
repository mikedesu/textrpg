from .Doortype import Doortype


class Door:
    def __init__(self, name="Door", y=0, x=0, doortype=Doortype.Wooden,
                 isClosed=True):
        self.y = y
        self.x = x
        self.doortype = doortype
        self.isClosed = isClosed

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        assert(y is not None)
        assert(y >= 0)
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        assert(x is not None)
        assert(x >= 0)
        self._x = x

    @property
    def doortype(self):
        return self._doortype

    @doortype.setter
    def doortype(self, v):
        assert(v is not None)
        self._doortype = v

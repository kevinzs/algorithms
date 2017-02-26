class Cell(object):
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y
        self._dead = True
        self._nextstate = True

    @property
    def x(self):
        return self._x

    @x.getter
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.getter
    def y(self):
        return self._y

    @property
    def dead(self):
        return self._dead

    @dead.setter
    def dead(self, dead):
        self._dead = dead

    @property
    def nextstate(self):
        return self._nextstate

    @nextstate.setter
    def nextstate(self, nextstate):
        self._nextstate = nextstate

    def setnextstate(self):
        self._dead = self._nextstate

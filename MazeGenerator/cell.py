import pygame


class Cell:
    """
    Cell types:
        1 - Wall cell
        2 - Visited cell
        3 - Backtrack Cell (for debugging)
    """

    def __init__(self, x=0, y=0, cellsize=0, type=1):
        self.x = x
        self.y = y
        self.cellsize = cellsize
        self._type = type

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, typ):
        self._type = typ

    def render(self, screen):
        if self.type == 1:
            pygame.draw.rect(screen, (51, 51, 51), (self.x, self.y, self.cellsize, self.cellsize))
        elif self.type == 2:
            pygame.draw.rect(screen, (226, 226, 226), (self.x, self.y, self.cellsize, self.cellsize))
        elif self.type == 3:
            pygame.draw.rect(screen, (77, 148, 255), (self.x, self.y, self.cellsize, self.cellsize))

    def set_type(self, _type):
        self.type = _type

    def __repr__(self):
        return '' + str(self.x) + ' ' + str(self.y)




import pygame


class Cell:
    """
    Cell types:
        1 - Normal cell
        2 - Wall cell
        3 - Visited Cell
        4 - Frontier cell
        5 - Start cell
        6 - End cell
        7 - Path Cell
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
            pygame.draw.rect(screen, (226, 226, 226), (self.x, self.y, self.cellsize, self.cellsize))
        elif self.type == 2:
            pygame.draw.rect(screen, (51, 51, 51), (self.x, self.y, self.cellsize, self.cellsize))
        elif self.type == 3:
            pygame.draw.rect(screen, (179, 179, 179), (self.x, self.y, self.cellsize, self.cellsize))
        elif self.type == 4:
            pygame.draw.rect(screen, (95, 95, 95), (self.x, self.y, self.cellsize, self.cellsize))
        elif self.type == 5:
            pygame.draw.rect(screen, (240, 10, 10), (self.x, self.y, self.cellsize, self.cellsize))
        elif self.type == 6:
            pygame.draw.rect(screen, (0, 190, 20), (self.x, self.y, self.cellsize, self.cellsize))
        elif self.type == 7:
            pygame.draw.rect(screen, (153, 0, 204), (self.x, self.y, self.cellsize, self.cellsize))

    def set_type(self, _type):
        self.type = _type

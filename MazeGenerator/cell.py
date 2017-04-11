import pyglet


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

    def render(self):
        if self.type == 1:
            pyglet.gl.glColor3f(51 / 255, 51 / 255, 51 / 255)
        elif self.type == 2:
            pyglet.gl.glColor3f(226 / 255, 226 / 255, 226 / 255)
        elif self.type == 3:
            pyglet.gl.glColor3f(77 / 255, 148 / 255, 255 / 255)

        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2f', [self.x, self.y,
                                      self.x + self.cellsize, self.y,
                                      self.x + self.cellsize,
                                      self.y + self.cellsize,
                                      self.x, self.y + self.cellsize])
                             )

    def set_type(self, _type):
        self.type = _type

    def __repr__(self):
        return '' + str(self.x) + ' ' + str(self.y)




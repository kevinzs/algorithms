import pyglet


class Cell:
    """
    Cell types:
        1 - Normal cell
        2 - Wall cell
        3 - Visited Cell
        4 - Frontier cell
        5 - Start cell
        6 - End cell
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
            pyglet.gl.glColor3f(223/255, 255 / 255, 128 / 255)
        elif self.type == 2:
            pyglet.gl.glColor3f(230 / 255, 145 / 255, 0)
        elif self.type == 3:
            pyglet.gl.glColor3f(128 / 255, 212 / 255, 255 / 255)
        elif self.type == 4:
            pyglet.gl.glColor3f(0, 116 / 255, 191 / 255)
        elif self.type == 5:
            pyglet.gl.glColor3f(240 / 255, 10 / 255, 10 / 255)
        elif self.type == 6:
            pyglet.gl.glColor3f(0 / 255, 190 / 255, 20 / 255)

        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2f', [self.x, self.y,
                                      self.x + self.cellsize, self.y,
                                      self.x + self.cellsize,
                                      self.y + self.cellsize,
                                      self.x, self.y + self.cellsize])
                             )

    def set_type(self, _type):
        self.type = _type

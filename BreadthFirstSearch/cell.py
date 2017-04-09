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

    def render(self):
        if self.type == 1:
            pyglet.gl.glColor3f(226 / 255, 226 / 255, 226 / 255)
        elif self.type == 2:
            pyglet.gl.glColor3f(51 / 255, 51 / 255, 51 / 255)
        elif self.type == 3:
            pyglet.gl.glColor3f(179 / 255, 179 / 255, 179 / 255)
        elif self.type == 4:
            pyglet.gl.glColor3f(95 / 255, 95 / 255, 95 / 255)
        elif self.type == 5:
            pyglet.gl.glColor3f(240 / 255, 10 / 255, 10 / 255)
        elif self.type == 6:
            pyglet.gl.glColor3f(0 / 255, 190 / 255, 20 / 255)
        elif self.type == 7:
            pyglet.gl.glColor3f(153 / 255, 0 / 255, 204 / 255)

        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2f', [self.x, self.y,
                                      self.x + self.cellsize, self.y,
                                      self.x + self.cellsize,
                                      self.y + self.cellsize,
                                      self.x, self.y + self.cellsize])
                             )

    def set_type(self, _type):
        self.type = _type

import pygame
from GameOfLife.cell import Cell


class Grid(object):
    def __init__(self, width=0, height=0, cellsize=15):
        self._width = width
        self._height = height
        self._cellSize = cellsize
        self._cells = [[Cell() for i in range(int(self._width / self._cellSize))]
                       for j in range(int(self._height / self._cellSize) + self._cellSize)]
        for i in range(0, len(self._cells)):
            for j in range(0, len(self._cells[0])):
                self._cells[i][j] = Cell(i * self._cellSize, j * self._cellSize)

    def draw_cells(self, screen):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[0])):
                if self._cells[i][j].dead:
                    pygame.draw.rect(screen, (0, 0, 0), (self._cells[i][j].x, self._cells[i][j].y,
                                                         self._cellSize, self._cellSize))
                else:
                    pygame.draw.rect(screen, (255, 255, 255), (self._cells[i][j].x, self._cells[i][j].y,
                                                               self._cellSize, self._cellSize))

    def setalivecell(self, x, y):
        try:
            self._cells[int(x / self._cellSize)][int(y / self._cellSize)].dead = False
        except IndexError:
            pass

    def transition(self):
        # Calculate next cell state
        for i in range(len(self._cells)):
            for j in range(len(self._cells[0])):
                neighbours = 0
                # Calculate live neighbours
                try:
                    if not self._cells[i - 1][j - 1].dead:
                        neighbours += 1
                    if not self._cells[i - 1][j].dead:
                        neighbours += 1
                    if not self._cells[i - 1][j + 1].dead:
                        neighbours += 1
                    if not self._cells[i][j - 1].dead:
                        neighbours += 1
                    if not self._cells[i][j + 1].dead:
                        neighbours += 1
                    if not self._cells[i + 1][j - 1].dead:
                        neighbours += 1
                    if not self._cells[i + 1][j].dead:
                        neighbours += 1
                    if not self._cells[i + 1][j + 1].dead:
                        neighbours += 1
                except IndexError:
                    pass

                # Rules
                if not self._cells[i][j].dead:
                    if neighbours < 2:
                        self._cells[i][j].nextstate = True
                    elif neighbours == 2 or neighbours == 3:
                        self._cells[i][j].nextstate = False
                    elif neighbours > 3:
                        self._cells[i][j].nextstate = True
                elif self._cells[i][j].dead and neighbours == 3:
                    self._cells[i][j].nextstate = False

        # Set cell state
        for i in range(len(self._cells)):
            for j in range(len(self._cells[0])):
                self._cells[i][j].setnextstate()

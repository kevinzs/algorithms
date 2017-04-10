from MazeGenerator.cell import Cell
from random import randint
from common.Queue import Queue


class Grid:
    def __init__(self, width, height, cellsize=15):
        self.width = width
        self.height = height
        self.start = False
        self.cellSize = cellsize
        self.visited = {}
        self.backtracked = {}
        self.track = Queue()
        self.frontier = Queue()
        self.cells = [[Cell() for i in range(int(self.width / self.cellSize))]
                      for j in range(int(self.height / self.cellSize) + self.cellSize)]
        for i in range(0, len(self.cells)):
            for j in range(0, len(self.cells[0])):
                self.cells[i][j] = Cell(i * self.cellSize, j * self.cellSize, cellsize)
        self.start_cell = self.cells[0][0]

    def in_bounds(self, cell):
        return 0 <= cell.x < self.width and 0 <= cell.y < self.height

    def neighbors(self, cell):
        results = []
        try:
            results.append(self.cells[int(cell.x / self.cellSize) + 2][int(cell.y / self.cellSize)])
            results.append(self.cells[int(cell.x / self.cellSize)][int(cell.y / self.cellSize) - 2])
            results.append(self.cells[int(cell.x / self.cellSize) - 2][int(cell.y / self.cellSize)])
            results.append(self.cells[int(cell.x / self.cellSize)][int(cell.y / self.cellSize) + 2])
        except IndexError:
            pass

        results = list(filter(self.in_bounds, results))
        return results

    def drawcells(self):
        for i in range(0, len(self.cells)):
            for j in range(0, len(self.cells[0])):
                self.cells[i][j].render()

    def maze_generator(self):
        if not self.start:
            self.start = True
            self.track.put(self.start_cell)
            self.visited[self.start_cell] = True
        else:
            if not self.track.empty():
                current = self.track.get()
                current.type = 2
                result = self.neighbors(current)
                if len(result) > 0:
                    loop = True
                    while loop:
                        next = result[randint(0, len(result) - 1)]
                        if next not in self.visited:
                            next.type = 2
                            self.visited[next] = True
                            if abs(current.x - next.x) == 0:
                                if current.y - next.y < 0:
                                    self.cells[int(current.x / self.cellSize)][int(current.y / self.cellSize) + 1].type = 2
                                else:
                                    self.cells[int(current.x / self.cellSize)][int(current.y / self.cellSize) - 1].type = 2
                            else:
                                if current.x - next.x < 0:
                                    self.cells[int(current.x / self.cellSize) + 1][int(current.y / self.cellSize)].type = 2
                                else:
                                    self.cells[int(current.x / self.cellSize) - 1][int(current.y / self.cellSize)].type = 2
                            self.track.put(next)
                            loop = False

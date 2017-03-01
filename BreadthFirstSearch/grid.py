from BreadthFirstSearch.cell import Cell
import pyglet

from common.Queue import Queue


class Grid:
    def __init__(self, width, height, cellsize=15):
        self.width = width
        self.height = height
        self.walls = []
        self.cellSize = cellsize
        self.start = Cell()
        self.frontier = Queue()
        self.visited = {}
        self.cells = [[Cell() for i in range(int(self.width / self.cellSize))]
                      for j in range(int(self.height / self.cellSize) + self.cellSize)]
        for i in range(0, len(self.cells)):
            for j in range(0, len(self.cells[0])):
                self.cells[i][j] = Cell(i * self.cellSize, j * self.cellSize, cellsize)

    def in_bounds(self, cell):
        return 0 <= cell.x < self.width and 0 <= cell.y < self.height

    def passable(self, cell):
        return cell not in self.walls

    def neighbors(self, cell):
        results = []
        try:
            results.append(self.cells[int(cell.x / self.cellSize) + 1][int(cell.y / self.cellSize)])
            results.append(self.cells[int(cell.x / self.cellSize)][int(cell.y / self.cellSize) - 1])
            results.append(self.cells[int(cell.x / self.cellSize) - 1][int(cell.y / self.cellSize)])
            results.append(self.cells[int(cell.x / self.cellSize)][int(cell.y / self.cellSize) + 1])
        except IndexError:
            pass

        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

    def drawcells(self):
        for i in range(0, len(self.cells)):
            for j in range(0, len(self.cells[0])):
                self.cells[i][j].render()

    def drawlines(self):
        pyglet.gl.glColor3f(100 / 255, 100 / 255, 100 / 255)
        for i in range(self.cellSize, self.width, self.cellSize):
            pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ("v2f", (0, i, self.width, i)))
            pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ("v2f", (i, 0, i, self.width)))

    def setstart(self, x, y):
        self.start.type = 1
        self.cells[int(x / self.cellSize)][int(y / self.cellSize)].type = 5
        self.start = self.cells[int(x / self.cellSize)][int(y / self.cellSize)]

    def setwall(self, x, y):
        self.cells[int(x / self.cellSize)][int(y / self.cellSize)].type = 2
        self.walls.append(self.cells[int(x / self.cellSize)][int(y / self.cellSize)])

    def setvisited(self, cell):
        self.cells[int(cell.x / self.cellSize)][int(cell.y / self.cellSize)].type = 3

    def setfrontier(self, cell):
        self.cells[int(cell.x / self.cellSize)][int(cell.y / self.cellSize)].type = 4

    def delete_grid(self):
        for i in range(0, len(self.cells)):
            for j in range(0, len(self.cells[0])):
                self.cells[i][j].type = 1
        self.walls = []

    def breadth_first_search1(self):
        self.frontier.put(self.start)
        self.visited[self.start] = True

    def breadth_first_search2(self):
        if not self.frontier.empty():
            current = self.frontier.get()
            if current != self.start:
                self.setvisited(current)
            for next in self.neighbors(current):
                if next not in self.visited:
                    self.frontier.put(next)
                    self.visited[next] = True
                    self.setfrontier(next)

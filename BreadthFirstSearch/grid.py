import pygame
from common.Queue import Queue
from BreadthFirstSearch.cell import Cell


class Grid:
    def __init__(self, width, height, cellsize=15):
        self.width = width
        self.height = height
        self.walls = []
        self.bfs = False
        self.finish = False
        self.cellSize = cellsize
        self.start = Cell()
        self.end = Cell()
        self.frontier = Queue()
        self.visited = {}
        self.came_from = {}
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

    def drawcells(self, screen):
        for i in range(0, len(self.cells)):
            for j in range(0, len(self.cells[0])):
                self.cells[i][j].render(screen)

    def drawlines(self, screen):
        for i in range(self.cellSize, self.width, self.cellSize):
            pygame.draw.line(screen, (200, 200, 200), (0, i), (self.width, i))
            pygame.draw.line(screen, (200, 200, 200), (i, 0), (i, self.width))

    def setstart(self, x, y):
        self.start.type = 1
        self.cells[int(x / self.cellSize)][int(y / self.cellSize)].type = 5
        self.start = self.cells[int(x / self.cellSize)][int(y / self.cellSize)]

    def setend(self, x, y):
        self.end.type = 1
        self.cells[int(x / self.cellSize)][int(y / self.cellSize)].type = 6
        self.end = self.cells[int(x / self.cellSize)][int(y / self.cellSize)]

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

    # Poner booleano de final para que no continue el bucle
    def breadth_first_search(self):
        if not self.bfs:
            self.frontier.put(self.start)
            self.visited[self.start] = True
            self.bfs = True
            self.came_from[self.start] = None
        else:
            if not self.frontier.empty() and not self.finish:
                current = self.frontier.get()
                if current != self.end:
                    if current != self.start:
                        self.setvisited(current)
                    for next in self.neighbors(current):
                        if next == self.end:
                            self.finish = True
                        if next not in self.visited:
                            self.frontier.put(next)
                            self.visited[next] = True
                            self.came_from[next] = current
                            self.setfrontier(next)
            else:
                self.end.type = 6
                current = self.came_from[self.end]
                while current != self.start:
                    current.type = 7
                    current = self.came_from[current]

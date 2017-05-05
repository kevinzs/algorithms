import sys, pygame
from pygame.locals import *
from MazeGenerator.grid import Grid

WIDTH = 640
HEIGHT = 480

grid = Grid(WIDTH, HEIGHT, 15)


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maze Generator")

    clock = pygame.time.Clock()
    while True:
        clock.tick(30)
        screen.fill((0, 0, 0))
        events()
        update(screen)
        pygame.display.update()
        pygame.display.flip()
    return 0


def update(screen):
    grid.drawcells(screen)
    grid.maze_generator()


def events():
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                grid.maze_generator()

if __name__ == '__main__':
    pygame.init()
    main()


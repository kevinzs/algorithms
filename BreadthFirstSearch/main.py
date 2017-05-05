import sys, pygame
from pygame.locals import *
from BreadthFirstSearch.grid import Grid

WIDTH = 640
HEIGHT = 480

start_BFS = False
grid = Grid(WIDTH, HEIGHT, 20)


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game Of Life")

    clock = pygame.time.Clock()
    while True:
        clock.tick(100)
        screen.fill((0, 0, 0))
        events()
        update(screen)
        pygame.display.update()
        pygame.display.flip()
    return 0


def update(screen):
    grid.drawcells(screen)
    grid.drawlines(screen)
    global start_BFS
    if start_BFS:
        grid.breadth_first_search()


def events():
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                global start_BFS
                start_BFS = True
            if event.key == pygame.K_d:
                grid.delete_grid()

    if pygame.mouse.get_pressed() == (1, 0, 0):
        pos = pygame.mouse.get_pos()
        grid.setwall(pos[0], pos[1])
    if pygame.mouse.get_pressed() == (0, 1, 0):
        pos = pygame.mouse.get_pos()
        grid.setend(pos[0], pos[1])
    if pygame.mouse.get_pressed() == (0, 0, 1):
        pos = pygame.mouse.get_pos()
        grid.setstart(pos[0], pos[1])

if __name__ == '__main__':
    pygame.init()
    main()
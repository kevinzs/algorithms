import sys, pygame
from pygame.locals import *
from GameOfLife.grid import Grid

WIDTH = 640
HEIGHT = 480

grid = Grid(WIDTH, HEIGHT)

pause = False


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game Of Life")

    clock = pygame.time.Clock()
    while True:
        if pause:
            clock.tick(60)
        else:
            clock.tick(15)
        screen.fill((0, 0, 0))
        events()
        update(screen)
        pygame.display.update()
        pygame.display.flip()
    return 0


def update(screen):
    grid.draw_cells(screen)
    if pause:
        label = font.render("PAUSE", 1, (255, 255, 255))
        screen.blit(label, (WIDTH/2.75, HEIGHT/2.5))
    else:
        grid.transition()


def events():
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                global pause
                pause = not pause
    if pygame.mouse.get_pressed() == (1, 0, 0):
        pos = pygame.mouse.get_pos()
        grid.setalivecell(pos[0], pos[1])

if __name__ == '__main__':
    pygame.init()
    font = pygame.font.SysFont("monospace", 50)
    main()
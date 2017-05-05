import math
import sys, pygame
from pygame.locals import *

WIDTH = 1280
HEIGHT = 480

padding = 100
lineLength = WIDTH - padding * 2
lines = [[padding, HEIGHT / 5, WIDTH - padding, HEIGHT / 5, 0]]


def update_frames(dt):
    pass


def kochCurve(lines):
    global lineLength
    lineLength = (lineLength / 3)

    nextLines = []
    for line in lines:
        nextLines.append([line[0],
                          line[1],
                          line[0] + lineLength * math.cos(math.radians(line[4])),
                          line[1] + math.sin(math.radians(line[4])) * lineLength,
                          line[4]])
        nextLines.append([line[0] + lineLength * math.cos(math.radians(line[4])),
                          line[1] + math.sin(math.radians(line[4])) * lineLength,
                          line[0] + lineLength * math.cos(math.radians(line[4])) + lineLength * math.cos(
                              math.radians((line[4] + 60) % 360)),
                          line[1] + math.sin(math.radians(line[4])) * lineLength + lineLength * math.sin(
                              math.radians((line[4] + 60) % 360)),
                          (line[4] + 60) % 360])
        nextLines.append([line[0] + lineLength * math.cos(math.radians(line[4])) + lineLength * math.cos(
                              math.radians((line[4] + 60) % 360)),
                          line[1] + math.sin(math.radians(line[4])) * lineLength + lineLength * math.sin(
                              math.radians((line[4] + 60) % 360)),
                          line[0] + 2 * lineLength * math.cos(math.radians(line[4])),
                          line[1] + math.sin(math.radians(line[4])) * lineLength + lineLength * math.sin(
                              math.radians((line[4]) % 360)),
                          (line[4] - 60) % 360])
        nextLines.append([line[0] + 2 * lineLength * math.cos(math.radians(line[4])),
                          line[1] + math.sin(math.radians(line[4])) * lineLength + lineLength * math.sin(
                              math.radians((line[4]) % 360)),
                          line[2],
                          line[1] + math.sin(math.radians(line[4])) * lineLength + 2 * lineLength * math.sin(
                              math.radians((line[4]) % 360)),
                          line[4]])

    return nextLines


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Koch Curve")

    clock = pygame.time.Clock()
    while True:
        clock.tick(30)
        screen.fill((0, 0, 0))
        events()
        update(screen)
        pygame.display.update()
    return 0


def update(screen):
    global lines
    for line in lines:
        pygame.draw.line(screen, (255, 255, 255), (line[0], line[1]), (line[2], line[3]))


def events():
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                global lines
                lines = kochCurve(lines)

if __name__ == '__main__':
    pygame.init()
    font = pygame.font.SysFont("monospace", 50)
    main()




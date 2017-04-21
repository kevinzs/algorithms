import math
import pyglet
from pyglet.window import key

width = 1280
height = 480
window = pyglet.window.Window(width, height)
window.set_location(250, 250)

counter = .0
fps = 1 / 1.0

padding = 100
lineLength = width - padding * 2
lines = [[padding, height / 5, width - padding, height / 5, 0]]


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


@window.event
def on_draw():
    window.clear()
    pyglet.gl.glColor3f(255 / 255, 255 / 255, 255 / 255)
    global lines
    for line in lines:
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ("v2f", (line[0], line[1], line[2], line[3])))
    lines = kochCurve(lines)


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.SPACE:
        global lines
        lines = kochCurve(lines)


pyglet.clock.schedule_interval(update_frames, fps)
pyglet.app.run()

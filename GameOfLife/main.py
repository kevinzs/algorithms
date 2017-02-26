import pyglet
from pyglet.window import key
from GameOfLife.grid import Grid

window = pyglet.window.Window(640, 480)
window.set_location(500, 250)

counter = .0
fps = 1 / 5.0
window_width, window_height = window.get_size()
grid = Grid(window_width, window_height)
pause = False


def update_frames(dt):
    global counter
    counter = (counter + dt) % 2


@window.event
def on_draw():
    window.clear()
    if not pause:
        grid.transition()
    grid.draw_cells()


@window.event
def on_mouse_press(x, y, button, modifiers):
    grid.setalivecell(x, y)


@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    grid.setalivecell(x, y)


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.SPACE:
        global pause
        pause = not pause


pyglet.clock.schedule_interval(update_frames, fps)
pyglet.app.run()

import pyglet
from pyglet.window import key, mouse
from BreadthFirstSearch.grid import Grid

window = pyglet.window.Window(640, 480)
window.set_location(500, 250)

counter = .0
fps = 1 / 2.0
window_width, window_height = window.get_size()
grid = Grid(window_width, window_height, 20)


def update_frames(dt):
    global counter
    counter = (counter + dt) % 2


@window.event
def on_draw():
    window.clear()
    grid.drawcells()
    grid.drawlines()


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        grid.setwall(x, y)
    elif button == mouse.RIGHT:
        grid.setstart(x, y)


@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    if buttons == mouse.LEFT:
        grid.setwall(x, y)


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.D:
        grid.delete_grid()
    elif symbol == key.SPACE:
        grid.breadth_first_search1()
    elif symbol == key.N:
        grid.breadth_first_search2()


pyglet.clock.schedule_interval(update_frames, fps)
pyglet.app.run()

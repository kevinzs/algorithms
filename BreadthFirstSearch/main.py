import pyglet
from pyglet.window import key, mouse
from BreadthFirstSearch.grid import Grid

window = pyglet.window.Window(640, 480)
keys = key.KeyStateHandler()
window.push_handlers(keys)
window.set_location(500, 250)


counter = .0
fps = 1 / 30.0
window_width, window_height = window.get_size()
grid = Grid(window_width, window_height, 20)


def update_frames(dt):
    global counter
    counter = (counter + dt) % 2

@window.event
def on_draw():
    handle_keyboard()
    window.clear()
    grid.drawcells()
    grid.drawlines()


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        grid.setwall(x, y)
    elif button == mouse.RIGHT:
        grid.setstart(x, y)
    elif button == mouse.MIDDLE:
        grid.setend(x, y)


@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    if buttons == mouse.LEFT:
        grid.setwall(x, y)

def handle_keyboard():
    if keys[key.D]:
        grid.delete_grid()
    if keys[key.SPACE]:
        grid.breadth_first_search()

pyglet.clock.schedule_interval(update_frames, fps)
pyglet.app.run()

import pyglet
from MazeGenerator.grid import Grid
from pyglet.window import mouse

window = pyglet.window.Window(640, 480)
window.set_location(500, 250)

counter = .0
fps = 1 / 200.0
start_BFS = False
window_width, window_height = window.get_size()
grid = Grid(window_width, window_height, 15)


def update_frames(dt):
    global counter
    counter = (counter + dt) % 2


@window.event
def on_draw():
    window.clear()
    grid.drawcells()
    grid.maze_generator()

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        grid.maze_generator()


pyglet.clock.schedule_interval(update_frames, fps)
pyglet.app.run()

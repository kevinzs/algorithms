import pyglet
from pyglet.window import mouse

width = 1280
height = 480
window = pyglet.window.Window(width, height)
window.set_location(250, 250)

counter = .0
fps = 1 / 200.0


def update_frames(dt):
    pass


def kochCurve():
    pyglet.gl.glColor3f(200 / 255, 200 / 255, 200 / 255)
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ("v2f", (100, height/5, width - 100, height/5)))


@window.event
def on_draw():
    window.clear()
    kochCurve()


pyglet.clock.schedule_interval(update_frames, fps)
pyglet.app.run()

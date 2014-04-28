import pyglet


class Game(object):
    """Controls the game window"""
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.window = pyglet.window.Window()

    def run(self):
        pyglet.app.run()

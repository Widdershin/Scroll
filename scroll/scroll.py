import pyglet


class Game(object):
    """Controls the game window"""
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.window = pyglet.window.Window()

    def run(self):
        pyglet.app.run()


class Floor(object):
    """A floor of the dungeon"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.characters = []
        self.terrain = [[None for i in range(width)] for j in range(height)]
        self.room = [[None for i in range(width)] for j in range(height)]

    def add_character(self, character, position):
        character.position = position
        self.characters.append(character)
        self.room[position.x][position.y] = character

    def generate(self):
        pass


class EmptyFloor(Floor):
    def __init__(self, width, height):
        super(EmptyFloor, self).__init__(width, height)

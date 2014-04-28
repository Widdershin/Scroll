import scroll

game = scroll.Game()


class Rogue(scroll.Character):
    """Our main character"""

    char = "@"
    sprite = "rogue.png"

    def __init__(self, position):
        super(Rogue, self).__init__()

if __name__ == '__main__':
    start_floor = scroll.EmptyFloor(64, 64)
    rogue = Rogue()
    game.run(start_floor)

import sys
sys.path.append("..\scroll")

import scroll

game = scroll.Scroll(resolution=(640, 480))


class Character(scroll.Entity):
    def __init__(self, position):
        super().__init__()
        self.sprite_path = r'C:\Projects\Scroll\rogue\sprites\test.png'
        self.add_component(scroll.component.Position(position))
        self.add_component(scroll.component.Sprite(self.sprite_path))


def main():
    char = Character(scroll.helpers.Vector2(100, 100))
    char.draw()
    game.run()


if __name__ == '__main__':
    main()

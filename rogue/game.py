import sys
sys.path.append("..\scroll")

import scroll

game = scroll.Scroll(resolution=(640, 480))


def main():
    game.run()


if __name__ == '__main__':
    main()

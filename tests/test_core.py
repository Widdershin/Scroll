import unittest
import unittest.mock

import pyglet
import scroll


class TestGame(unittest.TestCase):
    def test_can_run(self):
        pyglet.app.run = unittest.mock.MagicMock()
        game = scroll.Game()
        game.run()

        pyglet.app.run.assert_called_once_with()

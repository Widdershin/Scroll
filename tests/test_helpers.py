import scroll
import unittest

Position = scroll.Position


class TestPosition(unittest.TestCase):
    def test_tuple_equality(self):
        self.assertEqual(Position(23, -6), (23, -6))

    def test_position_addition(self):
        a = Position(5, 10)
        b = Position(3, 4)

        c = a + b

        self.assertEqual(c, (8, 14))

    def test_position_multiplication(self):
        a = Position(15, 3)
        b = Position(2, 3)

        c = a * b

        self.assertEqual(c, (30, 9))

    def test_multiplication(self):
        a = Position(2, 8.5)
        b = a * 2

        self.assertEqual(b, (4, 17))

    def test_division(self):
        a = Position(50, 44)

        b = a / 2

        self.assertEqual(b, (25, 22))

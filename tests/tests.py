import sys
sys.path.append("..\scroll")

import unittest

from scroll.helpers import Vector2


class TestVector2(unittest.TestCase):

    def test_addition(self):
        a = Vector2(15, 10)
        b = Vector2(10, 30)

        self.assertEqual(a + b, Vector2(25, 40))

    def test_equality(self):
        a = Vector2(10, 10)
        b = Vector2(10, 15)
        c = Vector2(10, 10)

        self.assertEqual(a, c)
        self.assertNotEqual(a, b)

    def test_vector_multiplication(self):
        a = Vector2(2, 3)
        b = Vector2(2, 1)

        self.assertEqual(a * b, Vector2(4, 3))

    def test_raw_multiplication(self):
        a = Vector2(3, 4)

        self.assertEqual(a * 3, Vector2(9, 12))

    def test_subtraction(self):
        a = Vector2(10, 10)
        b = Vector2(3, 2)

        self.assertEqual(a - b, Vector2(7, 8))

    def test_vector_division(self):
        a = Vector2(10, 6)
        b = Vector2(2, 3)

        self.assertEqual(a / b, Vector2(5, 2))

    def test_raw_division(self):
        a = Vector2(10, 6)

        self.assertEqual(a / 2, Vector2(5, 3))

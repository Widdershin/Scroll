import operator


class Position(tuple):
    """A position in the dungeon"""

    def __new__(cls, x, y):
        return super().__new__(cls, (x, y))

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self._operator_on_other(other, operator.add)

    def __mul__(self, other):
        return self._operator_on_other(other, operator.mul)

    def __sub__(self, other):
        return self._operator_on_other(other, operator.sub)

    def __truediv__(self, other):
        return self._operator_on_other(other, operator.truediv)

    def _operator_on_other(self, other, operator):
        try:
            return Position(operator(self.x, other[0]),
                            operator(self.y, other[1]))
        except TypeError:
            return Position(operator(self.x, other),
                            operator(self.y, other))

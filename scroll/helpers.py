
class Vector2(tuple):
    def __new__(cls, x, y):
        return super().__new__(cls, (x, y))

    def __add__(self, other):
        return Vector2(*map(sum, zip(self, other)))

    def __mul__(self, other):
        if isinstance(other, tuple):
            return Vector2(*map(lambda x: x[0] * x[1], zip(self, other)))
        else:
            return Vector2(*map(lambda x: x * other, self))

    def __sub__(self, other):
        return Vector2(*map(lambda x: x[0] - x[1], zip(self, other)))

    def __truediv__(self, other):
        if isinstance(other, tuple):
            return Vector2(*map(lambda x: x[0] / x[1], zip(self, other)))
        else:
            return Vector2(*map(lambda x: x / other, self))

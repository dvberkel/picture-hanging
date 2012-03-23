import string

from picture.group.element import Element

class Solver:
    def __init__(self):
        self.index = -1

    def solve(self, n):
        if (n == 1):
            self.index += 1
            return Element.word(string.letters[self.index])
        else:
            floor = n / 2
            ceil = n - floor

            a = self.solve(ceil)
            b = self.solve(floor)
            return a * b.inverse() * a.inverse() * b

import unittest

from picture.solver import Solver
from picture.group.element import Element

class testSolver(unittest.TestCase):
    def testSolution(self):
        for n in range(1,2):
            word = Solver().solve(n)
            
            letterCount = 0
            for letter in word.letters():
                letterCount += 1
                self.assertEquals(Element.word(""), word.remove(letter))
            self.assertEquals(n, letterCount)

if __name__ == '__main__':
    unittest.main()

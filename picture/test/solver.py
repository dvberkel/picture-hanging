import unittest

from picture.solver import Solver
from picture.group.element import Element

class testSolver(unittest.TestCase):
    def testSolution(self):
        word = Solver().solve(1)
        
        for letter in word.letters():
            self.assertEquals(Element.word(""), word.remove(letter))

        

if __name__ == '__main__':
    unittest.main()

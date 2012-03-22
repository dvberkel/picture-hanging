import unittest

from picture.group.test.freegroup import testFreeGroup
from picture.group.test.element import testElement
from picture.group.test.wordparser import testWordParser
from picture.group.test.formatter import testFormatter
from picture.group.test.normalizer import testNormalizer
from picture.test.solver import testSolver

class EvaluateSuite(unittest.TestSuite):
    def __init__(self):
        unittest.TestSuite.__init__(self)
        for clazz in [testFreeGroup, testElement, testWordParser, testFormatter, testNormalizer, testSolver]:
            self.addTest(unittest.makeSuite(clazz))

if __name__ == '__main__':
    suite = EvaluateSuite()

    unittest.TextTestRunner().run(suite)

import unittest

from picture.group.normalizer import Normalizer

class testNormalizer(unittest.TestCase):
    def testNormalisationOfFactors(self):
        self.assertEquals([('a', 1)], Normalizer.of([('a', 1)]).normalize())
        self.assertEquals([('b', -1)], Normalizer.of([('b', -1)]).normalize())
        self.assertEquals([], Normalizer.of([('a', 1), ('a', -1)]).normalize())
        self.assertEquals([], Normalizer.of([('b', -1), ('a', 1), ('a', -1), ('b', 1)]).normalize())


if __name__ == '__main__':
    unittest.main()

import unittest

from picture.group.formatter import FactorsFormatter

class testFormatter(unittest.TestCase):
    def testFormattingOfFactors(self):
        self.assertEquals("", str(FactorsFormatter([('a', 0)])))
        self.assertEquals("a", str(FactorsFormatter([('a', 1)])))
        self.assertEquals("a^2", str(FactorsFormatter([('a', 2)])))
        self.assertEquals("a^-1", str(FactorsFormatter([('a', -1)])))
        self.assertEquals("ab", str(FactorsFormatter([('a', 1), ('b', 1)])))

if __name__ == '__main__':
    unittest.main()

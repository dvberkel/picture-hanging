import unittest

from picture.group.wordparser import WordParser

class testWordParser(unittest.TestCase):
    def testWordParserFactors(self):
        self.assertEquals([('a', 1)], WordParser("a").factors())
        self.assertEquals([('b', 1)], WordParser("b").factors())

if __name__ == '__main__':
    unittest.main()

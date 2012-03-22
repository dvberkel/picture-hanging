import unittest

from picture.group.wordparser import WordParser, ParseError

class testWordParser(unittest.TestCase):
    def testWordParserFactors(self):
        self.assertEquals([('a', 1)], WordParser("a").factors())
        self.assertEquals([('b', 1)], WordParser("b").factors())
        self.assertEquals([('a', 1)], WordParser("a^1").factors())
        self.assertEquals([('b', 1)], WordParser("b^1").factors())
        self.assertEquals([('a', 2)], WordParser("a^2").factors())
        self.assertEquals([('b', 2)], WordParser("b^2").factors())
        
    def testExceptionsThrown(self):
        self.assertRaises(ParseError, WordParser("^").factors)

if __name__ == '__main__':
    unittest.main()

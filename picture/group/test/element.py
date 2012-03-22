import unittest

from picture.group.element import Element

class testElement(unittest.TestCase):
    def testCreationOfElement(self):
        self.assertNotEqual(None, Element.word("a"))

    def testMultiplicationOfElements(self):
        a = Element.word("a");
        b = Element.word("b");

        actual = a * b

        self.assertEquals(Element.word("ab"), actual)

if __name__ == '__main__':
    unittest.main()

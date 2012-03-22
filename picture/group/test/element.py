import unittest

from picture.group.element import Element

class testElement(unittest.TestCase):
    def testCreationOfElement(self):
        self.assertNotEqual(None, Element("a"))

if __name__ == '__main__':
    unittest.main()

import unittest

from picture.group.freegroup import FreeGroup
from picture.group.element import Element

class testFreeGroup(unittest.TestCase):
    def setUp(self):
        self.group = FreeGroup.over("a", "b")
        
    def testCreationOfAFreeGroup(self):
        self.assertNotEqual(None, self.group)
    
    def testNumberOfGenerators(self):
        self.assertEqual(2, len(self.group))

    def testGeneratorAccess(self):
        self.assertEquals(Element.word("a"), self.group[0])
        self.assertEquals(Element.word("b"), self.group[1])

if __name__ == '__main__':
    unittest.main()

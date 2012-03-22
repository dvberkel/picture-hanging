import unittest

from picture.group.freegroup import FreeGroup

class testFreeGroup(unittest.TestCase):
    def setUp(self):
        self.group = FreeGroup.over("a", "b")
        
    def testCreationOfAFreeGroup(self):
        self.assertNotEqual(None, self.group)

if __name__ == '__main__':
    unittest.main()

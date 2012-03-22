import unittest

from picture.group.freegroup import FreeGroup

class testFreeGroup(unittest.TestCase):
    def testCreateOfAFreeGroup(self):
        group = FreeGroup.over("a", "b")

        self.assertNotEqual(None, group)

if __name__ == '__main__':
    unittest.main()

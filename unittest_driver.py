import unittest
from Game import PC

class TestGame(unittest.TestCase):
    def test_PC(self):
        mypc = PC.PC('mike',1)
        self.assertTrue(mypc != None)


if __name__ == '__main__':
    unittest.main()

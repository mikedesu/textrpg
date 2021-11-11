#!/usr/bin/python3
import unittest
from Game import PC
from Game.PC import ZeroLevelException
from Game.PC import NegativeLevelException 
from Game.PC import NegativeAttributeException  
from Game.Race import Race
from Game.Job import Job
from random import randint

class TestGame(unittest.TestCase):
    def test_PC_creation_basic(self):
        a = []
        for i in range(6):
            a.append(randint(3,18))
        mypc = PC.PC('mike', 1, Race.HUMAN, Job.FIGHTER, a)
        self.assertTrue(mypc != None)
        self.assertTrue(mypc.name == 'mike')
        self.assertTrue(mypc.level == 1)
        self.assertTrue(mypc.race == Race.HUMAN)
        self.assertTrue(mypc.job == Job.FIGHTER)

    def test_PC_creation_basic_fail_attributes(self):
        a = []
        for i in range(6):
            a.append(randint(-18,-3))
        try:
            mypc = PC.PC('mike', 1, Race.HUMAN, Job.FIGHTER, a)
        except NegativeAttributeException:
            self.assertTrue(True)

    def test_PC_creation_basic_fail_level(self):
        a = []
        for i in range(6):
            a.append(randint(3,18))
        try:
            mypc = PC.PC('mike', randint(-100,0), Race.HUMAN, Job.FIGHTER, a)
        except ZeroLevelException:
            self.assertTrue(True)
        except NegativeLevelException:
            self.assertTrue(True)





if __name__ == '__main__':
    unittest.main()

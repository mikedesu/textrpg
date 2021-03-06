#!/usr/bin/python3
import unittest
import Game
from Game import Entity
from Game.Entity import ZeroLevelException
from Game.Entity import NegativeLevelException 
from Game.Entity import NegativeAttributeException  
from Game.Race import Race
from Game.Job import Job
from Game.Renderer import Renderer 
from random import randint

class TestGame(unittest.TestCase):

    def test_basic(self):
        self.assertTrue(True)

    #def test_Renderer_creation(self):
        #r = Renderer()

    #def test_Game_creation(self):
        #screen = None
        #myGame = Game.Game()
        #self.assertTrue(myGame != None)


    #def test_NPC_creation_basic(self):
    #    a = []
    #    for i in range(6):
    #        a.append(randint(3,18))
    #    mypc = NPC.NPC('mike', 1, Race.HUMAN, Job.FIGHTER, a)
    #    self.assertTrue(mypc != None)
    #    self.assertTrue(mypc.name == 'mike')
    #    self.assertTrue(mypc.level == 1)
    #    self.assertTrue(mypc.race == Race.HUMAN)
    #    self.assertTrue(mypc.job == Job.FIGHTER)

    #def test_NPC_creation_basic_fail_attributes(self):
    #    a = []
    #    for i in range(6):
    #        a.append(randint(-18,-3))
    #    try:
    #        mypc = NPC.NPC('mike', 1, Race.HUMAN, Job.FIGHTER, a)
    #    except NegativeAttributeException:
    #        self.assertTrue(True)

    #def test_NPC_creation_basic_fail_level(self):
    #    a = []
    #    for i in range(6):
    #        a.append(randint(3,18))
    #    try:
    #        mypc = NPC.NPC('mike', randint(-100,0), Race.HUMAN, Job.FIGHTER, a)
    #    except ZeroLevelException:
    #        self.assertTrue(True)
    #    except NegativeLevelException:
    #        self.assertTrue(True)





if __name__ == '__main__':
    unittest.main()

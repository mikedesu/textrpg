
from random import randint

class NameGenerator:
    def __init__(self):
        pass
            
    def generateName(self):
        alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        randomLenMin = 3
        randomLenMax = 20
        randomLen = randint(randomLenMin, randomLenMax)
        randomName = ""
        for j in range(randomLen):
            randomName += alphabet[ randint(0, len(alphabet)-1) ]
        return randomName 


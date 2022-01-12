
from random import randint

class NameGenerator:
    def __init__(self):
        pass
            
    def generateName(self):
        #return "ralph"
        #alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        #randomLenMin = 3
        #randomLenMax = 20
        #randomLen = randint(randomLenMin, randomLenMax)
        #randomName = ""
        #for j in range(randomLen):
        #    randomName += alphabet[ randint(0, len(alphabet)-1) ]

        prefixes = [
            'Bro',
            'Dro',
            'Do',
            'Fro',
            'Go',
            'Gro',
            'Glo',
            'Gno',
            'Ho',
            'Jo',
            'Ko',
            'Kro',
            'Lo',
            'Mo',
            'No',
            'Po',
            'Quo',
            'Ro',
            'So',
            'Sto',
            'To',
            'Vo',
            'Wo',
            'Xo',
            'Yo',
            'Zo'
        ]

        suffixes = [
            'bin',
            'din',
            'fin',
            'gin',
            'hin',
            'jin',
            'kin',
            'lin',
            'min',
            'nin',
            'pin',
            'rin',
            'sin',
            'tin',
            'vin',
            'win',
            'xin',
            'yin',
            'zin'
        ]

        name = prefixes[ randint( 0, len(prefixes)-1 ) ] + suffixes[ randint( 0, len(suffixes)-1 ) ] 
        return  name


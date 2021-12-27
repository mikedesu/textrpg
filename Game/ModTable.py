class ModTable:
    @staticmethod
    def getModForScore(score):
        table = {
            1 : [ -5, None, None, None, None, None, None, None, None, None, None],
            2 : [ -4, None, None, None, None, None, None, None, None, None, None],
            3 : [ -4, None, None, None, None, None, None, None, None, None, None],
            4 : [ -3, None, None, None, None, None, None, None, None, None, None],
            5 : [ -3, None, None, None, None, None, None, None, None, None, None],
            6 : [ -2, None, None, None, None, None, None, None, None, None, None],
            7 : [ -2, None, None, None, None, None, None, None, None, None, None],
            8 : [ -1, None, None, None, None, None, None, None, None, None, None],
            9 : [ -1, None, None, None, None, None, None, None, None, None, None],
           10 : [  0, None, None, None, None, None, None, None, None, None, None],
           11 : [  0, None, None, None, None, None, None, None, None, None, None],
           12 : [  1, None, 1, None, None, None, None, None, None, None, None],
           13 : [  1, None, 1, None, None, None, None, None, None, None, None],
           14 : [  2, None, 1, 1, None, None, None, None, None, None, None],
           15 : [  2, None, 1, 1, None, None, None, None, None, None, None],
           16 : [  3, None, 1, 1, 1, None, None, None, None, None, None],
           17 : [  3, None, 1, 1, 1, None, None, None, None, None, None],
           18 : [  4, None, 1, 1, 1, 1, None, None, None, None, None],
           19 : [  4, None, 1, 1, 1, 1, None, None, None, None, None],
           20 : [  5, None, 2, 1, 1, 1, 1, None, None, None, None]
        }
        return table[score][0]

    @staticmethod
    def getBonusSpells(self,score,level):
        table = {
            1 : [ -5, None, None, None, None, None, None, None, None, None, None],
            2 : [ -4, None, None, None, None, None, None, None, None, None, None],
            3 : [ -4, None, None, None, None, None, None, None, None, None, None],
            4 : [ -3, None, None, None, None, None, None, None, None, None, None],
            5 : [ -3, None, None, None, None, None, None, None, None, None, None],
            6 : [ -2, None, None, None, None, None, None, None, None, None, None],
            7 : [ -2, None, None, None, None, None, None, None, None, None, None],
            8 : [ -1, None, None, None, None, None, None, None, None, None, None],
            9 : [ -1, None, None, None, None, None, None, None, None, None, None],
           10 : [  0, None, None, None, None, None, None, None, None, None, None],
           11 : [  0, None, None, None, None, None, None, None, None, None, None],
           12 : [  1, None, 1, None, None, None, None, None, None, None, None],
           13 : [  1, None, 1, None, None, None, None, None, None, None, None],
           14 : [  2, None, 1, 1, None, None, None, None, None, None, None],
           15 : [  2, None, 1, 1, None, None, None, None, None, None, None],
           16 : [  3, None, 1, 1, 1, None, None, None, None, None, None],
           17 : [  3, None, 1, 1, 1, None, None, None, None, None, None],
           18 : [  4, None, 1, 1, 1, 1, None, None, None, None, None],
           19 : [  4, None, 1, 1, 1, 1, None, None, None, None, None],
           20 : [  5, None, 2, 1, 1, 1, 1, None, None, None, None]
        }
        return table[score][level+2]
            

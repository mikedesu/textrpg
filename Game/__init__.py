from . import DungeonFloor 

class Game:
    def __init__(self, title='my game', renderer=None):
        self.title = title
        self.logs = []
        self.currentTurnCount = 0
        assert(renderer != None)
        self.renderer = renderer
        #rows, cols = self.renderer.s.getmaxyx()
        rows = 10
        cols = 10
        #rows -= 4
        #cols -= 2
        self.dungeonFloor = DungeonFloor.DungeonFloor(self, rows, cols)

    def __str__(self):
        return self.title

    def addLog(self,log):
        if log==None or log=="":
            raise Exception("Log is empty or none")
        self.logs.append(log)

    def incrTurns(self):
        self.currentTurnCount += 1
    

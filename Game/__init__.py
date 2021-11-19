
class Game:
    def __init__(self, title='my game'):
        self.title = title
        self.logs = []
    def __str__(self):
        return self.title

    def addLog(self,log):
        if log==None or log=="":
            raise Exception("Log is empty or none")
        self.logs.append(log)

    

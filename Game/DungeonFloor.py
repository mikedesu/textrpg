class DungeonFloor:
    def __init__(self, rows, cols):
        # SUPER-basic beginning example
        self.map_ = []
        for i in range(rows):
            self.map_.append("#"*cols)


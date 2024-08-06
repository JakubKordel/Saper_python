class Spot():
    def __init__(self):
        self.setType()
        self.setVisibility()
        self.setBombsAround()

    def setType(self, t = 'VALUE' ):
        self.type = t

    def setVisibility(self, vis = 'HIDDEN' ):
        self.visibility = vis

    def setBombsAround(self, num = 0):
        self.bombs = num

    def getType(self):
        return self.type

    def getVisibility(self):
        return self.visibility

    def getBombsAround(self):
        return self.bombs

class Pointer():
    def __init__(self, widthX, heightY):
        self.width = widthX
        self.height = heightY
        self.x = 0
        self.y = 0


    def left(self):
        if self.x > 0:
            self.x = self.x - 1
        else:
            self.x = self.width - 1

    def right(self):
        if self.x < self.width - 1:
            self.x = self.x + 1
        else:
            self.x = 0


    def up(self):
        if self.y < self.height - 1:
            self.y = self.y + 1
        else:
            self.y = 0

    def down(self):
        if self.y > 0:
            self.y = self.y - 1
        else:
            self.y = self.height - 1

    def getX(self):
        return self.x

    def getY(self):
        return self.y

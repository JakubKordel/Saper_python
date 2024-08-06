class Settings():
    def __init__(self, pWidth, pHeight, pRisk, pGameType, pSetValue):
        self.pWidth = pWidth
        self.pHeight = pHeight
        self.pRisk = pRisk
        self.pGameType = pGameType
        self.pSetValue = pSetValue
        self.width = 5
        self.height = 5
        self.risk = 10
        self.gameType = 'NORMAL'

    def set(self, a):
        if self.pSetValue.getY() == 3:
            if a == 'a':
                self.pWidth.left()
            elif a == 'd':
                self.pWidth.right()
            self.width = 5 + self.pWidth.getX()
        elif self.pSetValue.getY() == 2:
            if a == 'a':
                self.pHeight.left()
            elif a == 'd':
                self.pHeight.right()
            self.height = 5 + self.pHeight.getX()
        elif self.pSetValue.getY() == 1:
            if a == 'a':
                self.pRisk.left()
            elif a == 'd':
                self.pRisk.right()
            self.risk = 10 + self.pRisk.getX()/5
        elif self.pSetValue.getY() == 0 and (a == 'a' or a == 'd'):
            if a == 'a':
                self.pGameType.left()
            else:
                self.pGameType.right()
            if self.pGameType.getX() == 0:
                self.gameType = 'NORMAL'
            elif self.pGameType.getX() == 1:
                self.gameType = 'AI'
            elif self.pGameType.getX() == 2:
                self.gameType = 'AITEST'

        if a == 's':
            self.pSetValue.down()
        elif a == 'w':
            self.pSetValue.up()

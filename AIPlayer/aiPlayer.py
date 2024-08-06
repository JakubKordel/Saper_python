import random

class AIPlayer():

    def __init__(self, engine):
        self.engine = engine

    def move(self):
        if not self.findFree() and not self.findBomb():
            self.shoot()

    def findBomb(self):
        f = False
        for i in range(0, self.engine.height()):
            for j in range(0, self.engine.width()):
                if self.engine.visibility(j, i) == 'VISIBLE' and self.countHidden(j, i) and self.engine.value(j, i) == self.countHidden(j, i) + self.countFlags(j, i):
                    self.setFlag(j, i)
                    f = True
                    break
            if f:
                break
        return f

    def findFree(self):
        f = False
        for i in range(0, self.engine.height()):
            for j in range(0, self.engine.width()):
                if self.engine.visibility(j, i) == 'VISIBLE' and self.countFlags(j, i) == self.engine.value(j, i) and self.countHidden(j, i):
                    self.unhide(j, i)
                    f = True
                    break
            if f:
                break
        return f

    def shoot(self):
        places = 0
        for i in range(0, self.engine.height()):
            for j in range(0, self.engine.width()):
                if self.engine.visibility(j, i) == 'HIDDEN':
                    places = places + 1

        randomNum = random.randint(1, places)
        for i in range(0, self.engine.height()):
            for j in range(0, self.engine.width()):
                if self.engine.visibility(j, i) == 'HIDDEN':
                    randomNum = randomNum - 1
                    if randomNum == 0:
                        self.engine.unhide(j, i)
                        break
            if randomNum == 0:
                break

    def unhide(self, x, y):
        up = False
        down = False
        left = False
        right = False
        if x > 0:
            left = True
        if x + 1 < self.engine.width():
            right = True
        if y > 0:
            down = True
        if y + 1 < self.engine.height():
            up = True
        if up and left and self.engine.visibility( x - 1, y + 1) == 'HIDDEN':
            self.engine.unhide( x - 1, y + 1)
        elif up and self.engine.visibility( x , y + 1 ) == 'HIDDEN':
            self.engine.unhide( x , y + 1 )
        elif up and right and self.engine.visibility( x + 1, y + 1 ) == 'HIDDEN':
            self.engine.unhide( x + 1, y + 1 )
        elif right and self.engine.visibility( x + 1, y  ) == 'HIDDEN':
            self.engine.unhide( x + 1, y )
        elif down and right and self.engine.visibility( x + 1, y - 1 ) == 'HIDDEN':
            self.engine.unhide( x + 1, y - 1 )
        elif down and self.engine.visibility( x , y - 1 ) == 'HIDDEN':
            self.engine.unhide( x , y - 1 )
        elif down and left and self.engine.visibility( x - 1, y - 1 ) == 'HIDDEN':
            self.engine.unhide( x - 1, y - 1 )
        elif left and self.engine.visibility( x - 1, y ) == 'HIDDEN':
            self.engine.unhide( x - 1, y )

    def setFlag(self, x, y):
        up = False
        down = False
        left = False
        right = False
        if x > 0:
            left = True
        if x + 1 < self.engine.width():
            right = True
        if y > 0:
            down = True
        if y + 1 < self.engine.height():
            up = True
        if up and left and self.engine.visibility(x - 1, y + 1) == 'HIDDEN':
            self.engine.switchSymbol(x - 1, y + 1)
        elif up and self.engine.visibility(x , y + 1) == 'HIDDEN':
            self.engine.switchSymbol(x , y + 1)
        elif up and right and self.engine.visibility( x + 1, y + 1) == 'HIDDEN':
            self.engine.switchSymbol(x + 1, y + 1)
        elif right and self.engine.visibility( x + 1, y) == 'HIDDEN':
            self.engine.switchSymbol(x + 1, y)
        elif down and right  and self.engine.visibility( x + 1, y - 1) == 'HIDDEN':
            self.engine.switchSymbol(x + 1, y - 1)
        elif down and self.engine.visibility( x , y - 1) == 'HIDDEN':
            self.engine.switchSymbol(x , y - 1)
        elif down and left and self.engine.visibility( x - 1, y - 1) == 'HIDDEN':
            self.engine.switchSymbol(x - 1, y - 1)
        elif left and self.engine.visibility( x - 1, y) == 'HIDDEN':
            self.engine.switchSymbol(x - 1, y)

    def countFlags(self, x, y):
        counter = 0
        up = False
        down = False
        left = False
        right = False
        if x > 0:
            left = True
        if x + 1 < self.engine.width():
            right = True
        if y > 0:
            down = True
        if y + 1 < self.engine.height():
            up = True
        if up and left and self.engine.visibility(x - 1, y + 1) == 'FLAG':
            counter = counter + 1
        if up and self.engine.visibility(x, y + 1) == 'FLAG':
            counter = counter + 1
        if up and right and self.engine.visibility(x + 1, y + 1) == 'FLAG':
            counter = counter + 1
        if right and self.engine.visibility(x + 1, y) == 'FLAG':
            counter = counter + 1
        if down and right and self.engine.visibility(x + 1, y - 1) == 'FLAG':
            counter = counter + 1
        if down and self.engine.visibility(x, y - 1) == 'FLAG':
            counter = counter + 1
        if down and left and self.engine.visibility(x - 1, y - 1) == 'FLAG':
            counter = counter + 1
        if left and self.engine.visibility(x - 1, y) == 'FLAG':
            counter = counter + 1
        return counter

    def countHidden(self, x, y):
        counter = 0
        up = False
        down = False
        left = False
        right = False
        if x > 0:
            left = True
        if x + 1 < self.engine.width():
            right = True
        if y > 0:
            down = True
        if y + 1 < self.engine.height():
            up = True
        if up and left and self.engine.visibility(x - 1, y + 1) == 'HIDDEN':
            counter = counter + 1
        if up and self.engine.visibility(x , y + 1) == 'HIDDEN':
            counter = counter + 1
        if up and right and self.engine.visibility(x + 1, y + 1) == 'HIDDEN':
            counter = counter + 1
        if right and self.engine.visibility(x + 1, y) == 'HIDDEN':
            counter = counter + 1
        if down and right and self.engine.visibility(x + 1, y - 1) == 'HIDDEN':
            counter = counter + 1
        if down and self.engine.visibility(x , y - 1) == 'HIDDEN':
            counter = counter + 1
        if down and left and self.engine.visibility(x - 1, y - 1) == 'HIDDEN':
            counter = counter + 1
        if left and self.engine.visibility(x - 1, y) == 'HIDDEN':
            counter = counter + 1
        return counter

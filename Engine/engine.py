from .spot import Spot
from .field import Field
import random

class Engine():

    def __init__(self, width, height, risk):
        self.heightY = height
        self.widthX = width
        self.field = Field(width, height)
        self.bombs = int(risk/100 * width * height)
        self.hiddenValues = width * height - self.bombs
        self.flags = self.bombs
        self.state = 'BEFORE'

    def setUpMap(self, n, x, y):
        self.setUpBombs(n, x, y)
        self.setUpValues()

    def setUpBombs(self, n, x, y):
         places = self.widthX*self.heightY - ( 1 + n ) #pozostale miejsca na bomby( bez punktu startowego i punktow wokol niego
         notPlacedBombs = self.bombs
         while notPlacedBombs > 0:
            notPlacedBombs = notPlacedBombs - 1
            randomNum = random.randint(0, places - 1)
            places = places - 1
            isPlaced = False
            for i in range(0, self.heightY):
                for j in range(0, self.widthX):
                    spot = self.field.getSpot( j, i )
                    if spot.getType() != 'BOMB' and not( j >= x - 1 and j <= x + 1 and i >= y - 1 and i <= y + 1 ) :
                        if randomNum != 0:
                            randomNum = randomNum - 1
                        else:
                            spot.setType('BOMB')
                            isPlaced = True
                            break
                if isPlaced:
                    break

    def setUpValues(self):
        for i in range(0, self.heightY):
            for j in range(0, self.widthX):
                spot = self.field.getSpot( j, i )
                spot.setBombsAround(self.countBombsAround(j, i))

    def countBombsAround(self, x, y):
        up = False
        down = False
        left = False
        right = False
        if x > 0:
            left = True
        if x + 1 < self.widthX:
            right = True
        if y > 0:
            down = True
        if y + 1 < self.heightY:
            up = True

        counter = 0
        if up and left and self.type(x - 1, y + 1) == 'BOMB':
             counter = counter + 1
        if up and self.type(x, y + 1) == 'BOMB':
            counter = counter + 1
        if up and right and self.type(x + 1, y + 1) == 'BOMB':
            counter = counter + 1
        if right and self.type(x + 1, y) == 'BOMB':
            counter = counter + 1
        if down and right and self.type(x + 1, y - 1) == 'BOMB':
            counter = counter + 1
        if down and self.type(x, y - 1) == 'BOMB':
            counter = counter + 1
        if down and left and self.type(x - 1, y - 1) == 'BOMB':
            counter = counter + 1
        if left and self.type(x - 1, y) == 'BOMB':
            counter = counter + 1
        return counter

    def bombsNum(self):
        return self.bombs

    def flagsNum(self):
        return self.flags

    def stateVal(self):
        return self.state

    def unhide(self, x, y):
        up = False
        down = False
        left = False
        right = False

        sum = 0
        if x > 0:
            left = True
            sum = sum + 1
        if x + 1 < self.widthX:
            right = True
            sum = sum + 1
        if y > 0:
            down = True
            sum = sum + 1
        if y + 1 < self.heightY:
            up = True
            sum = sum + 1
        n = 8

        spot = self.field.getSpot(x, y)
        if spot.getVisibility() == 'FLAG':
            self.flags = self.flags + 1
        if self.state == 'BEFORE':
            spot.setVisibility('VISIBLE')
            if sum == 3:
                n = 5
            if sum == 2:
                n = 3
            self.hiddenValues = self.hiddenValues - 1
            self.state = 'STARTED'
            self.setUpMap(n, x, y)
            if up and left:
                self.unhide( x - 1, y + 1 )
            if up:
                self.unhide( x, y + 1)
            if up and right:
                self.unhide( x + 1, y + 1)
            if right:
                self.unhide( x + 1, y )
            if down and right:
                self.unhide( x + 1, y - 1 )
            if down:
                self.unhide( x, y - 1)
            if down and left:
                self.unhide( x - 1, y - 1 )
            if left:
                self.unhide( x - 1, y )
        elif spot.getType() == 'BOMB':
            self.unhideAll()
            self.state = 'LOSE'
        elif spot.getVisibility() != 'VISIBLE':
            spot.setVisibility( 'VISIBLE' )
            self.hiddenValues = self.hiddenValues - 1
            if self.hiddenValues == 0:
                self.state = 'WIN'
            elif self.value( x, y ) == 0:
                    if up and left and self.type( x - 1, y + 1) == 'VALUE' and self.visibility( x - 1, y + 1 ) != 'VISIBLE':
                        self.unhide(x - 1, y + 1)
                    if up and self.type(x, y + 1) == 'VALUE' and self.visibility( x    , y + 1 ) != 'VISIBLE':
                        self.unhide(x, y + 1)
                    if up and right and self.type( x + 1, y + 1) == 'VALUE' and self.visibility( x + 1, y + 1 ) != 'VISIBLE':
                        self.unhide(x + 1, y + 1)
                    if right and self.type( x + 1, y    ) == 'VALUE' and self.visibility( x + 1, y     ) != 'VISIBLE':
                        self.unhide(x + 1, y)
                    if down and right and self.type( x + 1, y - 1) == 'VALUE' and self.visibility( x + 1, y - 1 ) != 'VISIBLE':
                        self.unhide(x + 1, y - 1)
                    if down and self.type( x    , y - 1) == 'VALUE' and self.visibility( x    , y - 1 ) != 'VISIBLE':
                        self.unhide(x, y - 1)
                    if down and left and self.type( x - 1, y - 1) == 'VALUE' and self.visibility( x - 1, y - 1 ) != 'VISIBLE':
                        self.unhide(x - 1, y - 1)
                    if left and self.type( x - 1, y    ) == 'VALUE' and self.visibility( x - 1, y     ) != 'VISIBLE':
                        self.unhide(x - 1, y)

    def switchSymbol(self, x, y):
        spot = self.field.getSpot(x, y)
        current = spot.getVisibility()
        if current != 'VISIBLE':
            if current == 'HIDDEN':
                spot.setVisibility('FLAG')
                self.flags = self.flags - 1
            elif current == 'FLAG':
                spot.setVisibility('QUESTION')
                self.flags = self.flags + 1
            elif current == 'QUESTION':
                spot.setVisibility('HIDDEN')

    def unhideAll(self):
        for i in range(0, self.heightY):
            for j in range(0, self.widthX):
                self.field.getSpot(j, i).setVisibility('VISIBLE')

    def visibility(self, x, y):
        return self.field.getSpot(x, y).getVisibility()

    def type(self, x, y):
        return self.field.getSpot(x, y).getType()

    def value(self, x, y):
        return self.field.getSpot(x, y).getBombsAround();

    def width(self):
        return self.field.getCollumnsNum()

    def height(self):
        return self.field.getRowsNum()

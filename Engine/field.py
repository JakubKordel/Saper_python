from .spot import Spot

class Field():

    def initialize(self):
        self.rows = []
        for r in range(self.rowsNum):
            row = []
            for c in range(self.collumnsNum):
                spot = Spot()
                row.append(spot)
            self.rows.append(row)


    def __init__(self, collumns = 10, rows = 10):
        self.collumnsNum = collumns
        self.rowsNum = rows
        self.initialize()

    def getSpot(self, x, y):
        return self.rows[y][x]

    def getCollumnsNum(self):
        return self.collumnsNum

    def getRowsNum(self):
        return self.rowsNum;

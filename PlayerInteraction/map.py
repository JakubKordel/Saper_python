from Engine.engine import Engine

class Map():
    def __init__(self, engine, pointer):
        self.engine = engine
        self.pointer = pointer
        self.width = engine.width()
        self.height = engine.height()

    def draw(self):
        print(f"Flags: {self.engine.flagsNum()}\n")
        print("klawisz l - odkrywa pole, klawisz p - zmienia pomiedzy X (flaga) -> ? -> O (zakryte)\n")
        for i in range(0, self.height):
            for j in range(0, self.width):
                if self.height - 1 - i == self.pointer.getY():
                    if self.pointer.getX() == j or self.pointer.getX() + 1 == j:
                        print('|', end = '')
                    else:
                        print(' ', end = '')
                else:
                    print(' ', end = '')
                if self.engine.visibility(j, self.height - 1 - i) == 'VISIBLE':
                    if self.engine.type(j, self.height - 1 - i) == 'VALUE':
                        if self.engine.value(j, self.height - 1 - i) == 0:
                            print(' ', end = '')
                        else:
                            print(self.engine.value(j, self.height - 1 - i), end = '')
                    else:
                        print("\033[40m ", end="")
                        print("\033[0m", end="")
                else:
                    if self.engine.visibility(j, self.height - 1 - i) == 'HIDDEN':
                        print('O', end = '')
                    elif self.engine.visibility(j, self.height - 1 - i) == 'FLAG':
                        print("\033[41m ", end="")
                        print("\033[0m", end="")
                    else:
                        print('?', end = '')
                if self.pointer.getX() == self.width - 1 and self.height - 1 - i == self.pointer.getY() and j == self.width - 1:
                    print('|', end = '')
            print("\n")

    #def clearScreen(self):
    #    print("\033[2J\033[H")

def clearScreen():
    print("\033[2J\033[H")

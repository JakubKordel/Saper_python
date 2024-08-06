import sys
import tty
import termios

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

class Input():
    def __init__(self, engine, pointer):
        self.engine = engine
        self.pointer = pointer

    def action(self):
        input = getch()
        if input == 'a':
            self.pointer.left();
        elif input == 'd':
            self.pointer.right();
        elif input == 's':
            self.pointer.down();
        elif input == 'w':
            self.pointer.up();
        elif input == 'l':
            self.engine.unhide( self.pointer.getX(), self.pointer.getY());
        elif input == 'p':
            self.engine.switchSymbol( self.pointer.getX(), self.pointer.getY());

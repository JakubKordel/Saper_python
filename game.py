from Engine import Engine
from PlayerInteraction import Map
from PlayerInteraction import Pointer
from PlayerInteraction import clearScreen
from PlayerInteraction import Input
from PlayerInteraction import getch
from AIPlayer import AIPlayer
import sys
import time

def clear_buf():
    while True:
        c = sys.stdin.read(1)
        if c == '\n' or c == '':
            break

def resultInfo(engine):
    print("\n")
    if engine.stateVal() == 'WIN':
        print("Gratulacje! Wygrales! ", end='')
    else:
        print("BUM!", end='')
    print("\nEnter", end='')
    getch()
    clear_buf()

def refresh(map):
    clearScreen()
    map.draw()

def game(width, height, risk):
    engine = Engine(width, height, risk)
    pointer = Pointer(width, height)
    mapObj = Map(engine, pointer)
    input = Input(engine, pointer)
    while engine.stateVal() != 'WIN' and engine.stateVal() != 'LOSE':
        refresh(mapObj)
        input.action()
    refresh(mapObj)
    resultInfo(engine)

def aiGame(width, height, risk, betweenMovesTimeInterval):
    engine = Engine(width, height, risk)
    pointer = Pointer(-1, -1)
    map = Map(engine, pointer)
    player = AIPlayer(engine)
    while engine.stateVal() != 'WIN' and engine.stateVal() != 'LOSE':
        refresh(map)
        player.move()
        time.sleep(betweenMovesTimeInterval)
    refresh(map)
    resultInfo(engine)

def aiGameTest(width, height, risk, n):
    counter = 0
    i = n
    while i:
        i = i - 1
        engine = Engine(width, height, risk)
        player = AIPlayer(engine)
        while engine.stateVal() != 'WIN' and engine.stateVal() != 'LOSE':
            clearScreen()
            print(f"Rozgrywanie {n} gier . . .", end = '')
            player.move()
        if engine.stateVal() == 'WIN':
            counter = counter + 1
        print(f"\nWygrane: {counter}")
        getch()
        clear_buf()

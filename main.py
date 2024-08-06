from PlayerInteraction import getch
from PlayerInteraction import Pointer
from PlayerInteraction import Map
from PlayerInteraction import clearScreen
from PlayerInteraction import Settings
from Engine import Engine
from Engine import Field
from Engine import Spot
from game import game
from game import aiGame
from game import aiGameTest

a = ''
width = Pointer(66, 0)
height = Pointer(41, 0)
risk = Pointer(201, 0)
gameType = Pointer(3, 0)
setValue = Pointer(0, 4)
settings = Settings(width, height, risk, gameType, setValue)
setValue.down()

while a != 'q':
    clearScreen()
    print("----------------------------------")
    print("              SAPER")
    print("----------------------------------\n")
    print("Sterowanie w grze awsd")
    print("USTAWIENIA\n")
    print("Szerokosc:")
    if setValue.getY() == 3:
        print(" < ", end='')
    else:
        print("   ", end='')
    print(settings.width, end = '')
    if setValue.getY() == 3:
        print(" > ")

    print("\nWysokosc:")
    if setValue.getY() == 2:
        print(" < ", end='')
    else:
        print("   ", end='')
    print(settings.height, end = '')
    if setValue.getY() == 2:
        print(" > ")

    print("\nRyzyko:")
    if setValue.getY() == 1:
        print(" < ", end='')
    else:
        print("   ", end='')
    print(settings.risk, end = '')
    if setValue.getY() == 1:
        print(" > ")

    print("\nTyp gry:")
    if setValue.getY() == 0:
        print(" < ", end='')
    else:
        print("   ", end='')
    if settings.gameType == 'NORMAL':
        print("Normalna", end='')
    elif settings.gameType == 'AI':
        print("Rozgrywka komputera", end='')
    elif settings.gameType == 'AITEST':
        print("Test komputera", end='')
    if setValue.getY() == 0:
        print(" > ")

    print("\ng - uruchamia rozgrywke")
    print("q - aby opuscic gre")

    a = getch()
    settings.set(a)

    if a == 'g':
        if settings.gameType == 'NORMAL':
            game(settings.width, settings.height, settings.risk)
        elif settings.gameType == 'AI':
            aiGame(settings.width, settings.height, settings.risk, 1)
        elif settings.gameType == 'AITEST':
            aiGameTest(settings.width, settings.height, settings.risk, 10)

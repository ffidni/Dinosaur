from os import system
from time import sleep
from random import choice
import keyboard
import pickle

CLEAR = lambda: print("\033[H\033[J")
RESIZE = lambda: system('MODE 70, 28')

def main():
    #Initialize object 'game' to dino class and starting the game
    RESIZE()
    game = Dino()
    game.start()

if __name__ == '__main__':
    main()
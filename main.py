from os import system, name
from time import sleep
from random import choice
from functions import *
import pickle

CLEAR = lambda: print("\033[H\033[J")

#Use different resize commands on different operating system
if name == 'nt':
    RESIZE = lambda: system('MODE 70, 28')
else:
    RESIZE = lambda: system('resize -s 70 28')

def install_requirement():
    #Install keyboard module.
    try:
        import keyboard
        return True
    except:
        system('pip install -r requirements.txt')
        print("Keyboard module has been installed, run the program again.")
        return False

def main():
    RESIZE()
    game = Dino()
    game.start()

#Check if the requirement is installed.
is_installed = install_requirement()
if is_installed:
    from keyboard import is_pressed
else:
    exit()

if __name__ == '__main__':
    main()
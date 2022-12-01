import sys 
import os
import game
import menu

if __name__ == "__main__":
    g = menu.MENU()
    if g is not None:
        game.GAME(g)
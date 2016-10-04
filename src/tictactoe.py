from map_generation import *
from engine import *

if __name__ == "__main__":
    size = 'a'
    while (size.isdigit() is False):
        size = input("Please enter a map size: ")
    game_engine = Engine(size)
    game_engine.gameLoop()

from map_generation import *

if __name__ == "__main__":
    size = 'a'
    while (size.isdigit() is False):
        size = input("Please enter a map size: ")
    game_map = Map(size)

    while (True):
        game_map.promptMap()
        x = input("Enter x: ")
        y = input("Enter y: ")
        game_map.editCase(x, y, 'x')
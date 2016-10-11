from src.map_generation import *

class Engine:
    'This is the engine of the game. Player management, win / lose / draw check, etc...'

    player_icon = ['x', 'o', '-']
    player_name = ['p1', 'p2', 'p3']
    current_player = 0
    size = 0

    def __init__(self, _size):
        print("[Debug] Engine initialization")
        self.game_map = Map(_size)
        self.size = int(_size)

    # Return True if the element is in range and is accessible, and False if any error (out of range / invalid coord)
    def checkIfElementIsAccessible(self, _x, _y):
        if str(_x).isdigit() is not True or str(_y).isdigit() is not True:
            return False
        elif int(_x) < 0 or int(_x) > self.size or int(_y) < 0 or int(_y) > self.size:
            return False
        else:
            return True

    def getInputFromPlayer(self):
        validInput = False
        x_input = 0
        y_input = 0

        while validInput is not True:
            x_input = input("Please enter x: ")
            y_input = input("Please enter y: ")
            if self.checkIfElementIsAccessible(x_input, y_input) is True:
                validInput = True
            else:
                print("---Wrong input:")
        return x_input, y_input

    def checkForWinRow(self, _x, _y, _player):
        if self.game_map.getElement(x + 1, y) == self.player_icon[_player] and self.game_map.getElement(x + 2, y) == self.player_icon[_player]:
            return True
        elif self.game_map.getElement(x + 1, y) == self.player_icon[_player] and self.game_map.getElement(x - 1, y) == self.player_icon[_player]:
            return True
        elif self.game_map.getElement(x - 1, y) == self.player_icon[_player] and self.game_map.getElement(x - 2, y) == self.player_icon[_player]:
            return True
        else:
            return False

    def checkForWinColumn(self, _x, _y, _player):
        if self.game_map.getElement(x, y + 1) == self.player_icon[_player] and self.game_map.getElement(x, y + 2) == self.player_icon[_player]:
            return True
        elif self.game_map.getElement(x, y + 1) == self.player_icon[_player] and self.game_map.getElement(x, y - 1) == self.player_icon[_player]:
            return True
        elif self.game_map.getElement(x, y - 1) == self.player_icon[_player] and self.game_map.getElement(x, y - 2) == self.player_icon[_player]:
            return True
        else:
            return False

# TODO need to check diag and diag inverted !!!!!

    def checkForWin(self, _x, _y, _player):

        print("TODO: Be careful of the vector of check")


    def switchPlayer(self):
        if self.current_player >= 2:
            self.current_player = 0
            return self.current_player
        else:
            self.current_player += 1
            return self.current_player

    #Return False if no draw, True if draw
    def checkForDraw(self):
        i = 0
        draw = False

        while i < self.size and draw is False:
            for element in self.game_map.getRow(i):
                if element == ' ' and draw is False:
                    draw = True
                    break
            i += 1
        draw = not draw
        return draw

    def gameLoop(self):
        end_of_game = False
        while end_of_game is False:
            self.game_map.promptMap()
            place_is_used = True
            while place_is_used is True:
                input_from_current_player = self.getInputFromPlayer()
                if self.game_map.setElement(input_from_current_player[0], input_from_current_player[1], self.player_icon[self.current_player]) is True:
                    place_is_used = False
                else:
                    print("---Wrong input:")
            if self.checkForWin(input_from_current_player[0], input_from_current_player[1]) == True:
                print("!!!! Player win !!! The player " + str(self.player_name[self.current_player]) + "(" + str(self.player_icon[self.current_player]) + ")")
                end_of_game = True
            if self.checkForDraw() is True:
                print("____ Draw ____")
                end_of_game = True
            self.switchPlayer()
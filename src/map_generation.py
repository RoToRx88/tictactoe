import sys

class Map:
    'Everything concerning the map. Content, creation functions, etc...'

    size = 0
    map = []

    def __init__(self, _size = 3):
        self.size = int(_size)
        self.initMap()

    def createRowOfMap(self):
        tmp_array = []
        x = 0

        while x < self.size:
            tmp_array.append(' ')
            x += 1
        return tmp_array

    def initMap(self):
        print("[debug] Initialization of the map with a size of " + str(self.size) + ".")
        y = 0

        while y < self.size:
            self.map.append(self.createRowOfMap())
            y += 1

    #If debug is True, display the raw values of each case instead of interpreted values TODO
    def promptRow(self, _column_number = 0, _debug = False):
        i = 0
        while i < self.size:
            print(str(self.map[_column_number][i])) #TODO: Need to find how to print in a row, fuc*k python, C printf is better
            i += 1

    # If debug is True, display the raw values of each case instead of interpreted values TODO
    def promptMap(self, _debug = False):
        i = 0
        while i < self.size:
            #self.promptRow(i, _debug) #TODO: need to implement the debug option
            print(self.map[i])
            i += 1

    # Return True if the element is in range and is accessible, and False if any error (out of range / invalid coord)
    def checkIfElementIsAccessible(self, _x, _y):
        if str(_x).isdigit() is not True or str(_y).isdigit() is not True:
            return False
        elif int(_x) < 0 or int(_x) > self.size or int(_y) < 0 or int(_y) > self.size:
            return False
        else:
            return True

    #If the element can be placed, return True, if an error occur return False
    def setElement(self, _x, _y, _entity):
        if self.map[int(_y)][int(_x)] == ' ':
            self.map[int(_y)][int(_x)] = _entity
            return True
        else:
            return False

    def getElement(self, _x, _y):
        if str(_x).isdigit() is False or str(_y).isdigit() is False:
            return False
        if self.checkIfElementIsAccessible(int(_x), int(_y)) is False:
            return False
        else:
            return self.map[int(_y)][int(_x)]

    def getRow(self, _row):
        return self.map[_row]
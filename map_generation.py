import sys

class Map:
    'Everything concerning the map. Content, creation functions, etc...'

    size = 0
    map = []

    def __init__(self, _size = 3):
        self.size = int(_size)
        self.initMap()
        if self.size < 3:
            sys.exit() #TODO Find a better way to handle to low map size

    def createRowOfMap(self):
        tmp_array = []
        x = 0

        while x < self.size:
            tmp_array.append(' ')
            x += 1
        return tmp_array

    def initMap(self):
        print("[debug] Initialization of the map with a size of 8.")
        x = 0
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

    def editCase(self, _x, _y, _entity):
        self.map[int(_y) - 1][int(_x) - 1] = _entity

    def getElement(self, _x, _y):
        return self.map[int(_y)][int(_x)]
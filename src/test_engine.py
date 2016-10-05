from unittest import TestCase
from unittest.mock import patch
from src.engine import Engine

class TestEngine(TestCase):
    def test_checkIfElementIsAccessible(self):
        e = Engine(4)
        self.assertIs(e.checkIfElementIsAccessible(1, 1), True)
        self.assertIs(e.checkIfElementIsAccessible(0, 0), False)
        self.assertIs(e.checkIfElementIsAccessible(50, 50), False)
        self.assertIs(e.checkIfElementIsAccessible(1, 59), False)
        self.assertIs(e.checkIfElementIsAccessible(39248, 2), False)
        self.assertIs(e.checkIfElementIsAccessible('', ''), False)
        self.assertIs(e.checkIfElementIsAccessible('zqmeofij', 'zoei'), False)

    def test_getInputFromPlayer(self):
        self.fail()

    def test_checkForWin(self):
        self.fail()

    def test_switchPlayer(self):
        e = Engine(4)
        e.current_player = 0
        self.assertIs(e.current_player, 0)
        self.assertIs(e.switchPlayer(), 1)
        self.assertIs(e.switchPlayer(), 2)
        self.assertIs(e.switchPlayer(), 0)


    def test_checkForDraw(self):
        map_size = 3
        e = Engine(map_size)
        e.game_map.promptMap()
        self.assertIs(e.checkForDraw(), False)
        for y in range(0, map_size):
            for x in range(0, map_size):
                e.game_map.setElement(x, y, 'o')
        e.game_map.promptMap()
        self.assertIs(e.checkForDraw(), True)
()
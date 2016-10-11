from unittest import TestCase
from src.map_generation import Map

class TestMap(TestCase):
    def test_createRowOfMap(self):
        self.fail()

    def test_initMap(self):
        self.fail()


    def test_checkIfElementIsAccessible(self):
        m = Map(4)
        self.assertIs(m.checkIfElementIsAccessible(1, 1), True)
        self.assertIs(m.checkIfElementIsAccessible(0, 0), True)
        self.assertIs(m.checkIfElementIsAccessible(50, 50), False)
        self.assertIs(m.checkIfElementIsAccessible(1, 59), False)
        self.assertIs(m.checkIfElementIsAccessible(39248, 2), False)
        self.assertIs(m.checkIfElementIsAccessible('', ''), False)
        self.assertIs(m.checkIfElementIsAccessible('zqmeofij', 'zoei'), False)

    def test_getRow(self):
        m = Map(4)
        m.setElement(1, 1, 'x')
        m.setElement(1, 0, 'x')
        self.assertIs(m.getRow(1), )
import unittest
from board import Board
from ui import UI


class TestShips(unittest.TestCase):
    def setUp(self) -> None:
        self._board = Board()
        unittest.TestCase.setUp(self)

    def test_add(self):
        print(str(self._board))
        for row in self._board.player_board:
            self.assertListEqual(row, [0, 0, 0, 0, 0, 0])
        for row in self._board.computer_board:
            self.assertListEqual(row, [0, 0, 0, 0, 0, 0])

from board import Board


class UI:
    def __init__(self, board: Board):
        self._board = board

    def start(self):
        print(str(self._board))
        print("	ship <C1L1C2L2C3L3>")
        self._place_battleships()

    def _place_battleships(self):
        pass

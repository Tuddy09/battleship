from texttable import Texttable


class Board:
    def __init__(self):
        self._width = 6
        self._height = 6
        self._player_data = [[0 for i in range(self._width)] for j in range(self._height)]
        self._computer_data = [[0 for i in range(self._width)] for j in range(self._height)]

    def __str__(self):
        header = ["", 'A', 'B', 'C', 'D', 'E', 'F']
        player_board = Texttable()
        player_board.set_cols_dtype(['a', 't', 't', 't', 't', 't', 't'])
        player_board.header(header)
        for i in range(self._height):
            row = [i]
            for element in self._player_data[i]:
                if element == 0:
                    row.append(".")
                elif element == 1:  # player ship
                    row.append("+")
                elif element == -1:  # hit ship
                    row.append("X")
                elif element == 10:  # miss attack
                    row.append("o")
            player_board.add_row(row)

        targeting_board = Texttable()
        targeting_board.set_cols_dtype(['a', 't', 't', 't', 't', 't', 't'])
        targeting_board.header(header)
        for i in range(self._height):
            row = [i]
            for element in self._computer_data[i]:
                if element == 0:
                    row.append(".")
                elif element == 1:  # player ship
                    row.append("+")
                elif element == -1:  # hit ship
                    row.append("X")
                elif element == 10:  # miss attack
                    row.append("o")
            targeting_board.add_row(row)
        return player_board.draw() + '\n' + "        Player board" + '\n' + targeting_board.draw() + '\n' + "       Targeting board"

    def place_ships(self):
        pass

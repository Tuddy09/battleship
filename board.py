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
                elif element == 1:  # computer hidden ship
                    row.append(".")
                elif element == -1:  # hit ship
                    row.append("X")
                elif element == 10:  # miss attack
                    row.append("o")
                elif element == 69:
                    row.append("#")
            targeting_board.add_row(row)
        return player_board.draw() + '\n' + "        Player board" + '\n' + targeting_board.draw() + '\n' + "       Targeting board"

    def place_ships(self, row, column):
        if column == 'A':
            column = 0
        elif column == 'B':
            column = 1
        elif column == 'C':
            column = 2
        elif column == 'D':
            column = 3
        elif column == 'E':
            column = 4
        elif column == 'F':
            column = 5
        self._player_data[int(row)][column] = 1

    def reset_board(self):
        self._player_data = [[0 for i in range(self._width)] for j in range(self._height)]

    def reset_ai_board(self):
        self._computer_data = [[0 for i in range(self._width)] for j in range(self._height)]

    def ai_ships(self, row, column):
        if column == 'A':
            column = 0
        elif column == 'B':
            column = 1
        elif column == 'C':
            column = 2
        elif column == 'D':
            column = 3
        elif column == 'E':
            column = 4
        elif column == 'F':
            column = 5
        self._computer_data[int(row)][column] = 1

    @property
    def player_board(self):
        return self._player_data

    @property
    def computer_board(self):
        return self._computer_data


class ShipValidator:
    def ship_validate(self, positions: list):
        valid_ship = True
        list_of_cols = ['A', 'B', 'C', 'D', 'E', 'F']
        list_of_rows = ['1', '2', '3', '4', '5', '0']
        for index in range(len(positions)):
            if index % 2 == 0:
                if positions[index] not in list_of_cols:
                    valid_ship = False
            else:
                if positions[index] not in list_of_rows:
                    valid_ship = False
        return valid_ship

    def ship_overlap(self, ships_list):
        valid_ship = True
        first_ship = ships_list[0]
        second_ship = ships_list[1]
        ship_row = []
        ship_col = []
        for ship in range(len(first_ship)):
            if ship % 2 == 0:
                ship_col.append(first_ship[ship])
            else:
                ship_row.append(first_ship[ship])
        index = 0
        while index < len(second_ship):
            current_col = second_ship[index]
            current_row = second_ship[index + 1]
            index += 2
            for i in range(len(ship_row)):
                if current_col == ship_col[i] and current_row == ship_row[i]:
                    valid_ship = False
        return valid_ship

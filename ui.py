from board import Board
from computer import AI
from board import ShipValidator


class UI:
    def __init__(self, board: Board):
        self._board = board
        self._ship_validator = ShipValidator()
        self._ai = AI(self._board)

    def start(self):
        print(str(self._board))
        print("Command for placing ships: ship <C1L1C2L2C3L3>")
        coordinates = []
        ships_coordinates = []
        while True:
            try:
                current_command = input(">")
                if current_command == "start" and len(ships_coordinates) == 2:
                    break
                coordinates = current_command.split(" ")
                coordinates = list(coordinates[1])
                if self._ship_validator.ship_validate(coordinates):
                    if len(ships_coordinates) < 1:
                        ships_coordinates.append(coordinates)
                        self._place_battleships(ships_coordinates)
                        print(str(self._board))
                    elif len(ships_coordinates) == 1:
                        ships_coordinates.append(coordinates)
                        if not self._ship_validator.ship_overlap(ships_coordinates):
                            ships_coordinates.pop(1)
                            print("Ships overlap!")
                        self._board.reset_board()
                        self._place_battleships(ships_coordinates)
                        print(str(self._board))
                    else:
                        ships_coordinates.pop(0)
                        ships_coordinates.append(coordinates)
                        self._board.reset_board()
                        self._place_battleships(ships_coordinates)
                        print(str(self._board))
                else:
                    print("Invalid input!")
            except ValueError:
                print("Invalid input!")
            except IndexError:
                print("Invalid input!")
        self._ai.computer_ships()
        self._ai.computer_ships()
        while not self._ai_validator(self._board.computer_board):
            self._board.reset_ai_board()
            self._ai.computer_ships()
            self._ai.computer_ships()
        while True:
            print(str(self._board))
            print("Command for attacking: attack <square>")
            attack_command = input(">")
            if attack_command == "cheat":
                self._ai.cheat_code(self._board.computer_board)
            else:
                command = attack_command.split(" ")
                self._ai.attack(command[1], self._board.player_board, self._board.computer_board)
            if self._ai.check_win(self._board.player_board, self._board.computer_board):
                break

    def _place_battleships(self, list_of_ships):
        for ships in list_of_ships:
            index = 0
            for coords in range(0, len(ships) // 2):
                column = ships[coords + index]
                index += 1
                row = ships[coords + index]
                self._board.place_ships(row, column)

    def _ai_validator(self, computer_board):
        valid = 0
        for row in range(6):
            for col in range(6):
                if computer_board[row][col] == 1:
                    valid += 1
        if valid == 6:
            return True
        return False

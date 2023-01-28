from board import Board
import random
from board import ShipValidator


class AI:
    def __init__(self, board: Board):
        self._board = board
        self._game_over = False
        self._ship_validator = ShipValidator()

    def computer_ships(self):
        list_of_cols = ['B', 'C', 'D', 'E']
        list_of_rows = [1, 2, 3, 4]
        coordinates = []
        col = random.choice(list_of_cols)
        row = random.choice(list_of_rows)
        orientation_choice = random.choice([0, 1])
        if orientation_choice == 0:  # horizontal
            self._board.ai_ships(row, chr(ord(col) - 1))
            self._board.ai_ships(row, col)
            self._board.ai_ships(row, chr(ord(col) + 1))

        else:  # vertical
            self._board.ai_ships(row - 1, col)
            self._board.ai_ships(row, col)
            self._board.ai_ships(row + 1, col)

    def attack(self, attack_command, player_board, computer_board):
        attack_command = list(attack_command)
        list_of_cols = ['A', 'B', 'C', 'D', 'E', 'F']
        list_of_rows = ['1', '2', '3', '4', '5', '0']
        row = attack_command[1]
        col = attack_command[0]
        if col == 'A':
            col = 0
        elif col == 'B':
            col = 1
        elif col == 'C':
            col = 2
        elif col == 'D':
            col = 3
        elif col == 'E':
            col = 4
        elif col == 'F':
            col = 5
        if computer_board[int(row)][int(col)] == 1 or computer_board[int(row)][int(col)] == 69:
            print("Player hits!")
            computer_board[int(row)][int(col)] = -1
        else:
            print("Player misses!")
            computer_board[int(row)][col] = 10
        row = random.choice(list_of_rows)
        col = random.choice(list_of_cols)
        print("computer attack " + str(col) + str(row))
        if col == 'A':
            col = 0
        elif col == 'B':
            col = 1
        elif col == 'C':
            col = 2
        elif col == 'D':
            col = 3
        elif col == 'E':
            col = 4
        elif col == 'F':
            col = 5
        if player_board[int(row)][int(col)] == 1:
            print("Computer hits!")
            player_board[int(row)][col] = -1
        else:
            print("Computer misses!")
            player_board[int(row)][int(col)] = 10

    def cheat_code(self, board):
        for row in range(0, 6):
            for col in range(0, 6):
                if board[row][col] == 1:
                    board[row][col] = 69
        return board

    def check_win(self, player_board, computer_board):
        player_win = True
        computer_win = True
        for row in range(6):
            for col in range(6):
                if player_board[row][col] == 1:
                    computer_win = False
                if computer_board[row][col] == 1 or computer_board[row][col] == 69:
                    player_win = False
        if player_win:
            print("Player wins!")
            return player_win
        elif computer_win:
            print("Computer wins!")
            return computer_win
        return False

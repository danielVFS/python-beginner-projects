import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 3x3 board
        self.current_winner = None

    def print_board(self):
        #   |   |   |
        #   |   |   |
        #   |   |   |
        board = [self.board[i * 3: (i + 1) * 3] for i in range(3)]
        for row in board:
            print('| ' + ' | '.join(row) + ' | ')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 |
        # 3 | 4 | 5 |
        # 6 | 7 | 8 |
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' | ')

    def available_moves(self):


if __name__ == '__main__':
    t = TicTacToe()
    t.print_board()
    t.print_board_nums()

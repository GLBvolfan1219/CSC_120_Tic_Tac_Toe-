import random


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('"')
            self.board.append(row)

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        # showing view of board
        print()
        self.show_board()

# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()

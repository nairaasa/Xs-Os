import random

class ComputerPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, board):
        available_moves = board.available_moves()
        return random.choice(available_moves)

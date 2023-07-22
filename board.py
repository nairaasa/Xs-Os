class Board:
    def __init__(self):
        self.board = [' ' for _ in range(9)]

    def display(self):
        for i in range(0, 9, 3):
            print(self.board[i], '|', self.board[i + 1], '|', self.board[i + 2])
            if i < 6:
                print('---------')

    def is_empty(self, position):
        return self.board[position] == ' '

    def is_full(self):
        return ' ' not in self.board

    def place_move(self, position, symbol):
        self.board[position] = symbol

    def is_winner(self, symbol):
        winning_positions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for pos in winning_positions:
            if all(self.board[p] == symbol for p in pos):
                return True
        return False

    def is_draw(self):
        return self.is_full() and not self.is_winner('X') and not self.is_winner('O')

    def available_moves(self):
        return [i for i in range(9) if self.is_empty(i)]

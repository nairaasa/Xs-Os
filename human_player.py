class HumanPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, board):
        while True:
            try:
                position = int(input(f"Player {self.symbol}, enter your move (0-8): "))
                if position in board.available_moves():
                    return position
                else:
                    print("Invalid move. The position is either taken or out of range. Try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number (0-8).")

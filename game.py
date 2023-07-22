from board import Board
from comp_player import ComputerPlayer
from human_player import HumanPlayer

class TicTacToeGame:
    def __init__(self):
        self.board = Board()

    def print_instructions(self):
        print("Welcome to Tic Tac Toe!")
        print("The board positions are as follows:")
        Board().display()

    def get_player_symbols(self):
        player1_symbol = input("Enter the symbol for Player 1 (X or O): ").upper()
        while player1_symbol not in ['X', 'O']:
            player1_symbol = input("Invalid symbol. Please enter 'X' or 'O': ").upper()

        return player1_symbol, 'O' if player1_symbol == 'X' else 'X'

    def play(self, player1, player2):
        current_player = player1

        while not self.board.is_full():
            self.board.display()
            move = current_player.make_move(self.board)

            if self.board.is_empty(move):
                self.board.place_move(move, current_player.symbol)
                if self.board.is_winner(current_player.symbol):
                    self.board.display()
                    print(f"Player {current_player.symbol} wins!")
                    return

                if self.board.is_draw():
                    self.board.display()
                    print("It's a draw!")
                    return

                current_player = player2 if current_player == player1 else player1

if __name__ == "__main__":
    game = TicTacToeGame()
    game.print_instructions()

    player1_symbol, player2_symbol = game.get_player_symbols()

    player1 = HumanPlayer(player1_symbol)
    player2 = ComputerPlayer(player2_symbol)

    game.play(player1, player2)
import chess
import chess.svg

def print_chessboard(board):
    print("   a  b  c  d  e  f  g  h")
    print(" -------------------------")
    for rank in range(8, 0, -1):
        row = f"{rank}|"
        for file in range(1, 9):
            square = chess.square(file - 1, rank - 1)
            piece = board.piece_at(square)
            if piece is None:
                row += " . "
            else:
                row += f" {piece.symbol()} "
        row += f"|{rank}"
        print(row)
    print(" -------------------------")
    print("   a  b  c  d  e  f  g  h")

def print_possible_moves(board):
    legal_moves = list(board.legal_moves)
    print("Legal Moves:")
    for move in legal_moves:
        print(move.uci())

def main():
    board = chess.Board()
    
    while not board.is_game_over():
        print_chessboard(board)
        print_possible_moves(board)
        
        # Get the move from the user (in algebraic notation, e.g., "e2e4")
        user_move = input("Enter your move (e.g., e2e4): ")
        
        try:
            # Attempt to make the user's move
            board.push_san(user_move)
        except ValueError:
            print("Invalid move. Try again.")
    
    print("Game over. Result: " + board.result())

if __name__ == "__main__":
    main()
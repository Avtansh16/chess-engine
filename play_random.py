import random
import chess

board = chess.Board()

while not board.is_game_over():
    move = random.choice(list(board.legal_moves))
    board.push(move)
    print(board)
    print()

print("Game over:", board.result())
print(board.outcome().termination)

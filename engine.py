import random
import chess
from evaluate import evaluate

def minimax(board, depth, alpha, beta):
    if board.is_checkmate():
        # Side to move has been mated. Faster mates score higher.
        if board.turn == chess.WHITE:
            return -(10000 + depth)
        return 10000 + depth
    if board.is_game_over():
        return 0  # draw
    if depth == 0:
        return evaluate(board)

    if board.turn == chess.WHITE:
        best = -float("inf")
        for move in board.legal_moves:
            board.push(move)
            score = minimax(board, depth - 1, alpha, beta)
            board.pop()
            best = max(best, score)
            alpha = max(alpha, best)
            if alpha >= beta:
                break
        return best
    else:
        best = float("inf")
        for move in board.legal_moves:
            board.push(move)
            score = minimax(board, depth - 1, alpha, beta)
            board.pop()
            best = min(best, score)
            beta = min(beta, best)
            if alpha >= beta:
                break
        return best

def find_best_move(board, depth=3):
    moves = list(board.legal_moves)
    random.shuffle(moves)  # so equal moves aren't always the same one
    best_move = None
    if board.turn == chess.WHITE:
        best_score = -float("inf")
    else:
        best_score = float("inf")

    for move in moves:
        board.push(move)
        score = minimax(board, depth - 1, -float("inf"), float("inf"))
        board.pop()
        if board.turn == chess.WHITE and score > best_score:
            best_score, best_move = score, move
        elif board.turn == chess.BLACK and score < best_score:
            best_score, best_move = score, move
    return best_move

def play():
    board = chess.Board()
    while not board.is_game_over():
        print(board)
        print()
        if board.turn == chess.WHITE:
            text = input("Your move (e.g. e4, Nf3): ")
            try:
                board.push_san(text)
            except ValueError:
                print("Illegal move, try again.")
        else:
            move = find_best_move(board, depth=3)
            print("Engine plays:", board.san(move))
            board.push(move)
    print(board)
    print("Game over:", board.result())

if __name__ == "__main__":
    play()

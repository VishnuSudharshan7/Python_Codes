import numpy as np

def create_board():
    board = np.zeros((6, 7))
    return board

def print_board(board):
    print(np.flip(board, 0))

def is_valid_location(board, col):
    return board[5][col] == 0

def get_next_open_row(board, col):
    for r in range(6):
        if board[r][col] == 0:
            return r

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def winning_move(board, piece):
    # Check horizontal locations for a win
    for c in range(7-3):
        for r in range(6):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations for a win
    for c in range(7):
        for r in range(6-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(7-3):
        for r in range(6-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(7-3):
        for r in range(3, 6):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def main():
    board = create_board()
    game_over = False
    turn = 0

    print_board(board)

    while not game_over:
        # Ask for Player 1 Input
        if turn == 0:
            col = int(input("Player 1 Make your Selection (0-6):"))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 1)

                if winning_move(board, 1):
                    print("PLAYER 1 WINS!!")
                    game_over = True

        # Ask for Player 2 Input
        else:
            col = int(input("Player 2 Make your Selection (0-6):"))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 2)

                if winning_move(board, 2):
                    print("PLAYER 2 WINS!!")
                    game_over = True

        print_board(board)

        turn += 1
        turn = turn % 2

if __name__ == "__main__":
    main()

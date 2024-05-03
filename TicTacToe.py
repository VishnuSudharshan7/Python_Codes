#Tic Tac Toe board
def print_board(board):   
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
        
#check if the current player has won
def check_winner(board, player):    
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

#Main function to run the Tic Tac Toe game
def tic_tac_toe():    
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    for _ in range(9):
        print("Player {}, it's your turn.".format(players[current_player]))
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
        except ValueError:
            print("Invalid input. Please enter row and column values as integers.")
            continue
        
# Check if the chosen cell is within the valid range
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid input. Please enter row and column values between 0 and 2.")
            continue

        # Check if the chosen cell is empty
        if board[row][col] != " ":
            print("This cell is already taken. Please choose another one.")
            continue

        # Place the player's symbol on the board
        board[row][col] = players[current_player]

        # Print the updated board
        print_board(board)

        # Check if the current player has won
        if check_winner(board, players[current_player]):
            print("Congratulations! Player {} wins!".format(players[current_player]))
            return

        # Switch to the next player
        current_player = (current_player + 1) % 2

    print("It's a draw!")

# Run the game
tic_tac_toe()

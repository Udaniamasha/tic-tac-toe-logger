def display_board(board):
    """ Display the current board state """
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")

def check_win(board):
    """ Check if there's a winner or if the game is a draw """
    # Define winning positions
    win_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
                     (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
                     (0, 4, 8), (2, 4, 6)]              # diagonals
    for i in win_positions:
        # Check if the current win position has the same player symbol and is not empty
        if board[i[0]] == board[i[1]] == board[i[2]] != ' ':
            return board[i[0]]  # Return the winning player symbol
    if ' ' not in board:
        return 'Draw'  # Return 'Draw' if there are no empty spots left
    return None  # Return None if there's no winner and the game is not a draw

def save_game_result(board, result, game_history):
    """ Save game result to a text file """
    file_name = f'game_result_{len(game_history)}.txt'  # Generate a file name based on the game history count
    with open(file_name, 'w') as file:
        file.write(f"Game Result: {result}\n")
        
        # Initialize wins counters
        player1_wins = 0
        player2_wins = 0
        draws = 0
        
        # Update counters based on result
        if result == 'Player 1':
            player1_wins = 1
        elif result == 'Player 2':
            player2_wins = 1
        elif result == 'Draw':
            draws = 1
        
        # Write the win counts to the file
        file.write("Player 1 Wins: {}\n".format(player1_wins))
        file.write("Player 2 Wins: {}\n".format(player2_wins))
        file.write("Draws: {}\n".format(draws))

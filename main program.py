import os
#importing functions from game_module
from game_modules import display_board, check_win, save_game_result

def play_game():
    """ Main game loop """
    board = [' '] * 9     # Initialize the game board with 9 empty spaces
    current_player = 'Player 1'  # Player 1 starts first
    game_in_progress = True  # Flag to control the game loop
    game_history = []     # List to store game session history

    while game_in_progress:
        display_board(board)  # Display the current state of the board
        try:
            move = int(input(f"{current_player}, enter your move (1-9), or enter 0 to quit: "))
            if move == 0:
                print("Quitting the game.")
                os._exit(0)  # Exit the program immediately
            elif 1 <= move <= 9 and board[move - 1] == ' ':
                # Update the board with the player's move
                board[move - 1] = 'X' if current_player == 'Player 1' else 'O'
                result = check_win(board)  # Check if the current move wins the game
                if result:
                    display_board(board)  # Display the final state of the board
                    print(f"Game Over! {current_player} wins!")
                    save_game_result(board, current_player, game_history)  # Save the game result
                    game_history.append(board[:])  # Save a copy of the board state
                    break
                # Switch to the other player for the next move
                current_player = 'Player 2' if current_player == 'Player 1' else 'Player 1'
            else:
                print("Invalid move! Please enter a number between 1-9 in an empty spot.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    while True:
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay == 'yes':
            play_game()  # Start a new game if the player chooses to replay
            break
        elif replay == 'no':
            print("Thanks for playing!")#Exiting the game
            break
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")

# Start the game 
if __name__ == "__main__":
    play_game()

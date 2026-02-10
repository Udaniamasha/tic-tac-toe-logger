# CLI Tic-Tac-Toe with Match History

## Overview
A Python-based command-line implementation of the classic Tic-Tac-Toe game. Unlike standard versions, this application features a persistent logging system that saves the outcome of every match to a text file, tracking wins, losses, and draws.

## Features
- **Modular Design:** Game logic and display functions are separated from the main execution loop.
- **2-Player Mode:** Local multiplayer functionality.
- **Input Validation:** Prevents overwriting moves or entering invalid characters.
- **Match Logging:** Automatically generates a `.txt` file (e.g., `game_result_1.txt`) after every game containing the winner and board state.

## How to Run
1. Ensure you have Python installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/Udaniamasha/tic-tac-toe-logger.git
3. Navigate to the directory and run the main script:
    ```bash
   python main.py

## Project Structure
- main.py: Handles the game loop and user input.
- game_modules.py: Contains functions for board display, win checking, and file saving.

**Key Tech:** Python, Modular Programming, File Handling.
   

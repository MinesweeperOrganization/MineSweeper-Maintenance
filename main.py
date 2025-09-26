# ----- main.py -----
"""
File Name: main.py

Description: This is where the project is launched from. It initializes the different classes 
and starts the game by invoking the UI to prompt the player for the number of mines.

All Collaborators: Group 4, ChatGPT, Group 5

Other sources for code: ChatGPT

Date Created: 8/29/2025

Last Updated: 9/26/2025
"""
import tkinter as tk
from board_manager import BoardManager
from game_logic import GameLogic
from input_handler import InputHandler
from user_interface import UserInterface
from sound_manager import SoundManager

# Source: ChatGPT, Group 5
def main():
    # declare the root for the GUI
    root = tk.Tk()
    # give the GUI the title "Minesweeper"
    root.title("Minesweeper")

    # initialize the sound manager
    sound_manager = SoundManager()

    # initialize the game board
    board = BoardManager()

    # initialize the game logic with the game board
    game = GameLogic(board, sound_manager) 

    # initialize the UI with the GUI root and game logic
    # None for input handler because it hasn't been created yet and the handler needs the ui to be initialized
    ui = UserInterface(root, game, None, sound_manager)

    # initialize the input handler with the game logic and UI
    input_handler = InputHandler(game, ui, sound_manager)

    # initialize the input handler in the UI
    ui.input = input_handler

    # starts the game by asking the player to enter the number of mines (10-20)
    ui.show_mine_prompt()

    root.mainloop() # launches the GUI

if __name__ == "__main__":
    main()

# ----- input_handler.py -----
"""
File Name: input_handler.py

Description: Handles user input events for the Minesweeper game. 
    Includes --> 1) Processing left clicks (reveal cells), 2) Processing right clicks (toggle flags), and 3) Coordinating between game logic and UI updates

All Collaborators: Group 4, ChatGPT, Group 5

Other sources for code: ChatGPT

Date Created: 8/29/2025

Last Updated: 9/26/2025
"""
import time #use for AI delay
from sound_manager import SoundManager

class InputHandler:
    """
    Class that handles user input events for the Minesweeper game. 
    Includes --> 1) Processing left clicks (reveal cells), 2) Processing right clicks (toggle flags), and 3) Coordinating between game logic and UI updates
    """

    # Source: ChatGPT, Group 5
    def __init__(self, game_logic, ui, sound_manager: SoundManager):
        # Store reference to the game logic instance for making game state changes
        self.game = game_logic
        # Store reference to the user interface instance for updating the display
        self.ui = ui
        # Sound manager
        self.sound_manager = sound_manager

    # Source: Group 5
    def handle_left_click(self, row, col):
        # Tell the game logic to reveal the clicked cell
        self.game.reveal_cell(row, col)
 
        # Update the visual board display's new state
        self.ui.update_board()
        # Check for victory or loss condition
        if self.game.game_over:

            # Pass victory status (true/false)
            self.ui.show_game_over(self.game.victory)
        else:
            self.sound_manager.play_uncover() # Play uncover sound

        self.game.player_turn = False #swap turn to AI after player click
        self.ui.update_board() #update board before AI turn to show it is AI's turn

        self.ui.root.after(2000, self.ai_turn) #delay AI turn by 2 seconds




    def ai_turn(self):
        self.game.ai_reveal_cell() #have AI reveal a cell
        
        self.ui.update_board() #update board after AI turn
        if self.game.game_over:
            self.ui.show_game_over(self.game.victory)
        else:
            self.sound_manager.play_uncover() # Play uncover sound

    # Source: Original work combined with ChatGPT, Group 5
    def handle_right_click(self, row, col):
        # Don't try to flag an uncovered cell or if the game is over
        if self.game.game_over:
            return
        cell = self.game.board.get_cell(row, col) # get the cell that was clicked
        # Ignore attempts to flag uncovered cells
        if not cell.is_covered:
            return

        changed = self.game.toggle_flag(row, col) # toggle the flag and store if it was toggled
        self.sound_manager.play_flag()
        # if the flag was toggled, update the board
        if changed:
            self.ui.update_board()
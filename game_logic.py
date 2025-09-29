# ----- game_logic.py-----
"""
File Name: game_logic.py

Description: Handles the player's standard interations with the Minesweeper board. 
    Includes --> 1) Keeping track of mines, 2) Placing flags, 3) Revealing cells, and 4) Victory/game-over states

All Collaborators: Group 4, ChatGPT, Group 5, Will

Other sources for code: ChatGPT

Date Created: 8/29/2025

Last Updated: 9/29/2025
"""
import random   #use for random AI cell pick
from board_manager import BoardManager
from sound_manager import SoundManager


class GameLogic:
    """
    Principle class that manipluates the Minesweeper board whenever the player interacts with it.

     In the game of Minesweeper, the player interacts with the board by clicking on cells. When a cell is clicked on it is revealed to be: empty, adjacent to a mine, or a mine.
    The player may also put down a flag on an unrevealed cell that they suspect has a mine. If the player clicks on a mine, the game-over state is triggered. The game is won when all 
    cells not containing mines are revealed.
    """

    # Source: Original work combined with ChatGPT
    def __init__(self, board_manager: BoardManager, sound_manager: SoundManager):
        """
        Initializes game logic for the board the player will interact with

        Input: BoardManager class object from board_manager.py

        Output: None
        
        """

        self.board = board_manager # The board the game is played on (2D array)

        self.total_mines = 10 # The number of mines randomly distrbued across the board

        self.flags = 0 # The number of flags placed (amount of flags the player can place = num of total mines)

        self.game_over = False # Sets the game-over state

        self.victory = False # Sets the victory state

        self.first_click = True # Flag to indicate it is the first click

        self.player_turn = True # Indicate that it is the player's turn

        self.sound_manager = sound_manager # Sound manager

        self.difficulty = "Easy"  # Default difficulty level

    # Source: Original work combined with ChatGPT
    def start_game(self, mine_count, difficulty, safe_cell=None):
        """
        Function that begins the game

        Input: 1 - Number of mines, 2 - Safe cell

        Output: None
        """
        self.difficulty = difficulty #set difficulty level
        print(difficulty)
        self.total_mines = mine_count #The user-given number of mines (10 - 20)

        self.flags = 0 # Begin to count of the number of flags the user has placed

        # Variables to keep track of game state
        self.game_over = False
        self.victory = False
        self.first_click = True # ensure that first_click is set to True for resets
        self.player_turn = True # Indicate that it is the player's turn

        self.sound_manager.play_background() # Play background music

    # Source: Original work combined with ChatGPT
    def toggle_flag(self, row, col):
        """
        Function called whenever the player places down a flag (right click)
        Toggles a flag at (row, col).
        Returns True if the flag state changed, False otherwise.

        Input: The x/y coordinates of the cell that the player clicks on 

        Output: None
        
        """

        if self.game_over:
            return False

        cell = self.board.get_cell(row, col) # The cell that the player clicked on
        
        # Only allow flagging if the cell is still covered
        if not cell.is_covered:
            return False

        # Check if the cell already has a flag on it. If it does, remove the flag.
        if cell.is_flagged:
            cell.is_flagged = False
            self.flags -= 1 # Remove flag
            return True
        
        # If there is no flag on the cell, then check if the player has placed all of their flags. If not, place a flag.
        else:
            if self.flags < self.total_mines:
                cell.is_flagged = True
                self.flags += 1 # Add flag
                return True
            return False

    # Source: Original work combined with ChatGPT, Group 5
    def reveal_cell(self, row, col):
        """
        Function called whenever the player reveals a cell (left click). Checks if the cell can be revealed, triggers game-over if the player uncovers a mine.
            Automatically reveals any adjecant empty cells.

        Input: The x/y coordinates of the cell that the player clicks on 

        Output: None
        """
        # if self.player_turn == False: #add logic for easy mode here.
        #     #randomly pick a cell to reveal for the player
        #     board_size = self.board.size #get the size of the board
        #     row = random.randint(0, board_size - 1)
        #     col = random.randint(0, board_size - 1)

        # Once the player gets a game-over, they may no longer play.
        if self.game_over:
            return
        
        # If it is the first click, initialize the board and set first_click to False
        if self.first_click:
            self.board.initialize_board(self.total_mines, safe_cell=(row, col))
            self.first_click = False
            self.player_turn = False #swap turn to AI after first click

        cell = self.board.get_cell(row, col) # The cell that the player clicked on

        # A cell may not be revealed if: It has a flag on it, or if it has already been revealed.
        if cell.is_flagged or not cell.is_covered:
            return
        
        # Reveal the cell to the player
        cell.is_covered = False

        # If the revealed cell contains a mine, trigger a game-over state
        if cell.is_mine:
            self.game_over = True
            self.victory = False
            self.sound_manager.play_game_over() # Play game over sound
            return

        # If the revealed cell has no adjacent mines, recursively reveal all surrounding cells.
        if cell.adjacent == 0:
            # Check the 8 surrounding cells (nr = near rows, nc = near columns)
            for nr in range(row-1, row+2):
                for nc in range(col-1, col+2):
                    #if the surrounding cells are within the bound of the board AND are not yet revealed, reveal them to the player.
                    if 0 <= nr < self.board.size and 0 <= nc < self.board.size:
                        if self.board.get_cell(nr, nc).is_covered:
                            self.reveal_cell(nr, nc) # Recursive call of reveal_cell function
        
        # if self.player_turn == False: #swap turn between player and AI and vice versa
        #     self.player_turn = True #swap from AI to player
        # else:
        #     self.player_turn = False #swap from player to AI

        self.check_victory() # Check for a victory state after every time a cell is revealed

    def get_covered_neighbors(self, row, col):
        """
        Helper function that returns a list of valid neighboring cell coordinates.

        Input: The x/y coordinates of the cell

        Output: List of tuples containing the coordinates of neighboring cells that are covered and not flagged
        """
        neighbors = []
        for r in range(row-1, row+2):
            for c in range(col-1, col+2):
                if (r == row and c == col) or r < 0 or c < 0 or r >= self.board.size or c >= self.board.size:
                    continue
                if self.board.get_cell(r, c).is_covered and not self.board.get_cell(r, c).is_flagged:
                    neighbors.append((r, c))
        return neighbors

    def get_flagged_neighbors(self, row, col):
        """
        Helper function that returns a list of valid neighboring cell coordinates.

        Input: The x/y coordinates of the cell

        Output: List of tuples containing the coordinates of neighboring cells that are flagged
        """
        neighbors = []
        for r in range(row-1, row+2):
            for c in range(col-1, col+2):
                if (r == row and c == col) or r < 0 or c < 0 or r >= self.board.size or c >= self.board.size:
                    continue
                if self.board.get_cell(r, c).is_flagged:
                    neighbors.append((r, c))
        return neighbors

    def ai_reveal_cell(self):
        """
        Function that allows the AI to reveal a cell on its turn.

        """

        if self.game_over:
            return

        if self.difficulty == "Easy":
            # AI randomly selects a covered, unflagged cell to reveal
            covered_cells = [(r, c) for r in range(self.board.size) for c in range(self.board.size)
                            if self.board.get_cell(r, c).is_covered and not self.board.get_cell(r, c).is_flagged]

            if not covered_cells:
                return  # No cells left to reveal

            row, col = random.choice(covered_cells)
            self.reveal_cell(row, col)
            self.player_turn = True
            # Important, this is linked with input handler under handle left click
        elif self.difficulty == "Medium": #filler of easy for now
            #Gets all revealed numbered cells
            numbered_cells = [(r, c) for r in range(self.board.size) for c in range(self.board.size)
                            if not self.board.get_cell(r, c).is_covered and self.board.get_cell(r, c).adjacent > 0]
            #iterates through all numbered cells 
            for row, col in numbered_cells:
                print(f"AI checking cell at ({row}, {col}) with number {self.board.get_cell(row, col).adjacent}")
                #list of covered neighbors
                covered_neighbors = self.get_covered_neighbors(row, col)
                if len(covered_neighbors) == self.board.get_cell(row, col).adjacent - len(self.get_flagged_neighbors(row, col)):
                    for nr, nc in covered_neighbors:
                        self.toggle_flag(nr, nc)
                        print(f"AI flagged cell at ({nr}, {nc})")    
                    self.player_turn = True
                if len(self.get_flagged_neighbors(row, col)) == self.board.get_cell(row, col).adjacent:
                    covered_neighbors2 = self.get_covered_neighbors(row, col)
                    for nr, nc in covered_neighbors2:
                        self.reveal_cell(nr, nc)
                        print(f"AI revealed cell at ({nr}, {nc})")
                    self.player_turn = True
            if self.player_turn == False:
                covered_cells = [(r, c) for r in range(self.board.size) for c in range(self.board.size)
                            if self.board.get_cell(r, c).is_covered and not self.board.get_cell(r, c).is_flagged]

                if not covered_cells:
                    return  # No cells left to reveal

                row, col = random.choice(covered_cells)
                self.reveal_cell(row, col)
                print(f"AI randomly revealed cell at ({row}, {col})")
                self.player_turn = True
            # Important, this is linked with input handler under handle left click
        elif self.difficulty == "Hard": #filler of easy for now
            # AI randomly selects a covered, unflagged cell to reveal
            covered_cells = [(r, c) for r in range(self.board.size) for c in range(self.board.size)
                            if self.board.get_cell(r, c).is_covered and not self.board.get_cell(r, c).is_flagged]

            if not covered_cells:
                return  # No cells left to reveal

            row, col = random.choice(covered_cells)
            self.reveal_cell(row, col)
            self.player_turn = True
            # Important, this is linked with input handler under handle left click
        

    # Source: ChatGPT, Group 5
    def check_victory(self):
        """
        Helper function that checks for victory state.

        Input: None

        Output: None
        """

        # Check every cell on the board. If all of the cells without mines in them are revealed, trigger the victory state and the game is won.
        for r in range(self.board.size):
            for c in range(self.board.size):

                cell = self.board.get_cell(r, c)

                # If a cell which does not have a mine is still revealed, the player has not won the game.
                if not cell.is_mine and cell.is_covered:
                    return
        
        self.victory = True
        self.game_over = True
        self.sound_manager.play_victory() # Play victory sound
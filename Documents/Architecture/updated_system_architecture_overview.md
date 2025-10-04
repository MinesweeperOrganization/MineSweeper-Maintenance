# Minesweeper Game System Architecture Overview

## 1. Overview
The Minesweeper system is built with a modular, object-oriented architecture that separates concerns into sound management, user interface handling, game logic, board state, and time tracking. The central coordination occurs through `main.py`, which instantiates and connects the core components.

---

## 2. Core Components

### 2.1 main.py
**Responsibilities:**  
Acts as the entry point of the program. Initializes the main game components:
- `SoundManager`
- `BoardManager`
- `GameLogic`
- `UserInterface`

**Key Method:**  
- `main()`: starts the application.

---

## 3. Managers

### 3.1 SoundManager
**Purpose:**  
Handles all audio functionality for menu, background, game events, victory, uncover, and flag sounds.

**Attributes:**  
- `start_menu_thread`, `background_thread`: manage playback threads.  
- `background_playing`, `start_menu_playing`: boolean flags for playback state.  
- `background`, `start_menu`, `game_over`, etc.: store `Sound` objects for each sound type.

**Methods:**  
- `play_start()`, `play_background()`, `play_victory()`, etc. control playback.  
- `stop_music()` halts audio.

---

### 3.2 BoardManager
**Purpose:**  
Manages the game board state, including mine placement and adjacency calculations.

**Attributes:**  
- `size`: board dimensions.  
- `board`: 2D list of `Cell` objects.  
- `mines`: set of mine coordinates.

**Methods:**  
- `initialize_board()`: sets up an empty board.  
- `place_mines()`: randomly places mines.  
- `calculate_adjacent_counts()`: assigns adjacent mine counts.  
- `get_cell()`, `get_orthogonal_cells()`: board access helpers.  
- `reset_board()`: clears the board for a new game.

---

### 3.3 TimeManager
**Purpose:**  
Tracks the elapsed time during gameplay.

**Attributes:**  
- `start_time`, `end_time`, `elapsed`: floats representing timing.

**Methods:**  
- `start_timer()`, `stop_timer()` control measurement.

---

## 4. Game Logic Layer

### 4.1 GameLogic
**Purpose:**  
Implements the core rules and state transitions of Minesweeper.

**Attributes:**  
- References to `BoardManager` and `SoundManager`.  
- `total_mines`, `flags`, `game_over`, `victory`, `first_click`, `player_turn`, `difficulty`.

**Methods:**  
- `start_game()`: initializes gameplay state.  
- `toggle_flag()`, `reveal_cell()`: handle moves.  
- `check_victory()`: evaluates win condition.  
- `get_flagged_neighbors()`, `get_covered_neighbors()`: support reveal logic.  
- `check_visibility()`, `ui_reveal_cell()`: interface updates.

---

## 5. User Interaction Layer

### 5.1 UserInterface
**Purpose:**  
Builds and updates the Tkinter GUI components and manages interactions.

**Attributes:**  
- GUI elements (`Frame`, `Label`, `Entry`, `Button`, `RadioButton`).  
- References to `GameLogic`, `InputHandler`, `SoundManager`, `TimeManager`.

**Methods:**  
- `start_game()`, `update_board()`, `show_game_over()`.  
- `build_board()`: constructs UI grid.  
- `toggle_fullscreen()`, `hide_mine_prompt()`, `show_mine_prompt()`: manage display states.

---

### 5.2 InputHandler
**Purpose:**  
Mediates between user input and game logic.

**Attributes:**  
- References to `GameLogic`, `UserInterface`, `SoundManager`.

**Methods:**  
- `handle_left_click()`: reveals cell.  
- `handle_right_click()`: toggles flags.  
- `__init__()`: connects handlers to game components.

---

## 6. Data Structures

### 6.1 Cell
**Purpose:**  
Represents a single board cell.

**Attributes:**  
- `is_mine`, `is_covered`, `is_flagged`: boolean states.  
- `adjacent`: integer number of adjacent mines.

---

## 7. Component Interactions
- **Initialization:** `main.py` constructs `SoundManager`, `BoardManager`, `GameLogic`, and `UserInterface`. Dependencies are injected at creation.
- **Gameplay Flow:**  
  - User clicks → `InputHandler` routes to `GameLogic`.  
  - `GameLogic` modifies `BoardManager` and updates UI.  
  - `SoundManager` plays sounds for events (reveal, flag, victory).  
  - `TimeManager` tracks elapsed time during active play.
- **Separation of Concerns:**  
  - Board state and rules are isolated in `BoardManager` and `GameLogic`.  
  - UI rendering is handled by `UserInterface`.  
  - Audio is isolated in `SoundManager`.  
  - Timing is separated into `TimeManager`.

---

## 8. Summary
This architecture enforces clear boundaries between logic, presentation, state management, and external I/O. Each class is responsible for a single major function, simplifying testing and future modifications. The use of Tkinter and sound threads allows for an interactive and responsive Minesweeper implementation.

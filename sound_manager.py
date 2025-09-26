# ----- sound_manager.py -----
"""
File Name: sound_manager.py

Description: File that defines the SoundManager class that handles playing sound files.

All Collaborators: Group 5, Gemini

Other sources for code: Gemini

Date Created: 9/25/2025

Last Updated: 9/26/2025
"""

# Requires playsound function from playsound 3 module
# To install, run 'pip install playsound3'
from playsound3 import playsound
import threading

# Source: Group 5 original work, Gemini
class SoundManager:
    # Source: Group 5 original work, Gemini
    def __init__(self):
        # Initialize variables storing play state of sounds
        # Music thread variables
        self.start_menu_thread = None # Start menu thread
        self.background_thread = None # Background thread

        # Music flag variables
        self.start_menu_playing = False # Start menu flag
        self.background_playing = False # Background flag

        # Looping music variables
        self.start_menu = None # Plays on start menu
        self.background = None # Plays in background while playing

        # Non-looping music variables
        self.game_over = None # Plays on loss
        self.victory = None # Plays on victory

        # SFX variables
        self.uncover = None # Uncovering a cell
        self.flag = None # Placing/removing a flag

    # Source: Group 5 original work
    def stop_music(self):
        # Set flags to False
        if self.start_menu_playing: # Start menu flag
            self.start_menu_playing = False # Set flag
        if self.background_playing: # Background flag
            self.background_playing = False # Set flag
        if self.start_menu is not None: # Check if start menu music is not None (playsound object)
            if self.start_menu.is_alive(): # Check if music is currently playing
                self.start_menu.stop() # Stop start menu music
        if self.background is not None: # Check if background music is not None (playsound object)
            if self.background.is_alive(): # Check if music is currently playing
                self.background.stop() # Stop background music
        if self.game_over is not None: # Check if game over sound is not None (playsound object)
            if self.start_menu.is_alive(): # Check if music is currently playing
                self.game_over.stop() # Stop game over music
        if self.victory is not None: # Check if victory sound is not None (playsound object)
            if self.victory.is_alive(): # Check if music is currently playing
                self.victory.stop() # Stop victory music

    # Source: Gemini
    def _loop_start_menu(self):
        # Private method to continuously play the start menu sound
        while self.start_menu_playing: # Loop continuously
            sound = playsound("Sounds/start_menu.mp3", block=False) # Play start menu music
            self.start_menu = sound # Store in a class variable
            sound.wait() # Wait until the sound finishes

    # Source: Gemini
    def _loop_background(self):
        # Private method to continuously play the background music
        while self.background_playing: # Loop continuously
            sound = playsound("Sounds/background.mp3", block=False) # Play background music
            self.background = sound # Store in a class variable
            sound.wait() # Wait until the sound finishes

    # Source: Gemini
    def play_start(self):
        # Play start menu music with the ability to loop
        self.stop_music() # Stop all music
        if not self.start_menu_playing: # Check if the music is already supposed to be playing
            self.start_menu_playing = True # Set control flag to True
            self.start_menu_thread = threading.Thread(target=self._loop_start_menu, daemon=True) # Create a new thread to loop the background music
            self.start_menu_thread.start() # Start the thread

    # Source: Gemini
    def play_background(self):
        # Play background music with the ability to loop
        self.stop_music() # Stop all music
        if not self.background_playing: # Check if the music is already supposed to be playing
            self.background_playing = True # Set control flag to True
            self.background_thread = threading.Thread(target=self._loop_background, daemon=True) # Create a new thread to loop the background music
            self.background_thread.start() # Start the thread

    # Source: Group 5 original work
    def play_game_over(self):
        # Play game over music
        self.stop_music() # Stop all music
        self.game_over = playsound("Sounds/game_over.mp3", block=False) # Play game over sound (does not loop)

    # Source: Group 5 original work
    def play_victory(self):
        # Play victory music
        self.stop_music() # Stop all music
        self.victory = playsound("Sounds/victory.mp3", block=False) # Play victory sound (does not loop)
    
    # Source: Group 5 original work
    def play_uncover(self):
        # Play uncover sound effect
        self.uncover = playsound("Sounds/uncover.mp3", block=False) # Play uncover sound (does not loop)

    # Source: Group 5 original work
    def play_flag(self):
        # Play flag sound effect
        self.flag = playsound("Sounds/flag.mp3", block=False) # Play flag sound (does not loop)
# ----- sound_manager.py -----
"""
File Name: sound_manager.py

Description: File that defines the SoundManager class that handles playing sound files.

All Collaborators: Group 5

Other sources for code: None

Date Created: 9/25/2025

Last Updated: 9/26/2025
"""

# Requires playsound function from playsound 3 module
# To install, run 'pip install playsound3'
from playsound3 import playsound

# Source: Group 5 original work
class SoundManager:
    # Source: Group 5 original work
    def __init__(self):
        # Initialize variables storing play state of sounds
        # Music
        self.background = None # Plays in background while playing
        self.game_over = None # Plays on loss
        self.start_menu = None # Plays on start menu
        self.victory = None # Plays on victory

        # SFX
        self.uncover = None # Uncovering a cell
        self.flag = None # Placing/removing a flag

    # Source: Group 5 original work
    def stop_music(self):
        # Stop all playing music files
        try: # If sound has not been played during runtime, it is NoneType and will raise an exception (means sound is not playing)
            if self.start_menu.is_alive(): # Check if start menu music is playing
                self.start_menu.stop() # Stop sound
        except: pass # Do nothing, sound not playing
        try: # If sound has not been played during runtime, it is NoneType and will raise an exception (means sound is not playing)
            if self.background.is_alive(): # Check if background music is playing
                self.background.stop() # Stop sound
        except: pass # Do nothing, sound not playing
        try: # If sound has not been played during runtime, it is NoneType and will raise an exception (means sound is not playing)
            if self.game_over.is_alive(): # Check if game over music is playing
                self.game_over.stop() # Stop sound
        except: pass # Do nothing, sound not playing
        try: # If sound has not been played during runtime, it is NoneType and will raise an exception (means sound is not playing)
            if self.victory.is_alive(): # Check if victory music is playing
                self.victory.stop() # Stop sound
        except: pass # Do nothing, sound not playing

    # Source: Group 5 original work
    def play_start(self):
        # Play start menu music with the ability to loop
        try: # If sound has not been played during runtime, it is NoneType and will raise an exception (means sound is not playing)
            if not self.start_menu.is_alive(): # Check if start music is not currently playing
                self.stop_music() # Stop all music
                self.start_menu = playsound("Sounds/start_menu.mp3") # Play start menu sound
        except: # First time playing sound during runtime
            self.start_menu = playsound("Sounds/start_menu.mp3") # Play start menu sound
    
    # Source: Group 5 original work
    def play_background(self):
        # Play background music with the ability to loop
        try: # If sound has not been played during runtime, it is NoneType and will raise an exception (means sound is not playing)
            if not self.background.is_alive(): # Check if background music is not currently playing
                self.stop_music() # Stop all music
                self.background = playsound("Sounds/background.mp3", block=False) # Play background sound
        except: # First time playing sound during runtime
            self.background = playsound("Sounds/background.mp3", block=False) # Play background sound

    # Source: Group 5 original work
    def play_game_over(self):
        # Play game over music
        self.stop_music() # Stop all music
        self.game_over = playsound("Sounds/game_over.mp3") # Play game over sound (does not loop)

    # Source: Group 5 original work
    def play_victory(self):
        # Play victory music
        self.stop_music() # Stop all music
        self.victory = playsound("Sounds/victory.mp3") # Play victory sound (does not loop)
    
    # Source: Group 5 original work
    def play_uncover(self):
        # Play uncover sound effect
        self.uncover = playsound("Sounds/uncover.mp3") # Play uncover sound (does not loop)

    # Source: Group 5 original work
    def play_flag(self):
        # Play flag sound effect
        self.flag = playsound("Sounds/flag.mp3") # Play flag sound (does not loop)
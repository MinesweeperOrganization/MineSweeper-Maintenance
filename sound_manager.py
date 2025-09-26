# ----- sound_manager.py -----
"""
File Name: sound_manager.py

Description: 

All Collaborators: Group 5

Other sources for code: None

Date Created: 9/25/2025

Last Updated: 9/25/2025
"""

from playsound3 import playsound

class SoundManager:
    def __init__(self):
        self.background = None
        self.dig = None
        self.flag = None
        self.game_over = None
        self.start_menu = None
        self.victory = None

    def play_start(self):
        try:
            if self.background.is_alive():
                self.background.stop()
        except: pass
        self.start_menu = playsound("Sounds/start_menu.mp3")
    
    def play_background(self):
        self.background = playsound("Sounds/background.mp3", block=False)
        
    def play_dig(self):
        self.dig = playsound("Sounds/dig.mp3")

    def play_flag(self):
        self.flag = playsound("Sounds/flag.mp3")
    
    def play_game_over(self):
        try:
            if self.background.is_alive():
                self.background.stop()
        except: pass
        self.game_over = playsound("Sounds/game_over.mp3")

    def play_victory(self):
        try:
            if self.background.is_alive():
                self.background.stop()
        except: pass
        self.victory = playsound("Sounds/victory.mp3")
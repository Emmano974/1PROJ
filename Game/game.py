import pygame
from player import Crash

# Classe qui représente le jeu
class Game:

    def __init__(self):
        # genere le joueur
        self.crash = Crash()
        self.key_pressed = {}

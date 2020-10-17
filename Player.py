import pygame
from Const import *

class Player(object):

    def __init__(self, screen):
        self.lives = 3  # Always start with three lives
        self.screen = screen

    def takeDamage(self, amount):
        self.lives -= amount


import pygame
from Const import *

class Player(object):

    def __init__(self, screen):

        self.lives = 3  # Always start with three lives
        self.points = 0  # Always start with three lives
        self.screen = screen

    def addScore(self, amount):
        self.points += amount

    def displayScore(self):
        font = pygame.font.SysFont("sans", 20)
        text = font.render(f"Lives: {self.lives} Score: {self.points}", True, (225, 0, 0))
        self.screen.blit(text, (10, SCREEN_HEIGHT - 20))

    def takeLife(self):
        self.lives -= 1
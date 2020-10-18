import pygame
from Const import *

class Player(object):

    def __init__(self, screen):

        self.lives = 3  # Always start with three lives
        self.points = 0  # Always start with three lives
        self.screen = screen
        self.sounds = {
            SOUND_DAMAGE: pygame.mixer.Sound(SOUND_DAMAGE),
        }

    def displayScore(self):
        font = pygame.font.SysFont("sans", 20)
        text = font.render(f"Lives: {self.lives} Score: {self.points}", True, (225, 0, 0))
        self.screen.blit(text, (10, SCREEN_HEIGHT - 20))

    def play(self, sound):
        if sound in self.sounds:
            self.sounds[sound].play()

    def score(self, amount):
        self.points += amount
        self.play(SOUND_DAMAGE)


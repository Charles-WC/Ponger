import pygame
from Const import *

class Player(object):

    def __init__(self, screen):

        self.lives = 3  # Always start with three lives
        self.screen = screen
        self.sounds = {
            SOUND_DAMAGE: pygame.mixer.Sound(SOUND_DAMAGE),
        }

    def displayScore(self):
        font = pygame.font.SysFont("sans", 20)
        text = font.render(f"Lives: {self.lives}", True, (0, 128, 0))
        self.screen.blit(text, (10, 10))

    def playSound(self, sound):
        if sound in self.sounds:
            self.sounds[sound].play()

    def takeDamage(self, amount):
        self.lives -= amount
        self.playSound(SOUND_DAMAGE)


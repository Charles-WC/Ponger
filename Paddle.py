import pygame
from Const import *

class Paddle(object):

    def __init__(self, screen):
        self.direction = DIRECTION_NONE
        self.image = pygame.image.load("res/paddle.png")
        self.screen = screen
        self.speed = 300
        self.state = PADDLE_STATE_STILL
        self.width = 150
        self.height = 25
        self.x = 0
        self.y = 0

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self, time_delta, direction):

        self.direction = direction

        if self.direction == DIRECTION_LEFT:
            pixels_to_move_x = -self.speed
        else:
            pixels_to_move_x = self.speed

        self.x += time_delta * pixels_to_move_x

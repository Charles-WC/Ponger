import pygame
from Const import *

class Ball(object):

    def __init__(self, screen):

        self.radius = 10
        self.screen = screen
        self.state = BALL_STATE_READY
        self.x = 0
        self.y = 0
        self.x_direction = DIRECTION_NONE
        self.y_direction = DIRECTION_UP
        self.x_speed = 400
        self.y_speed = 250

    def draw(self):
        pygame.draw.circle(self.screen, (227, 232, 41), (int(self.x), int(self.y)), self.radius)

    def move(self, time_delta):

        # First, let's GTFO if we are already doing something
        if self.state is not BALL_STATE_MOVE:
            return None

        if self.x_direction == DIRECTION_LEFT:
            pixels_to_move_x = -self.x_speed
        else:
            pixels_to_move_x = self.x_speed

        if self.y_direction == DIRECTION_UP:
            pixels_to_move_y = -self.y_speed
        else:
            pixels_to_move_y = self.y_speed

        self.x += time_delta * pixels_to_move_x
        self.y += time_delta * pixels_to_move_y

    def moveCenter(self, new_x):
        pass

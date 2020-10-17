import pygame
from Const import *

class Ball(object):

    def __init__(self, paddle):

        self.paddle = paddle
        self.radius = 10
        self.screen = paddle.screen
        self.sounds = {
            SOUND_BOUNCE: pygame.mixer.Sound(SOUND_BOUNCE),
            SOUND_STRIKE: pygame.mixer.Sound(SOUND_STRIKE)
        }
        self.state = BALL_STATE_READY
        self.x = 0
        self.y = 0
        self.x_direction = DIRECTION_NONE
        self.y_direction = DIRECTION_UP
        self.x_speed = 400
        self.y_speed = 250

    def bounce(self, direction):

        # Figure out which axis to change
        if direction in (DIRECTION_DOWN, DIRECTION_UP):
            self.y_direction = direction
        else:
            self.x_direction = direction

        # Play the bounce sound
        self.playSound(SOUND_BOUNCE)

    def playSound(self, sound):
        if sound in self.sounds:
            self.sounds[sound].play()

    def draw(self):
        pygame.draw.circle(self.screen, BALL_COLOR, (int(self.x), int(self.y)), self.radius)

    def fire(self):
        if self.state is not BALL_STATE_MOVE:
            self.state = BALL_STATE_MOVE

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

    def reset(self):
        """ This will recenter the ball on the paddle"""
        self.state = BALL_STATE_READY
        self.x = self.paddle.x + (self.paddle.width / 2)
        self.y = self.paddle.y - self.radius

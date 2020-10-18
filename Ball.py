import pygame
from Const import *

class Ball(pygame.sprite.Sprite):

    def __init__(self, paddle):

        super().__init__()
        self.paddle = paddle
        self.radius = 10
        self.rect = pygame.rect.Rect(paddle.x + (paddle.width / 2), paddle.y - self.radius, TILE_WIDTH, TILE_HEIGHT)
        self.screen = paddle.screen
        self.sounds = {
            SOUND_BOUNCE: pygame.mixer.Sound(SOUND_BOUNCE),
            SOUND_STRIKE: pygame.mixer.Sound(SOUND_STRIKE)
        }
        self.state = BALL_STATE_READY
        self.x = paddle.x + (paddle.width / 2)
        self.y = paddle.y - self.radius
        self.x_direction = DIRECTION_NONE
        self.y_direction = DIRECTION_UP
        self.x_delta = 400
        self.y_delta = 250

    def bounce(self, direction, play_sound=True):

        # Figure out which axis to change
        if direction in (DIRECTION_DOWN, DIRECTION_UP):
            self.y_direction = direction
        else:
            self.x_direction = direction

        # And we need to change the deltas if we are going up
        if direction == DIRECTION_UP:
            self.x_delta = self.x - self.paddle.x

        # Play the bounce sound
        if play_sound:
            self.play(SOUND_BOUNCE)

    def draw(self):
        self.rect = pygame.rect.Rect(int(self.x), int(self.y), TILE_WIDTH, TILE_HEIGHT)
        pygame.draw.circle(self.screen, BALL_COLOR, (int(self.x), int(self.y)), self.radius)

    def fire(self):
        if self.state is not BALL_STATE_MOVE:
            self.state = BALL_STATE_MOVE

    def move(self, time_delta):

        # First, let's GTFO if we are already doing something
        if self.state is not BALL_STATE_MOVE:
            return None

        # Let's move the X Direction
        if self.x_direction == DIRECTION_LEFT:
            self.x += time_delta * -self.x_delta
        else:
            self.x += time_delta * self.x_delta

        # And now move the y direction
        if self.y_direction == DIRECTION_UP:
            self.y += time_delta * -self.y_delta
        else:
            self.y += time_delta * self.y_delta

    def play(self, sound):
        if sound in self.sounds:
            self.sounds[sound].play()

    def reset(self):
        """ This will recenter the ball on the paddle"""
        self.state = BALL_STATE_READY
        self.x = self.paddle.x + (self.paddle.width / 2)
        self.y = self.paddle.y - self.radius

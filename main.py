import pygame
from Player import Player
from Paddle import Paddle
from Ball import Ball
from Const import *

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# create the player
player = Player(screen)

# create the paddle
paddle = Paddle(screen)
paddle.x = SCREEN_WIDTH / 2 - paddle.width / 2
paddle.y = SCREEN_HEIGHT - (paddle.height * 2)

# start at the center of the paddle
ball = Ball(paddle)
ball.x = paddle.x + (paddle.width / 2)
ball.y = paddle.y - ball.radius

while True:

    time_delta = clock.tick(FRAME_RATE) / 1000

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Fire the ball
                ball.fire()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.x > 0:
        paddle.move(time_delta, DIRECTION_LEFT)
    elif keys[pygame.K_RIGHT] and paddle.x <= SCREEN_WIDTH - paddle.width:
        paddle.move(time_delta, DIRECTION_RIGHT)

    # FIll up the background
    screen.fill((25, 25, 25))

    # Is the ball moving?
    if ball.state == BALL_STATE_MOVE:

        # Check the x boundaries for the ball. Soon this will be with other sprites, not just the edge of the game
        if ball.x <= 0:
            ball.bounce(DIRECTION_RIGHT)
        elif ball.x >= SCREEN_WIDTH - ball.radius:
            ball.bounce(DIRECTION_LEFT)

        # If the ball is off the map, send it back down. TODO: REPLACE WITH TILES
        if ball.y <= 0:
            ball.bounce(DIRECTION_DOWN)

        # Check if we are off the screen
        if ball.y >= SCREEN_HEIGHT:
            # We need to take damage, and reset the ball
            player.takeDamage(1)
            ball.reset()

        elif ball.y + ball.radius >= paddle.y:
            #  First, check to see if the bottom of the ball is the same as the top of the paddle.

            #  If so, then check to see if the x of the ball is within in the x_width of the paddle
            if ball.x > paddle.x and ball.x < paddle.x + paddle.width:

                # it is, so we need to reverse the course of the ball.
                ball.y_direction = DIRECTION_UP

                # and we need to figure out the right degree in which to bounce, and adjust the X and Y speeds accordingly
                x_axis = ball.x - paddle.x
                ball.x_speed = x_axis

    ball.move(time_delta)
    paddle.draw()
    ball.draw()
    player.displayScore()
    pygame.display.update()

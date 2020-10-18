import pygame
from Player import Player
from Paddle import Paddle
from Ball import Ball
from Tiles import Tiles, Tile
from Const import *

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# create the player
player = Player(screen)

# create the tiles
tiles = Tiles(screen)

# create the paddle
paddle = Paddle(screen)
paddle.x = SCREEN_WIDTH / 2 - paddle.width / 2
paddle.y = SCREEN_HEIGHT - (paddle.height * 2)

# start at the center of the paddle
ball = Ball(paddle)

while True:

    time_delta = clock.tick(FRAME_RATE) / 1000 * 2

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

        # Check the x boundaries for the ball
        if ball.x <= 0:
            ball.bounce(DIRECTION_RIGHT)
        elif ball.x >= SCREEN_WIDTH - ball.radius:
            ball.bounce(DIRECTION_LEFT)

        # Check the Y boundaries of the ball
        # If the ball is off the map, send it back down.
        if ball.y <= 0:
            ball.bounce(DIRECTION_DOWN)

        # Check if we are off the screen
        elif ball.y >= SCREEN_HEIGHT:

            # We need to take damage, and reset the ball
            player.takeLife()
            ball.reset()

        # Check to see if the ball is hitting the paddle
        elif ball.y + ball.radius >= paddle.y:

            #  If so, then check to see if the x of the ball is within in the x_width of the paddle
            if ball.x > paddle.x and ball.x < paddle.x + paddle.width:
                # it is, so we need to reverse the course of the ball.
                ball.bounce(DIRECTION_UP)

        if tiles.hasBallHitTile(ball):
            ball.bounce(DIRECTION_DOWN)
            player.addScore(1)

    paddle.draw()
    ball.move(time_delta)
    ball.draw()
    tiles.draw(screen)

    player.displayScore()
    pygame.display.update()

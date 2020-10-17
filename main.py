import pygame

BALL_STATE_READY = "ready"
BALL_STATE_FIRING = "firing"

DIRECTION_NONE = "none"
DIRECTION_LEFT = "left"
DIRECTION_RIGHT = "right"
DIRECTION_UP = "up"
DIRECTION_DOWN = "down"

FRAME_RATE = 60

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
PADDLE_STATE_STILL = "still"
PADDLE_STATE_MOVE = "moving"


class Ball(object):

    def __init__(self, screen):

        self.radius = 10
        self.screen = screen
        self.state = BALL_STATE_READY
        self.x = 0
        self.y = 0
        self.x_direction = DIRECTION_NONE
        self.y_direction = DIRECTION_UP
        self.x_speed = 300
        self.y_speed = 100

    def draw(self):
        pygame.draw.circle(self.screen, (227, 232, 41), (int(self.x), int(self.y)), self.radius)

    def move(self, time_delta):

        # First, let's GTFO if we are already doing something
        if self.state is not BALL_STATE_FIRING:
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
        


class Paddle(object):

    def __init__(self, screen):
        self.direction = DIRECTION_NONE
        self.image = pygame.image.load("res/paddle.png")
        self.screen = screen
        self.speed = 300
        self.state = PADDLE_STATE_STILL
        self.width = 200
        self.height = 25
        self.x = 0
        self.y = 0

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self, time_delta):

        # Check the direction
        if self.state == PADDLE_STATE_STILL:
            return

        if self.direction == DIRECTION_LEFT:
            pixels_to_move_x = -self.speed
        else:
            pixels_to_move_x = self.speed

        self.x += time_delta * pixels_to_move_x


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# create the paddle
paddle = Paddle(screen)
paddle.x = SCREEN_WIDTH / 2 - paddle.width / 2
paddle.y = SCREEN_HEIGHT - (paddle.height * 2)

# start at the center of the paddle
ball = Ball(screen)
ball.x = paddle.x + (paddle.width / 2)
ball.y = paddle.y - ball.radius

while True:

    time_delta = clock.tick(FRAME_RATE) / 1000

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            SystemExit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ball.state = BALL_STATE_FIRING
        elif event.type == pygame.KEYUP:
            paddle.state = PADDLE_STATE_STILL

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.direction = DIRECTION_LEFT
        paddle.state = PADDLE_STATE_MOVE
    elif keys[pygame.K_RIGHT]:
        paddle.direction = DIRECTION_RIGHT
        paddle.state = PADDLE_STATE_MOVE

    # FIll up the background
    screen.fill((25, 25, 25))

    # Check the boundaries. Soon this will be with other sprites, not just the edge of the game
    if ball.x <= 0:
        ball.x_direction = DIRECTION_RIGHT
    elif ball.x >= SCREEN_WIDTH - ball.radius:
        ball.x_direction = DIRECTION_LEFT

    if ball.y <= 0:
        ball.y_direction = DIRECTION_DOWN
    elif ball.y >= SCREEN_HEIGHT - ball.radius:
        ball.y_direction = DIRECTION_UP

    ball.move(time_delta)
    paddle.move(time_delta)
    paddle.draw()
    ball.draw()

    pygame.display.update()

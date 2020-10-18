import pygame
from Const import *


class Tiles(pygame.sprite.Group):

    def __init__(self, screen, *sprites):

        super().__init__(*sprites)
        self.screen = screen
        self.tiles = []
        self.tile_image = pygame.image.load("res/tile.png")
        self.populate()

    def populate(self):

        # Add up to three levels of tiles TODO: Change this to increase with levels
        for index_x in range(0, int(SCREEN_WIDTH / TILE_WIDTH)):

            # Cycle through the Y's
            for index_y in range(0, 3):
                tile = Tile(self.screen, self.tile_image, index_x * TILE_WIDTH, index_y * TILE_HEIGHT)
                self.add(tile)

class Tile(pygame.sprite.Sprite):

    def __init__(self, screen, tile_image, x, y):
        super().__init__()
        self.image = tile_image
        self.rect = pygame.rect.Rect(x, y, TILE_WIDTH, TILE_HEIGHT)
        self.screen = screen
        self.x = x
        self.y = y

    def draw(self):
        self.rect = pygame.rect.Rect(int(self.x), int(self.x), TILE_WIDTH, TILE_HEIGHT)
        self.screen.blit(self.image, (self.x, self.y))

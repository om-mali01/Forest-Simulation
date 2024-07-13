import pygame, sys

class Tile:
    def __init__(self, x, y, width, height, color) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height) #creats the rectangle/Tile

    def draw_tile(self, screen):
        # draws the tile on scrreen
        self.screen = screen
        pygame.draw.rect(self.screen, self.color, self.rect)

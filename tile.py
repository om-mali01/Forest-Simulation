import pygame

class Tile:
    def __init__(self, x, y, tile_width, tile_height, tile_color, age, max_age, alive=False) -> None:
        self.x = x
        self.y = y
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.tile_color = tile_color
        self.age = age
        self.max_age = max_age
        self.alive = alive
        self.rect = pygame.Rect(x, y, tile_width, tile_height)
    
    def grow(self) -> None:
        if self.age < self.max_age:
            self.age += 1
            self.tile_color = (0, 250 - 15*self.age, 0)
            self.alive = True

    def draw_tile(self, screen):
        self.screen = screen
        pygame.draw.rect(self.screen, self.tile_color, self.rect)

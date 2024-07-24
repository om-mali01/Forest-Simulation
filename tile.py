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
        '''when the tree cross the age limit ie.max_age it will die
            if the max age is 10 then at 11th it will die'''
        if self.age < self.max_age:
            self.age += 1
            self.tile_color = (0, 210 - 10*self.age, 0)
            self.alive = True
        else:
            self.tile_color = (128, 128, 128)
            self.alive = False

    def draw_tile(self, screen):
        self.screen = screen
        pygame.draw.rect(self.screen, self.tile_color, self.rect)

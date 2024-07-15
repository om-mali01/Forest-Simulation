import pygame

class Tile:
    def __init__(self, x, y, tile_width, tile_height, tile_color, age, alive=False) -> None:
        self.x = x
        self.y = y
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.tile_color = tile_color
        self.age = age
        self.alive = alive
        self.rect = pygame.Rect(x, y, tile_width, tile_height)
    
    def grow(self) -> None:
        self.age += 1
        if self.age > 10:
            self.alive = False
            self.tile_color = (139, 69, 19) #brown
        elif 4 < self.age < 7:
            self.tile_color = (0,150, 0)  #light green
        else:
            self.tile_color = (0, 200, 0)  #dark green

    def draw_tile(self, screen):
        self.screen = screen
        pygame.draw.rect(self.screen, self.tile_color, self.rect)

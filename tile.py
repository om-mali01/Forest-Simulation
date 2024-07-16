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
        if self.age < 10:
            self.age += 1
            if self.age < 1:
                self.tile_color = (0,230, 0)  
            elif self.age < 2:
                self.tile_color = (0, 220, 0)
            elif self.age < 3:
                self.tile_color = (0, 200, 0)
            elif self.age < 4:
                self.tile_color = (0, 180, 0)
            elif self.age < 5:
                self.tile_color = (0, 150, 0)
            elif self.age < 6:
                self.tile_color = (0, 140, 0)
            elif self.age < 7:
                self.tile_color = (0, 130, 0)
            elif self.age < 8:
                self.tile_color = (0, 120, 0)
            elif self.age < 9:
                self.tile_color = (0, 110, 0)
            else:
                self.tile_color = (0,100, 0) #darkest

    def draw_tile(self, screen):
        self.screen = screen
        pygame.draw.rect(self.screen, self.tile_color, self.rect)

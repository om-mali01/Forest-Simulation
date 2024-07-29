import pygame
import stats

class Tile:
    def __init__(self, x, y, tile_width, tile_height, tile_color, age, max_age, height, alive=False) -> None:
        self.x = x
        self.y = y
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.tile_color = tile_color
        self.age = age
        self.max_age = max_age
        self.height = height
        self.alive = alive
        self.rect = pygame.Rect(x, y, tile_width, tile_height)
    
    def grow(self) -> None:
        '''when the tree cross the age limit ie.max_age it will die
            if the max age is 10 then at 11th it will die'''
        if self.tile_color == (128, 128, 128):
            return
        elif self.age < self.max_age:
            self.age += 1
            self.height += 2
            stats.update_max_age_tree(self.age)           #update the max age
            stats.update_max_height_tree(self.height)     #update the max height
            self.tile_color = (0, 250 - 20*self.age, 0)
            self.alive = True
        else:
            self.tile_color = (128, 128, 128)
            self.alive = False
            self.age = 0
            self.height = 0
            stats.increment_total_dead_trees()            #count the dead trees

    def draw_tile(self, screen):
        self.screen = screen
        pygame.draw.rect(self.screen, self.tile_color, self.rect)

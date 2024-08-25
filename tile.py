import pygame
import stats

class Tile:
    def __init__(self, x, y, tile_width, tile_height, tile_color, age, max_age, height, tree_species, stats, alive=False) -> None:
        self.x = x
        self.y = y
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.tile_color = tile_color
        self.age = age
        self.max_age = max_age
        self.height = height
        self.stats = stats
        self.alive = alive
        self.temperature = tree_species["temperature range"]
        self.ph =tree_species["pH range"]
        self.growth_rate = tree_species["growth rate"]
        self.rect = pygame.Rect(x, y, tile_width, tile_height)
    
    def grow(self, forest_temp, soil_ph) -> None:
        '''when the tree cross the age limit ie.max_age it will die
            if the max age is 10 then at 11th it will die'''
        if self.tile_color == (128, 128, 128):
            return
        elif self.age < self.max_age:
            self.age += 1
            if self.temperature[0] < forest_temp < self.temperature[1] and self.ph[0] < soil_ph < self.ph[1]:
                self.height += self.growth_rate
            else:
                self.growth_rate -= 0.5
                self.height += self.growth_rate

            self.stats.update_max_age_tree(self.age)           #update the max age
            self.stats.update_max_height_tree(self.height)     #update the max height
            self.tile_color = (0, 250 - 20*self.age, 0)
            self.alive = True
        else:
            self.tile_color = (128, 128, 128)
            self.alive = False
            self.age = 0
            self.height = 0
            self.stats.increment_dead_trees()            #count the dead trees

    def draw_tile(self, screen):
        self.screen = screen
        pygame.draw.rect(self.screen, self.tile_color, self.rect)

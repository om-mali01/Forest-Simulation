import pygame

class Tile:
    def __init__(self, x, y, tile_width, tile_height, tile_color, age, max_age, max_height, height, tree_species, stats, alive=False) -> None:
        self.x = x
        self.y = y
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.tile_color = tile_color
        self.age = age
        self.max_age = max_age
        self.max_height = max_height
        self.height = height
        self.stats = stats
        self.alive = alive
        self.temperature = tree_species["temperature range"]
        self.ph =tree_species["pH range"]
        self.growth_rate = tree_species["growth rate"]
        self.moisture = tree_species["water/moisture range"]
        self.sunlight_intensity = tree_species["sunlight intensity range"]
        self.soil_nutrients = tree_species["soil nutrients range"]
        self.rect = pygame.Rect(x, y, tile_width, tile_height)
    
    def grow(self, forest_temp, soil_ph, forest_moisture, forest_sunlight_intensity, forest_soil_nutrients) -> None:
        '''when the tree cross the age limit ie.max_age it will die
            if the max age is 10 then at 11th it will die'''
        if self.tile_color == (128, 128, 128):
            return
        elif self.age < self.max_age:
            self.age += 1

        # "temperature range": [15, 30]        // temp in celsius
        # "water/moisture range": [40, 60]     // Percentage
        # "sunlight intensity range": [70, 100] // Percentage
        # "soil nutrients range": [60, 80]      // Percentage

            favorable_temperature = self.temperature[0] < forest_temp < self.temperature[1]
            favorable_moisture = self.moisture[0] < forest_moisture < self.moisture[1]
            favorable_ph = self.ph[0] < soil_ph < self.ph[1]
            favorable_sunlight_intensity = self.sunlight_intensity[0] < forest_sunlight_intensity < self.sunlight_intensity[1]
            favorable_soil_nutrients = self.soil_nutrients[0] < forest_soil_nutrients < self.soil_nutrients[1]

            if (favorable_temperature and favorable_ph
                and favorable_moisture and favorable_sunlight_intensity 
                and favorable_soil_nutrients):
                self.height += self.growth_rate+[self.growth_rate*0.25]
            else:
                if self.growth_rate > 0:
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

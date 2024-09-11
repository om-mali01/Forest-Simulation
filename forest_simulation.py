import random
from tile import Tile
import json

class Forest:
    def __init__(self, num_trees, rows, columns, max_age, max_height, tile_width, tile_height, forest_temperature, soil_ph, moisture, sunlight_intensity, soil_nutrients, tree_data, stats) -> None:
        self.num_trees = num_trees
        self.rows = rows
        self.columns = columns
        self.max_age = max_age
        self.max_height = max_height
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.forest_temperature = forest_temperature
        self.soil_ph = soil_ph
        self.moisture = moisture
        self.sunlight_intensity = sunlight_intensity
        self.soil_nutrients = soil_nutrients
        self.tree_data = tree_data
        self.stats = stats
        self.forest = self.create_empty_forest()
        self.place_trees_randomly()
        self.sim_data = []

    def create_empty_forest(self):
        forest = []
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                x = j * self.tile_width
                y = i * self.tile_height
                tree_species = random.choice(self.tree_data)
                tile = Tile(x, y, self.tile_width, self.tile_height, (139, 69, 19), 0, self.max_age, self.max_height, 0, tree_species, self.stats, False)  #brown (139, 69, 19)
                row.append(tile)
            forest.append(row)
        return forest
    
    def place_trees_randomly(self):
        while self.num_trees > 0:
            x = random.randint(0, self.rows-1)
            y = random.randint(0, self.columns-1)
            if not self.forest[x][y].alive:
                # if the age generates max_age (eg.10) (initial state), when the sim starts, max_age tree will be at dead state
                # so to avoid this generation of age should be less than max_age (1, self.max_age-1)
                tree_species = random.choice(self.tree_data)
                age = random.randint(1, self.max_age-2)
                self.forest[x][y].tile_color = (0, 250 - 20*age, 0)  #green
                alive = True
                self.forest[x][y].age = age
                self.forest[x][y].height = age*tree_species["growth rate"]
                self.forest[x][y].tree_species = tree_species
                self.forest[x][y].alive = alive
                self.num_trees -= 1

    def check_boundary(self, x, y):
        if 0 <= x < self.rows and 0 <= y < self.columns:    #!!!!
            neighbor_tile = self.forest[x][y]
            if neighbor_tile.height >= self.max_height:
                return False
        return True

    def run_sim(self) -> None:
        for i in range(self.rows):
            for j in range(self.columns):
                tile = self.forest[i][j]

                if tile.alive:
                    self.stats.steps()
                    self.stats.total_tree_ages(tile.age)             
                    self.stats.total_tree_height(tile.height)
                if tile.age == 1:
                    self.stats.increment_tree_count()     #count the total number of trees
                if tile.height == self.max_height:
                    tile.grow(self.forest_temperature, self.soil_ph, self.moisture, self.sunlight_intensity, self.soil_nutrients)
                    continue

                # -ve part/axis
                # Top
                x = i
                y = j - 1
                # if self.check_boundary == False then continue
                if not self.check_boundary(x, y):
                    continue
                
                # left
                x = i - 1
                y = j
                if not self.check_boundary(x, y):
                    continue

                # +ve part 
                # right
                x = i + 1
                y = j
                if not self.check_boundary(x, y):
                    continue
                
                # Bottom
                x = i
                y = j + 1
                if not self.check_boundary(x, y):
                    continue

                # check diagonally
                # Top-left
                x = i - 1
                y = j - 1
                if not self.check_boundary(x, y):
                    continue

                # Top-right
                x = i + 1
                y = j - 1
                if not self.check_boundary(x, y):
                    continue
                
                # Bottom-right
                x = i + 1
                y = j + 1
                if not self.check_boundary(x, y):
                    continue
                
                # Bottom-left
                x = i - 1
                y = j + 1
                if not self.check_boundary(x, y):
                    continue

                tile.grow(self.forest_temperature, self.soil_ph, self.moisture, self.sunlight_intensity, self.soil_nutrients)

        data = self.stats.report()
        self.sim_data.append(data)

        with open('data.json', 'w') as file:
            json.dump(self.sim_data, file, indent=4)

    def print_forest(self):
        for row in self.forest:
            for tree in row:
                print(f"{tree.age} ", end=" ")
            print()
        print()

    def draw(self, screen):
        for row in self.forest:
            for tile in row:
                tile.draw_tile(screen)
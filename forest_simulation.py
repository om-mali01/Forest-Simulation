import random
from tile import Tile

class Forest:
    def __init__(self, num_trees, rows, colums, max_age, tile_width, tile_height) -> None:
        self.num_trees = num_trees
        self.rows = rows
        self.colums = colums
        self.max_age = max_age
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.forest = self.create_empty_forest()
        self.place_trees_randomly()

    def create_empty_forest(self):
        forest = []
        for i in range(self.rows):
            row = []
            for j in range(self.colums):
                x = j * self.tile_width
                y = i * self.tile_height
                tile = Tile(x, y, self.tile_width, self.tile_height, (139, 69, 19), 0, False)
                row.append(tile)
            forest.append(row)
        return forest
    
    def place_trees_randomly(self):
        while self.num_trees > 0:
            x = random.randint(0, self.rows-1)
            y = random.randint(0, self.colums-1)
            if not self.forest[x][y].alive:
                age = random.randint(0, self.max_age)
                alive = True if age <= 10 else False
                color = (0, 128, 0) if alive else (139, 69, 19)
                self.forest[x][y].age = age 
                self.forest[x][y].tile_color = color
                self.forest[x][y].alive = alive
                self.num_trees -= 1

    def run_sim(self) -> None:
        for row in self.forest:
            for tile in row:
                if tile.alive:
                    tile.grow()

    def draw(self, screen):
        for row in self.forest:
            for tile in row:
                tile.draw_tile(screen)
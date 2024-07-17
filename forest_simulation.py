import random
from tile import Tile

class Forest:
    def __init__(self, num_trees, rows, columns, max_age, tile_width, tile_height) -> None:
        self.num_trees = num_trees
        self.rows = rows
        self.columns = columns
        self.max_age = max_age
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.forest = self.create_empty_forest()
        self.place_trees_randomly()

    def create_empty_forest(self):
        forest = []
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                x = j * self.tile_width
                y = i * self.tile_height
                tile = Tile(x, y, self.tile_width, self.tile_height, (139, 69, 19), 0, False)
                row.append(tile)
            forest.append(row)
        return forest
    
    def place_trees_randomly(self):
        while self.num_trees > 0:
            x = random.randint(0, self.rows-1)
            y = random.randint(0, self.columns-1)
            if not self.forest[x][y].alive:
                age = random.randint(0, self.max_age)
                alive = True
                color = (0, 200, 0)
                self.forest[x][y].age = age 
                self.forest[x][y].tile_color = color
                self.forest[x][y].alive = alive
                self.num_trees -= 1

    def check_boundary(self, x, y):
        if 0 <= x < self.rows and 0 <= y < self.columns:
            if self.forest[x][y].age >= self.max_age:
                return False
        return True

    def run_sim(self) -> None:
        for i in range(self.rows):
            for j in range(self.columns):
                tile = self.forest[i][j]
                
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

                tile.grow()

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
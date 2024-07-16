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

    # def sunlight_effect(self, i, j):
    #     # -ve part/axis

    #     # upper side 
    #     up_x = i
    #     up_y = j - 1
    #     if up_y >= 0:
    #         if self.forest[up_x][up_y].age >= self.max_age:
    #             False
        
    #     # left side 
    #     left_x = i - 1
    #     left_y = j
    #     if left_x >= 0:
    #         if self.forest[left_x][left_y].age >= self.max_age:
    #             False

    #     # +ve part 

    #     # right side 
    #     right_x = i + 1
    #     right_y = j
    #     if right_x < self.columns:
    #         if self.forest[right_x][right_y].age >= self.max_age:
    #             False
        
    #     # down side 
    #     down_x = i
    #     down_y = j + 1
    #     if down_y < self.rows:
    #         if self.forest[down_x][down_y].age >= self.max_age:
    #             False

    #     If none of the neighboring trees block sunlight, return True   
    #     return True

    def run_sim(self) -> None:
        for i in range(self.rows):
            for j in range(self.columns):
                tile = self.forest[i][j]
                
                # -ve part/axis

                # upper side 
                up_x = i
                up_y = j - 1
                if up_y >= 0:
                    if self.forest[up_x][up_y].age >= self.max_age:
                        continue
                
                # left side 
                left_x = i - 1
                left_y = j
                if left_x >= 0:
                    if self.forest[left_x][left_y].age >= self.max_age:
                        continue

                # +ve part 

                # right side 
                right_x = i + 1
                right_y = j
                if right_x < self.columns:
                    if self.forest[right_x][right_y].age >= self.max_age:
                        continue
                
                # down side 
                down_x = i
                down_y = j + 1
                if down_y < self.rows:
                    if self.forest[down_x][down_y].age >= self.max_age:
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
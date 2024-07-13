# create 
import pygame
import random
import sys

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

def main():
    pygame.init()

    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    num_trees = 50
    rows = 10
    colums = 10
    max_age = 10
    tile_width = screen_width//colums
    tile_height = screen_height//rows

    # obj of the forest
    forest = Forest(num_trees, rows, colums, max_age, tile_width, tile_height)

    step = 0
    max_step = 5 #number of times sim will run

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not step < max_step:
            break  #try agian without break !!!
        forest.run_sim()
        step += 1
            
        screen.fill((255, 255, 255))
        forest.draw(screen)
        pygame.display.flip()
        clock.tick(1)

    pygame.quit()
    sys.exit()

main()
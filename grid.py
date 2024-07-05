from tile import Tile
import pygame, sys

class Grid:
    def __init__(self, num_colums, num_rows, tile_width, tile_height, tile_color, screen) -> None:
        self.num_colums = num_colums
        self.num_rows = num_rows
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.tile_color = tile_color
        self.screen = screen
        self.tiles = []  #list to hold the tile object for grid

        for i in range(num_rows):
            row = []
            for j in range(num_colums):
                x = j * self.tile_width
                y = i * self.tile_height
                tile = Tile(x, y, self.tile_width, self.tile_height, self.tile_color)
                row.append(tile)
            self.tiles.append(row)

    def draw(self):
        """draw all tiles in grid"""
        for row in self.tiles:
            for tile in row:
                tile.draw_tile(self.screen)

    def run_loop(self):
        """Main loop for running the grid display"""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((255, 255, 255))
            self.draw() #draw the grid
            pygame.display.flip()

        pygame.quit()
        sys.exit()

def main():
    
    pygame.init()

    screen_width = 600
    screen_height = 600
    tile_color = (0, 0, 0) #black

    screen = pygame.display.set_mode((screen_width, screen_height))
    
    num_rows = 5
    num_colums = 5
    tile_width = screen_width // num_colums
    tile_height = screen_height // num_rows

    grid = Grid(num_colums, num_rows, tile_width, tile_height, tile_color, screen)

    grid.run_loop()

main()



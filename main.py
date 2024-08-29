import pygame, sys
from forest_simulation import Forest
from stats import Stats
import json

def main():
    pygame.init()

    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    num_trees = 50
    rows = 10
    columns = 10
    max_age = 10
    max_height = 10
    tile_width = screen_width//columns
    tile_height = screen_height//rows

    forest_temperature = 15
    soil_ph = 5.6

    with open('tree_species.json', 'r') as file:
        data = json.load(file)

    stats = Stats()
    
    # obj of the forest
    forest = Forest(num_trees, rows, columns, max_age, max_height, tile_width, tile_height, forest_temperature, soil_ph, data, stats)

    step = 0
    max_step = 7 #number of times sim will run

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if step < max_step:
            # running = False
            forest.run_sim()
            step += 1
            # forest.print_forest()
        forest.draw(screen)
        pygame.display.flip()
        clock.tick(2)
    # print(stats.report())
    print("Year wise data has been added to the data.json file..")
    pygame.quit()
    sys.exit()

main()
import pygame, sys
from forest_simulation import Forest

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
            running = False
        forest.run_sim()
        step += 1
        print(step)
            
        forest.draw(screen)
        pygame.display.flip()
        clock.tick(1)

    pygame.quit()
    sys.exit()

main()
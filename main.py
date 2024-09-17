import pygame, sys
from forest_simulation import Forest
from stats import Stats
import json
import data_visualization
from Input_box import InputBox
from forest_legend import Forest_legend

def main():

    pygame.init()

    black = (0, 0, 0)
    red = (250, 0, 0)
    white = (250, 250, 250)
    active_color = red
    inactive_color = black
    base_font = pygame.font.Font(None, 20)
    title_font = pygame.font.Font(None, 25)

    screen = pygame.display.set_mode((1000, 500), pygame.RESIZABLE)

    pygame.display.flip()

    boxes = [
        InputBox(600, 50, 200, 25, "Number of Trees (0-100)", inactive_color,base_font, black),
        InputBox(600, 100, 200, 25, "Forest temperature (Celsius)", inactive_color,base_font, black),
        InputBox(600, 150, 200, 25, "Soil pH (0-7)", inactive_color,base_font, black),
        InputBox(600, 200, 200, 25, "Moisture (0-100%)", inactive_color,base_font, black),
        InputBox(600, 250, 200, 25, "Sunlight Intensity (0-100%)", inactive_color,base_font, black),
        InputBox(600, 300, 200, 25, "Soil Nutrients (0-100%)", inactive_color,base_font, black)
    ]

    num_trees, forest_temperature, soil_ph, moisture, sunlight_intensity, soil_nutrients = 0, 0, 0, 0, 0, 0
    running = True


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                num_trees = boxes[0].get_values()
                forest_temperature = boxes[1].get_values()
                soil_ph = boxes[2].get_values()
                moisture = boxes[3].get_values()
                sunlight_intensity = boxes[4].get_values()
                soil_nutrients = boxes[5].get_values()
                running = False

            for box in boxes:
                box.event_handel(event, active_color, inactive_color, black, base_font)
            
        screen.fill(white)

        # border and title for the input box 
        InputBox.create_labeled_rect(screen, black, (550, 2), "Forest Growth Factors", title_font, 400, 330) 

        Forest_legend(screen)

        for box in boxes:
            box.draw(screen, base_font, black)

        pygame.display.flip()

    # -------------Forest Sim-------------------
    # forest area 
    columns = 10
    rows = 10
    max_age = 10
    max_height = 10

    forest_width = 500
    forest_height = 500

    clock = pygame.time.Clock()

    tile_width = forest_width // columns
    tile_height = forest_height // rows

    with open("tree_species.json", "r") as file:
        data = json.load(file)

    stats = Stats()

    # obj of the forest
    forest = Forest(
        num_trees,
        rows,
        columns,
        max_age,
        max_height,
        tile_width,
        tile_height,
        forest_temperature,
        soil_ph,
        moisture,
        sunlight_intensity,
        soil_nutrients,
        data,
        stats,
    )

    step = 0
    max_step = 7  # number of times sim will run

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if step < max_step:
            # running = False
            forest.run_sim()
            step += 1

        forest.draw(screen)

        pygame.display.flip()
        clock.tick(2)

    # Visualize the final data
    data_visualization.visualize_data()
    print("Year wise data has been added to the data.json file..")
    pygame.quit()
    sys.exit()

main()
# general count for taking avg
simulation_steps = 0
def increment_sim_steps():
    global simulation_steps
    simulation_steps += 1

# Tree count
total_trees_planted = 0
def increment_total_trees_planted():
    global total_trees_planted
    total_trees_planted += 1

total_dead_trees = 0
def increment_total_dead_trees():
    global total_dead_trees
    total_dead_trees += 1

# Age data
max_tree_age = 0
def update_max_age_tree(age):
    global max_tree_age
    max_tree_age = max(max_tree_age, age)

total_tree_ages = 0
def add_tree_age(age):
    global total_tree_ages
    total_tree_ages += age

# Height data
max_tree_height = 0
def update_max_height_tree(height):
    global max_tree_height
    max_tree_height = max(max_tree_height, height)

total_tree_height = 0
def add_tree_height(height):
    global total_tree_height
    total_tree_height += height

def report():
    avg_age = round((total_tree_ages/simulation_steps), 2)
    avg_height = round((total_tree_height/simulation_steps), 2)
    data = {
        print(f"Total trees: {total_trees_planted}"),
        print(f"Total dead trees: {total_dead_trees}"),
        print(f"max age of tree: {max_tree_age} years"),
        print(f"avg age: {avg_age} years"),
        print(f"max height of tree: {max_tree_height} feet"),
        print(f"avg height of tree: {avg_height} feet")
    }
    return data

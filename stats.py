count = 0
def simpleCount():
    global count
    count += 1

total_trees = 0
def countTotalTrees():
    global total_trees
    total_trees += 1

dead_trees = 0
def countDeadTrees():
    global dead_trees
    dead_trees += 1

# age data
max_age = 0
def max_age_tree(age):
    global max_age
    max_age = max(max_age, age)

total_ages = 0
def total_count_ages(age):
    global total_ages
    total_ages += age

# height data
max_height = 0
def max_height_tree(height):
    global max_height
    max_height = max(max_height, height)

total_height = 0
def total_count_height(height):
    global total_height
    total_height += height

def report():
    avg_age = round((total_ages/count), 2)
    avg_height = round((total_height/count), 2)
    data = {
        print(f"Total trees: {total_trees}"),
        print(f"Total dead trees: {dead_trees}"),
        print(f"max age of tree: {max_age} years"),
        print(f"avg age: {avg_age} years"),
        print(f"max height of tree: {max_height} feet"),
        print(f"avg height of tree: {avg_height} feet")
    }
    return data

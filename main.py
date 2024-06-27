import random

NUM_TREES = 20
forest_size = 10

class Tree:
    def __init__(self, age=0, alive=True):
        self.age = age
        self.alive = alive

    def grow(self):
        self.age += 1
        if self.age > 10:
            self.alive = False

def twoDiForest(forest_size):
    # forest_size = 10
    forest = []
    for _ in range(forest_size):
        row = []
        for _ in range(forest_size):
            row.append(None)
        forest.append(row)
    return forest

def place_trees_randomly(forest, max_age=5):
    x = random.randint(0, forest_size-1)
    y = random.randint(0, forest_size-1)
    if forest[x][y] is None:
        age = random.randint(0, max_age)
        alive = True if age <= 10 else False
        forest[x][y] = Tree(age, alive)

def initialize_forest(forest, NUM_TREES, max_age=5):
    for _ in range(NUM_TREES):
        place_trees_randomly(forest, max_age)

forest = twoDiForest(forest_size)
initialize_forest(forest, NUM_TREES)

def main():
    for step in range(10):
        for i in range(forest_size):
            for j in range(forest_size):
                if forest[i][j] is not None:
                    forest[i][j].grow()
                    if not forest[i][j].alive:
                        forest[i][j] = None

        # optional
        print(f"Step {step + 1}:")
        for row in forest:
            for tree in row:
                if tree is not None:
                    if tree.alive:
                        print(f'T{tree.age}', end='  ')
                else:
                    print('.', end='  ')
            print()
        print()

if __name__ == "__main__":
    main()
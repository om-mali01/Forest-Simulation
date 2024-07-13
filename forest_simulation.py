import random
from tree import Tree

class ForestSimulation:
    def __init__(self, forest_size: int, num_trees: int, max_age: int) -> None:
        self.forest_size = forest_size
        self.num_trees = num_trees
        self.max_age = max_age
        self.forest = self.create_2d_list()
        self.initialize_forest()

    def create_2d_list(self):
        forest = []
        for _ in range(self.forest_size):
            row = []
            for _ in range(self.forest_size):
                row.append(None)
            forest.append(row)
        return forest

    def place_trees_randomly(self) -> None:
        x = random.randint(0, self.forest_size-1)
        y = random.randint(0, self.forest_size-1)
        if self.forest[x][y] is None:
            age = random.randint(0, self.max_age)
            alive = True if age <= 10 else False
            self.forest[x][y] = Tree(age, alive)

    def initialize_forest(self) -> None:
        for _ in range(self.num_trees):
            self.place_trees_randomly()

    def run_sim(self) -> None:
        for i in range(self.forest_size):
            for j in range(self.forest_size):
                if not self.forest[i][j]:
                    continue
                self.forest[i][j].grow()
                if not self.forest[i][j].alive:
                    self.forest[i][j] = None

    def print_forest(self):
        print(self.forest)
        # for row in self.forest:
        #     for tree in row:
        #         if not tree:
        #             print('.', end=' ')
        #             continue
        #         print(f'T{tree.age}', end=' ')
        #     print()
        # print()

    # def print_forest(self, step: int) -> None:
    #     print(f"Step {step + 1}:")
    #     for row in self.forest:
    #         for tree in row:
    #             if not tree:
    #                 print('.', end='  ')
    #                 continue
    #             print(f'T{tree.age}', end='  ')
    #         print()
    #     print()
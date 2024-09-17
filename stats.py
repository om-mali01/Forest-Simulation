class Stats:
    def __init__(self) -> None:
        self.sim_steps = 0
        self.tree_count = 0
        self.total_dead_trees = 0
        self.max_age_tree = 0
        self.total_ages_trees = 0
        self.max_height_tree = 0
        self.total_height_trees = 0

    def steps(self):
        self.sim_steps += 1

    def increment_tree_count(self):
        self.tree_count += 1

    def increment_dead_trees(self):
        self.total_dead_trees += 1

    def update_max_age_tree(self, age):
        self.max_age_tree = max(self.max_age_tree, age)

    def total_tree_ages(self, age):
        self.total_ages_trees += age

    def update_max_height_tree(self, height):
        self.max_height_tree = max(self.max_height_tree, height)

    def total_tree_height(self, height):
        self.total_height_trees += height

    def report(self):
        if self.sim_steps == 0:
            avg_age = 0
            avg_height = 0
        else:
            avg_age = round((self.total_ages_trees / self.sim_steps), 2)
            avg_height = round((self.total_height_trees / self.sim_steps), 2)

        data = {
            "total_trees": self.tree_count,
            "total_dead_trees": self.total_dead_trees,
            "max_age_of_tree": self.max_age_tree,
            "avg_age_of_tree": avg_age,
            "max_height_of_tree": self.max_height_tree,
            "avg_height_of_tree": avg_height
        }
        return data

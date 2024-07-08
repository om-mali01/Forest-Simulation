from forest_simulation import ForestSimulation

def main():
    forest_size: int = 10
    num_trees: int = 10
    max_age: int = 2
    steps: int = 10

    sim: ForestSimulation = ForestSimulation(forest_size, num_trees, max_age)

    # for step in range(steps):
    #     sim.run_sim()
    #     sim.print_forest(step)

    sim.print_forest()

if __name__ == "__main__":
    main()
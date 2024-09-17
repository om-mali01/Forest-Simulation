import matplotlib.pyplot as plt
import json
import numpy as np

def visualize_data():
    with open('data.json', 'r') as file:
        data = json.load(file)

    total_trees = [d["total_trees"] for d in data]
    total_dead_trees = [d["total_dead_trees"] for d in data]
    max_age = [d["max_age_of_tree"] for d in data]
    avg_age = [d["avg_age_of_tree"] for d in data]
    max_height = [d["max_height_of_tree"] for d in data]
    avg_height = [d["avg_height_of_tree"] for d in data]

    plt.plot(total_trees, color="red", linewidth=3, label="Total trees")
    plt.plot(total_dead_trees, color="green", linewidth=3, label="Total Dead Trees")
    plt.plot(max_age, color="blue", linewidth=3, label="Max Age")
    plt.plot(avg_age, color="black", linewidth=3, label="Avg Age")
    plt.plot(max_height, color="brown", linewidth=3, label="Max Height")
    plt.plot(avg_height, color="orange", linewidth=3, label="Avg Height")

    plt.grid()
    plt.xlabel("Year")
    plt.ylabel("Total Trees")
    plt.title('Total Trees Over Time')
    plt.legend(title="data")
    plt.show()

    # grouped bar 

    total_trees = [d["total_trees"] for d in data]
    total_dead_trees = [d["total_dead_trees"] for d in data]
    width = 0.4

    bar1 = np.arange(len(total_trees))
    bar2 = [i+width for i in bar1]

    plt.bar(bar1, total_trees, width, label="Total Trees")
    plt.bar(bar2, total_dead_trees, width, label="Total Dead Trees")

    plt.xlabel("Year")
    plt.ylabel("Total Trees")
    plt.xticks(bar1+width/2)
    plt.title('Total Trees Over Time')
    plt.legend()
    plt.show()

# visualize_data()
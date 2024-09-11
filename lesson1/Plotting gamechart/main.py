from lesson1.ParsingData.task import parse_dataset
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":

    platforms = ["PS4", "XOne", "PC", "WiiU"]
    game_genres = ["Action", "Adventure", "Fighting", "Misc", "Platform", "Puzzle", "Racing", "Role-Playing", "Shooter",
                   "Simulation", "Sports", "Strategy"]

    gamesCounters = parse_dataset("dataset.csv")

    single_bar_width = 0.25
    bar_padding = 1
    all_bar_width = single_bar_width * len(game_genres) + bar_padding

    bar_positions = np.zeros((len(game_genres), len(platforms)))

    #example of plt.bar
    plt.bar([1,2,3,4],[1,4,9,16],width=single_bar_width, edgecolor='grey', label="example values")

    # writing bar positions
    for genreIndex in range(len(game_genres)):  # looping through genres
        for platformsIndex in range(len(platforms)):  # looping through platforms
            bar_positions[genreIndex, platformsIndex] = platformsIndex * all_bar_width + genreIndex * single_bar_width

    # setting up bar for every game genres
    for i, genre in enumerate(game_genres):  # loop through genres
        plt.bar(bar_positions[i], gamesCounters[i], width=single_bar_width, edgecolor='grey', label=genre)

    # setting up labels
    plt.xlabel('Platform', fontweight='bold', fontsize=15)
    plt.ylabel('Count', fontweight='bold', fontsize=15)

    # setting up sub-labels with platform names
    plt.xticks([i * all_bar_width for i in range(len(platforms))],
               platforms)

    plt.legend()  # showing legend
    plt.show()  # showing the result
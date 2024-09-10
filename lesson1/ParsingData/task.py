# todo: replace this with an actual task
import numpy as np
import pandas as pd


def parseDataset():
    platforms = ["PS4", "XOne", "PC", "WiiU"]
    game_genres = ["Action", "Adventure", "Fighting", "Misc", "Platform", "Puzzle", "Racing", "Role-Playing", "Shooter",
                  "Simulation", "Sports", "Strategy"]
    games_counters = np.zeros((len(game_genres), len(platforms)))

    games = pd.read_csv("dataset.csv")  # reading dataset.csv
    games = games[
        games["platform"].isin(platforms)]  # selecting only rows where platform column is in list of platforms

    for platformIndex, platform in enumerate(platforms):  # loops through platforms
        games_on_platform = games[games["platform"] == platform]
        for genreIndex, genre in enumerate(game_genres):  # loops through game_genres
            # Counts amount of rows, which satisfy condition
            games_counters[genreIndex, platformIndex] = len(games_on_platform[games_on_platform["genre"] == genre])
    return games_counters

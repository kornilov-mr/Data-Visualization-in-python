import numpy as np
import pandas as pd


def solution():
    return parse_dataset("dataset.csv")


def parse_dataset(path_to_dataset):
    platforms = ["PS4", "XOne", "PC", "WiiU"]
    game_genres = ["Action", "Adventure", "Fighting", "Misc", "Platform", "Puzzle", "Racing", "Role-Playing", "Shooter",
                   "Simulation", "Sports", "Strategy"]
    games_counters = np.zeros((len(game_genres), len(platforms)))  # creates 2d array with zeros with shape (12,4)

    games = pd.read_csv(path_to_dataset)  # reading dataset.csv
    games = games[
        games["platform"].isin(platforms)]  # selecting only rows where platform column is in list of platforms

    for platformIndex, platform in enumerate(platforms):  # loops through platforms
        games_on_platform = games[games["platform"] == platform]
        for genreIndex, genre in enumerate(game_genres):  # loops through game_genres
            # Counts amount of rows, which satisfy condition
            games_counters[genreIndex, platformIndex] = len(games_on_platform[games_on_platform["genre"] == genre])
    return games_counters


Task is to extract information from **dataset.csv** about amount of games of given genres in each given platform
<code>platforms = ["PS4", "XOne", "PC", "WiiU"] </code> <br>
<code>gameGenres = ["Action", "Adventure", "Fighting", "Misc", "Platform", "Puzzle", "Racing", "Role-Playing", "Shooter",
                  "Simulation", "Sports", "Strategy"]</code>

Answer should be in 2d Array where i axis is genres and j axis is platforms <br>
For example:
<pre>
  PS4,XOne,  PC, WiiU
[[148.  81.  39.  35.]  #Amount of Action games 
 [ 28.  14.   8.   3.]  #Amount of Adventure games
 [ 17.   5.   2.   2.]  #Amount of Fighting games
 [ 19.  17.   3.  13.]  #Amount of Adventure games
 [  9.   4.   1.   7.]  #Amount of Misc games
 [  1.   0.   0.   3.]  #Amount of Platform games
 [ 18.  18.  13.   1.]  #Amount of Puzzle games
 [ 52.  14.  18.   4.]  #Amount of Racing games
 [ 38.  36.  21.   3.]  #Amount of Role-Playing games
 [  6.   3.  18.   0.]  #Amount of Shooter games
 [ 42.  34.  11.   2.]  #Amount of Simulation games
 [  5.   2.  17.   0.]] #Amount of Sports games</pre>
<div class="hint">
    You can select only given platform with pandas using Dataframe.isin() <br>
    <code> games = games[games["platform"].isin(platforms)] </code>
</div>

<div class="hint">
    You can count rows which contain given genre using Pandas boolean indexing and len() <br>
    <code> len(games[games["genre"] == genre])</code>
</div>

Hint 3 is a complete solution

<div class="hint">
    
    games = pd.read_csv("dataset.csv")  # reading dataset.csv
    games = games[
        games["platform"].isin(platforms)]  # selecting only rows where platform column is in list of platforms

    for platformIndex, platform in enumerate(platforms):  # loops through platforms
        games_on_platform = games[games["platform"] == platform]
        for genreIndex, genre in enumerate(game_genres):  # loops through game_genres
            # Counts amount of rows, which satisfy condition
            games_counters[genreIndex, platformIndex] = len(games_on_platform[games_on_platform["genre"] == genre])

</div>



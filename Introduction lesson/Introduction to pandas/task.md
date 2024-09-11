
This paragraph consists of main **pandas** functions, 
which we will need later and also are used in almost any dataset parsing

<a href= "https://pandas.pydata.org/docs/user_guide/10min.html">10 minutes guide to pandas</a>

Basic data structures in **pandas**: <br>
**DataFrame**: a two-dimensional data structure that holds data like a two-dimension array or a table with rows and columns.

Main functions for this task:
- <code>pd.read_csv(path)</code> loads dataFrame. Main parameter is file path to dataset. <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html">docs</a>
  <br> use case <code>pd.read_csv("dataset.csv")</code>
- <code>DataFrame.isin(values)</code> selects all rows which have value specified in parameters <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isin.html">docs</a>
  <br> use case <code>games[games["platform"].isin(platforms)]</code>


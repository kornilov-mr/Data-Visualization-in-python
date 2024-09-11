
This paragraph consists of main **matplotlib.plot** functions, 
which we will need later and also are used in almost any plotting

<a href= "https://matplotlib.org/stable/users/explain/quick_start.html">Quick start matplotlib guide</a>

For this project we will use one of the most common plot types - bar plot

Main functions for this task:
- <code>matplotlib.pyplot.bar(heights, xCords, columnWidth)</code> makes bars on given x Coordinates with given height <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html">docs</a>
  <br> use case <code>plt.bar(barPositions, gamesCounters, width=0.25, edgecolor='grey', label="action")</code> <br>

- <code>plt.xlabel(name, font, fontSize)</code> draws text label on x-axis with given fontType and fontSize <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html">docs</a>
  <br> use case <code>plt.xlabel('Platform', fontweight='bold', fontsize=15)</code> <br>

- <code>plt.ylabel(name, font, fontSize)</code> draws text label on y-axis with given fontType and fontSize <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html">docs</a>
  <br> use case <code>plt.ylabel('Count', fontweight='bold', fontsize=15)</code>

- <code>plt.xticks(positions, labels)</code> draws text sub-label on x-axis with given x positions <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html">docs</a>
  <br> use case <code>plt.xticks([10,20], ["1964","1984"])</code>

- <code> plt.legend()</code> shows legend on end plot <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html">docs</a>
  <br> use case <code>plt.legend()</code>

- <code>plt.show()</code> shows final plot <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html">docs</a>
  <br> use case <code>plt.show()</code>

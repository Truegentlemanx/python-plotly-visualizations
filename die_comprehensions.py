import plotly.express as px

from die import Die

# Create two D6 Dice.
die_1 = Die()
die_2 = Die()


# Make some rolls and store results in a list using list comprehension.
results = [die_1.roll() * die_2.roll() for result in range(5000)]

# Analize the results.
max_result = die_1.num_sides * die_2.num_sides 
poss_results = range(3, max_result+1)
# Used a list comprehension.
frequencies = [results.count(value) for value in poss_results]

# Visualize the results.
title = "Results of multiplying rolls of two D6 Dice"
labels = {'x' : 'Result', 'y' : 'Frequency of Result' }
fig = px.bar(x = poss_results, y = frequencies, title=title, labels=labels)

# Further customize the chart.
fig.update_layout(xaxis_dtick=1)

fig.show()
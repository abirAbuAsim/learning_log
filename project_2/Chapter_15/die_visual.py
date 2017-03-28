import pygal
from die import Die 

# Create a D6
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll in range(1000):
	result = die.roll()
	results.append(result)

# Analyze the results
frequencies = []
for value in range(1, die.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
# hist.x_labels = ['1', '2', '3', '4', '5', '6']
# Using list comprehension for generating the x labels ;) 
hist.x_labels = [str(i) for i in range(1, 7)] 
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
import matplotlib.pyplot as plt 
from die import Die 

# Create a D6
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll in range(1000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

# Analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

# hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
# Using list comprehension for generating the x labels ;) 
y_items = range(2, max_result+1)
plt.bar(y_items, frequencies, color="green") 
plt.xticks([i+1 for i in range(1, max_result)])
plt.xlabel("Result") 
plt.ylabel("Frequency of Result")
plt.title("Results of rolling two D6 dice 1000 times.")

plt.savefig("dice_visual_using_matplotlib.png", bbox_inches='tight')
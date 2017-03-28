import matplotlib.pyplot as plt 

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values] # list comprehension

plt.scatter(x_values, y_values, c = y_values, cmap=plt.cm.Blues, 
	edgecolor='none', s = 40)

# Set the Chart title and label axes
plt.title("Square Number", fontsize = 24)
plt.xlabel("Values", fontsize = 14)
plt.ylabel("Square of Values", fontsize = 14)

# Set the size of tick labels
plt.tick_params(axis='both', labelsize = 14)

# Set the range for each axis
plt.axis([0, 1100, 0, 1100000])

plt.savefig('squares_plot.png', bbox_inches='tight')
import matplotlib.pyplot as plt 

input_values = [1, 2, 3, 4, 5]
squares = [x**2 for x in input_values]

plt.plot(input_values, squares, linewidth = 5)

# Set Chart title label axes
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Values", fontsize = 14)
plt.ylabel("Square of Values", fontsize = 14)

# Set size of tick labels
plt.tick_params(axis='both', labelsize = 14)

# Show the plot
plt.show()
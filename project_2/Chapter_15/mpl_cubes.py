import matplotlib.pyplot as plt 

input_values = list(range(1, 6))
cubes = [x**3 for x in input_values]

plt.plot(input_values, cubes, linewidth = 5)

# Set the Chart title and label axes
plt.title("Cube Numbers", fontsize = 24)
plt.xlabel("Values", fontsize = 14)
plt.ylabel("Cube of Values", fontsize = 14)

# Set the tick labels
plt.tick_params(axis='both', labelsize = 14)

plt.savefig('Cube_Plot.png', bbox_inches='tight')
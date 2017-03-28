import matplotlib.pyplot as plt 

from random_walk import RandomWalk 

# Keep making new walks, as long as the program is active.
while True:
	# Make a random walk, and plot the points.
	rw = RandomWalk(5000)
	rw.fill_walk()

	# Set the size of the plotting window.
	plt.figure(figsize=(10,6))

	point_numbers = list(range(rw.num_points))
	plt.plot(rw.x_values, rw.y_values, linewidth= 5)


	# Remove the axes.
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)

	plt.show()

	keep_running = raw_input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break
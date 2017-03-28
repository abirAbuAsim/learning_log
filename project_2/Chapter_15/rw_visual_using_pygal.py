import pygal

from random_walk import RandomWalk 

# Keep making new walks, as long as the program is active.
while True:
	# Make a random walk, and plot the points.
	rw = RandomWalk(500)
	rw.fill_walk()

	# Set the size of the plotting window.
	

	point_numbers = list(range(rw.num_points))
	# plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
	#			edgecolor='none', s = 1)
	xy_chart = pygal.XY(stroke=False)
	xy_chart.title = 'Correlation'
	xy_chart.add("", rw.x_values)
	# Emphasize the first and last points
	# plt.scatter(0, 0, c='green', edgecolor='none', s=100)
	# plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none',
	# 			 s=100)
	
	# Remove the axes.
	xy_chart.render_to_file("rw_visual_using_pygal.svg")


	keep_running = raw_input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break
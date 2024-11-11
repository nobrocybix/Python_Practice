import os
import pygal

from random_walk import RandomWalk

randw = RandomWalk()
basedir = os.path.dirname(__file__)

randw.fill_walk()

# Visualize the the results.
hist = pygal.Bar()


hist.title = "Random Walk in 5000 times"
hist.x_labels = [x for x in range(1, randw.num_points+1)]
hist.x_title = "Number of walk"
hist.y_title = "X values"

hist.add('X', randw.x_values)
hist.render_to_file(os.path.join(basedir, 'randomwalk.svg'))
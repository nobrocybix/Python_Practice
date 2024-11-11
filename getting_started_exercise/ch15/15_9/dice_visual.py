import os
import pygal

from die import Die

die_1 = Die()
die_2 = Die()

basedir = os.path.dirname(__file__)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)
    
# Look for possible results
num_result = set()
for n_die_1 in range(1, die_1.num_sides + 1):
    for n_die_2 in range(1, die_2.num_sides + 1):
        num_result.add(n_die_1 * n_die_2)
        
num_result = sorted(num_result)

# Analyze the results.
frequencies = []
for value in num_result:
    frequency = results.count(value)
    frequencies.append(frequency)

      
# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = [x for x in num_result]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 * D6', frequencies)
hist.render_to_file(os.path.join(basedir, 'dice_visual.svg'))

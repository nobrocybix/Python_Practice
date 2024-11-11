import os
import pygal

from die import Die

# Create two D6 dice.
die_1 = Die(8)
die_2 = Die(8)

basedir = os.path.dirname(__file__)

# Make some rolls, and store results in a list.
results = []

current_rolls = 1000
max_rolls = 100000000

try:
    while current_rolls < max_rolls:
        for roll_num in range(current_rolls):
            result = die_1.roll() + die_2.roll()
            results.append(result)
        
        current_rolls *= 2
        print(f"已完成 {current_rolls} 次擲骰子...")

except MemoryError:      
        print("System overloaded! Stopping the simulation.")
except Exception as e:
    print(f"發生錯誤: {e}")
            

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)  

      
# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = list(range(2, 17))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8 + D8', frequencies)
hist.render_to_file(os.path.join(basedir, 'dice_visual.svg'))

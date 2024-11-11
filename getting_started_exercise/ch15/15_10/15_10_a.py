import os

from die import Die
import die_functions as df
import matplotlib.pyplot as plt

die_1 = Die()
die_2 = Die()
basedir = os.path.dirname(__file__)

x_values = df.two_die_num_result(die_1, die_2)
y_values = df.two_die_multiply(die_1, die_2, 1000)

plt.plot(x_values, y_values, linewidth=5, color='green')

# Set chart title and label.
plt.title("Results of rolling two D6 dice 1000 times.", fontsize=14, color='red')
plt.xlabel("Result", fontsize=10, color='blue')
plt.ylabel("Frequency of Result", fontsize=10, color='blue')

plt.grid()

plt.tick_params(axis='both', labelsize=10)
plt.savefig(os.path.join(basedir, 'dies_plot.png'), bbox_inches='tight')

plt.show()
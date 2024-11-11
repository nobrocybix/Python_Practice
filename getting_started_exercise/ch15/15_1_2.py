import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [y**3 for y in x_values]

plt.scatter(x_values, y_values, c=(0, 0.8, 0), edgecolor='none', s=40)

# Set chart title, and label axes.
plt.title("Cube number", fontsize=20, c='green')
plt.xlabel("Value", fontsize=16, c='#e57e1d')
plt.ylabel("Cuble of Value", fontsize=16, c='#e57e1d')

# Set size of tick labels.
plt.tick_params(axis="both", which='major', labelsize=16,
                labelcolor='#2a21e5', color='#e57e1d')

plt.show()
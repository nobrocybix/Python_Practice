import matplotlib.pyplot as plt

x_values = list(range(1, 6))
y_values = [x**3 for x in x_values]

plt.plot(x_values, y_values, linewidth=8)

# Set chart title, and label axes.
plt.title("Cuble Numbers", fontsize=24, loc="left")
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', which='major',
                length=5, width=5, 
                color='red', labelcolor='green',
                labelsize=14)

plt.show()
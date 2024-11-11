import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [y**3 for y in x_values]

plt.scatter(x_values, y_values, c=x_values, cmap=plt.cm.Reds, 
            edgecolor='none', s=40)

# Set chart title, and label axes.
plt.title("Cube number", fontsize=20, c='red')
plt.xlabel("Value", fontsize=16)
plt.ylabel("Cuble of Value", fontsize=16)

# Set size of tick labels.
plt.tick_params(axis="both", which='major', labelsize=16)

plt.show()
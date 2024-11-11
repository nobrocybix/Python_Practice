import matplotlib.pyplot as plt
from random import randint

x_rand = []
y_rand = []

# Create random num x, y 
for n in range(5):   
    x_rand.append(randint(0, 99))

for n in range(5):
    y_rand.append(randint(0, 99))

x_rand.sort()
y_rand.sort()
plt.plot(x_rand, y_rand, color='green', linewidth=5)

# Set chart title and label axes.
plt.title("Random Numbers", fontsize=24, loc="left")
plt.xlabel("Random X", fontsize=14)
plt.ylabel("Random Y", fontsize=14)

# Set size of thick labels.
plt.tick_params(axis='both', labelsize=14, color='#a36153', labelcolor='#15e467')

plt.show()
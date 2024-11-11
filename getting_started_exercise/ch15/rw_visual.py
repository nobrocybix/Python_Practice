import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks. as long as the program is active.
keep_running = True
while keep_running:
    # Make a random walk, and plot the points.
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Set the size of the plotting window.
    plt.figure(dpi=128, figsize=(13, 7))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolor='none', s=1)
    
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
                s=100)

    # Remove the axes.
    ax = plt.gca()  # 獲取當前坐標軸
    ax.get_xaxis().set_visible(False)  # 隱藏 x 軸
    ax.get_yaxis().set_visible(False)  # 隱藏 y 軸

    plt.show()

    while True:
        running = input("Make another walk? (y/n)")
        if running.lower() == 'n':
            keep_running = False
            break
        if running.lower() == 'y':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
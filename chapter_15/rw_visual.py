import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk

rw = RandomWalk()
rw.fill_walk()
print(rw.num_points)

# Plot the points in the walk.

plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
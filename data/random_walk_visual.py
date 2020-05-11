import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()
plt.figure(dpi=128, figsize=(10, 6))
plt.scatter(rw.x_values, rw.y_values, s=0.1)
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.show()
# plt.savefig("random_walk.png")

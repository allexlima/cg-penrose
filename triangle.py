import numpy as np
import matplotlib.pyplot as plt

def vertices(a, b, c):
    return np.array([a, b, c])

fig, ax = plt.subplots()
ax.set_aspect("equal")

tr = plt.Polygon(np.array([a, b, c]))
ax.add_patch(tr)
ax.relim()
ax.autoscale_view()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
 # from mpl_toolkits.mplot3d import Axes3D

ax = plt.figure().gca(projection='3d')

t = np.arange(0.01, 16*np.pi, 0.01)

x = np.sin(2 * t)
y = 1 - np.cos(2 * t)
z = 2 * np.cos(t)

ax.plot(x, y, z)

plt.show()
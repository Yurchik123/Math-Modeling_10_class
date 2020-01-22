import numpy as np
import matplotlib.pyplot as plt
 # from mpl_toolkits.mplot3d import Axes3D

ax = plt.figure().gca(projection='3d')

t = np.arange(0.01, 16*np.pi, 0.01)
R = 5

x = R * np.sin(t)**3
y = R * np.cos(t)**3
z = np.cos(2 * t)

ax.plot(x, y, z)

plt.show()
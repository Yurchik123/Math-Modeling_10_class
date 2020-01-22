import numpy as np
import matplotlib.pyplot as plt
 # from mpl_toolkits.mplot3d import Axes3D

ax = plt.figure().gca(projection='3d')

t = np.arange(0.01, 16*np.pi, 0.01)

x = 2**(- 0.1 * t) * np.cos(t)
y = 2**(- 0.1 * t) * np.sin(t)
z = -t

ax.plot(x, y, z)

plt.show()
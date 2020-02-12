import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
import numpy as np

ax = p3.Axes3D(plt.figure())

phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0, 10 * np.pi, 100)
h = 100

x = np.outer(phi, np.cos(theta))
y = np.outer(phi, np.sin(theta))
z = h * np.outer(np.ones(np.size(phi)), theta)

ax.plot_surface(x, y, z)
plt.show()
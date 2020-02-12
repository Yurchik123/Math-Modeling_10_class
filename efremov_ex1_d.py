import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
import numpy as np

ax = p3.Axes3D(plt.figure())

phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(-2 * np.pi, 2 * np.pi, 100)
l = 1
m = 1
n = 1
x = np.outer(phi, np.cos(theta)) + l * np.cos(theta)
y = np.outer(phi, np.sin(theta)) + m * np.sin(theta)
z = n * np.outer(np.ones(np.size(phi)), np.sin(theta))

ax.plot_surface(x, y, z)
plt.show()
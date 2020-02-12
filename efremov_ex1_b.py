import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
import numpy as np

ax = p3.Axes3D(plt.figure())

phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(-2 * np.pi, 2 * np.pi, 100)
a = 4
b = 4
c = 10

x = a * np.outer(np.cos(phi), np.sinh(theta))
y = b * np.outer(np.sin(phi), np.sinh(theta))
z = c * np.outer(np.ones(np.size(phi)), np.sinh(theta))

ax.plot_surface(x, y, z)
plt.show()
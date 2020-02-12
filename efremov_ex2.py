import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

fig = plt.figure()
ax = p3.Axes3D(fig)


N = 100
phi = np.linspace(0, np.pi, N)
theta = np.linspace(0, np.pi, N)
h = 1

#x = np.outer(phi, np.cos(theta))
#y = np.outer(phi, np.sin(theta))
#z = h * np.outer(np.ones(np.size(phi)), theta)
x = np.outer(phi, np.cos(theta))
y = np.outer(phi, np.sin(theta))
z = np.outer(phi**2, np.ones(np.size(theta)))
ax.plot_surface(x, y, z)

phi1 = np.linspace(-np.pi, np.pi, N)

#x1 = phi * np.cos(theta)
#y1 = phi * np.sin(theta)
#z1 = h * theta + 1
x1 = phi1
y1 = np.zeros(np.size(phi1))
z1 = phi1**2

ball, = ax.plot(x1, y1, z1, 'o', color='r')
line, = ax.plot(x1, y1, z1, '-', color='r')

def animation_func(i):
    ball.set_data(x1[i], y1[i])
    ball.set_3d_properties(z1[i])
    
    line.set_data(x1[:i], y1[:i])
    line.set_3d_properties(z1[:i])

ax.set_xlim3d([-10, 10])
ax.set_ylim3d([-10, 10])
ax.set_zlim3d([-10, 10])

ani = animation.FuncAnimation(fig, animation_func, N, interval=50)
ani.save('ani.gif')
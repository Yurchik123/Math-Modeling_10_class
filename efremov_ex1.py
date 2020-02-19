import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
from matplotlib import animation

fig = plt.figure()
ax = p3.Axes3D(fig)

N = 200
t = np.linspace(0, 4 * np.pi, N)

def diff_func(s, t):
    x, v_x, y, v_y, z, v_z = s
    
    dxdt = v_x
    dv_xdt = x / a**2 * ( (g - (v_x**2 / a**2) - (v_y**2 / b**2) - (v_z**2 / c**2)) )
    
    dydt = v_y
    dv_ydt = y / b**2 * ( (g - (v_x**2 / a**2) - (v_y**2 / b**2) - (v_z**2 / c**2)) )
    
    dzdt = v_z
    dv_zdt = -g + x / a**2 * ( (g - (v_x**2 / a**2) - (v_y**2 / b**2) - (v_z**2 / c**2)) )
    
    return dxdt, dv_xdt, dydt, dv_ydt, dzdt, dv_zdt

x0 = 0
y0 = 0
z0 = 0

v_x0 = 3
v_y0 = 0
v_z0 = 0

a = 5
b = 5
c = 10

s0 = x0, v_x0, y0, v_y0, z0, v_z0

g = 9.8

sol = odeint(diff_func, s0, t)

ball, = ax.plot(sol[:, 0], sol[:, 2], sol[:, 0], 'o', color='r')
line, = ax.plot(sol[:, 0], sol[:, 2], sol[:, 0], '--', color='r')

def animation_func(i):
    ball.set_data(sol[i, 0], sol[i, 2])
    ball.set_3d_properties(sol[i, 4])
    
    line.set_data(sol[:i, 0], sol[:i, 2])
    line.set_3d_properties(sol[:i, 4])

# рисуем эллипсоид
phi = np.linspace(0, np.pi, N)
theta = np.linspace(-np.pi / 2, np.pi / 2, N)
x = a * np.outer(np.cos(phi), np.sin(theta))
y = b * np.outer(np.sin(phi), np.sin(theta))
z = c * np.outer(np.ones(np.size(phi)), np.cos(theta)) - c
ax.plot_surface(x, y, z, color='g')

ax.set_xlim3d([-10, 10])
ax.set_ylim3d([-10, 10])
ax.set_zlim3d([-10, 10])

ani = animation.FuncAnimation(fig, animation_func, N, interval=50)
ani.save('ani1.gif')
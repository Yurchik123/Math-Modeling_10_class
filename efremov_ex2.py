import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
from matplotlib import animation

fig = plt.figure()
ax = p3.Axes3D(fig)

N = 200
t = np.linspace(0, 10, N)

def diff_func(s, t):
    x, v_x, y, v_y, z, v_z = s
    ml = 3 * g * z / (z**2 + x**2) # множитель Лагранжа
    
    dxdt = v_x
    dv_xdt = ml * x
    
    dydt = v_y
    dv_ydt = 0
    
    dzdt = v_z
    dv_zdt = - g + ml * z
    
    return dxdt, dv_xdt, dydt, dv_ydt, dzdt, dv_zdt

x0 = 1
y0 = 0
z0 = 0

v_x0 = 0
v_y0 = 1
v_z0 = 0

g = 9.8
#k = 1
R = 1

s0 = x0, v_x0, y0, v_y0, z0, v_z0

sol = odeint(diff_func, s0, t)

ball, = ax.plot(sol[:, 0], sol[:, 2], sol[:, 0], 'o', color='r')
line, = ax.plot(sol[:, 0], sol[:, 2], sol[:, 0], '--', color='r')

def animation_func(i):
    ball.set_data(sol[i, 0], sol[i, 2])
    ball.set_3d_properties(sol[i, 4])
    
    line.set_data(sol[:i, 0], sol[:i, 2])
    line.set_3d_properties(sol[:i, 4])

# рисуем эллипсоид
theta = np.linspace(-np.pi, 0, N)

x = R * np.outer(np.ones(np.size(t)), np.cos(theta))
y = np.outer(t, np.ones(np.size(theta)))
z = R * np.outer(np.ones(np.size(t)), np.sin(theta))

ax.plot_surface(x, y, z, color='g')

ax.set_xlim3d([-5, 5])
ax.set_ylim3d([0, 5])
ax.set_zlim3d([-5, 5])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ani = animation.FuncAnimation(fig, animation_func, N, interval=50)
ani.save('ani3.gif')
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

ax = plt.figure().gca(projection='3d')

t = np.arange(10**(-7), 3*10**(-7), 10**(-11))

def diff_func(s, t):
    x, v_x, y, v_y, z, v_z = s
    
    dxdt = v_x
    dv_xdt = q/m * (Ex + v_y * Bz  - v_z * By) - (G*M) / ((x-xc)**2 + (y-yc)**2 + (z-zc)**2)**(1.5) * (x - xc)
    
    dydt = v_y
    dv_ydt = q/m * (Ey + v_z * Bx  - v_x * Bz) - (G*M) / ((x-xc)**2 + (y-yc)**2 + (z-zc)**2)**(1.5) * (y - yc)
    
    dzdt = v_z
    dv_zdt = q/m * (Ez + v_x * By  - v_y * Bx) - (G*M) / ((x-xc)**2 + (y-yc)**2 + (z-zc)**2)**(1.5) * (z - xc)
    
    return dxdt, dv_xdt, dydt, dv_ydt, dzdt, dv_zdt

x0 = 0
y0 = 0
z0 = 0

xc = 0.05
yc = 0.08
zc = 0

v_x0 = 10**7
v_y0 = 10**6
v_z0 = 0

s0 = x0, v_x0, y0, v_y0, z0, v_z0

m = 1.67 * 10**(-31)
q = 1.6 * 10**(-19)
G = 6.7 * 10**(-11)
M = 1.67 * 10**(23)

Ex = 0
Ey = 10**(-3)
Ez = 0

Bx = 0
By = 10**(-3)
Bz = 0

sol = odeint(diff_func, s0, t)

ax = plt.figure().gca(projection='3d')
ax.plot(sol[:, 0], sol[:, 2], sol[:, 4], label='Proton')

ax.quiver(x0, y0, z0, Bx, By, Bz,
          length=(0.005), normalize=True, color='r', label='B')
ax.quiver(x0, y0, z0, Ex, Ey, Ez,
          length=(0.005), normalize=True, color='b', label='E')
ax.quiver(x0, y0, z0, v_x0, v_y0, v_z0,
          length=(0.005), normalize=True, color='g', label='v')

plt.legend()
plt.show()
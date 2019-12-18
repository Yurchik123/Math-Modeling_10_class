#Задание 2.b
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.arange(0, 500, 0.01)
G = 6.67 * 10**(-11)
R = 6.371 * 10**6
M = 5.94 * 10**24
k = 0.1
m = 20

def diff_func(z, t):
    r, v = z
    dr_dt = v
    dv_dt = - G * M / r**2 - k/m * v
    return dr_dt, dv_dt

v0 = 13200 #начальная скорость
h0 = 1.5 #высота пушки
r0 = R + h0  #начальное расстояние от центра земли
z0 = r0, v0

sol = odeint(diff_func, z0, t)
plt.plot(t, sol[:, 0])
#plt.plot(sol[:, 1], sol[:, 0])
plt.show()
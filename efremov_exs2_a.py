#Задание 2.a
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.arange(0, 20, 0.01)
g = 9.8 #Ускорение свободного падения
l = 15 #Длина нити

def diff_func(z, t):
    s, v = z
    ds_dt = v
    dv_dt = -g * np.sin(s/l)
    return ds_dt, dv_dt

s0 = 5 #Нач отклонение
v0 = 5 #Нач. скорость
z0 = s0, v0

sol = odeint(diff_func, z0, t)
plt.plot(t, sol[:, 1])
plt.show()
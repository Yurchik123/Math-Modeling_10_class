import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation


t = np.arange(1, 500, 0.001)

def diff_func(s, t):
    (x1, v_x1, y1, v_y1,     
     x2, v_x2, y2, v_y2,     
     x3, v_x3, y3, v_y3) = s 
     
    dxdt1 = v_x1
    dv_xdt1 = (k * q1 * q2 / m1 *(x1 - x2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
              + k * q1 * q3 / m1 *(x1 - x3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5)
    dydt1 = v_y1
    dv_ydt1 = (k * q1 * q2 / m1 *(y1 - y2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
              + k * q1 * q3 / m1 *(y1 - y3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5)
    
    dxdt2 = v_x2
    dv_xdt2 = (k * q2 * q1 / m2 *(x2 - x1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
              + k * q2 * q3 / m2 *(x2 - x3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5)
    dydt2 = v_y2
    dv_ydt2 = (k * q2 * q1 / m2 *(y2 - y1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
              + k * q2 * q3 / m2 *(y2 - y3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5)
    
    dxdt3 = v_x3
    dv_xdt3 = (k * q3 * q1 / m3 *(x3 - x1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
              + k * q3 * q2 / m3 *(x3 - x2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5)
    dydt3 = v_y3
    dv_ydt3 = (k * q3 * q1 / m3 *(y3 - y1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
              + k * q3 * q2 / m3 *(y3 - y2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5)
    
    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,
            dxdt2, dv_xdt2, dydt2, dv_ydt2,
            dxdt3, dv_xdt3, dydt3, dv_ydt3)
     
k = 8.98755 * 10**9

m1 = 2 * 10**(-2)
m2 = 1 * 10**(-2)
m3 = 1.5 * 10**(-2)

q1 = 2.1 * 10**(-1)
q2 = 3.1 * 10**(-1)
q3 = - 1.1 * 10**(-1)

x10 = 0
v_x10 = 0.1
y10 = 0.5
v_y10 = 0

x20 = -0.4
v_x20 = 0.1
y20 = -0.3
v_y20 = 0

x30 = 0.4
v_x30 = 0
y30 = -0.3
v_y30 = 0.5

s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30)

sol = odeint(diff_func, s0, t)
plt.plot(sol[:, 0], sol[:, 2], '-',  color='b')
plt.plot(sol[:, 4], sol[:, 6], '-', color='r')
plt.plot(sol[:, 8], sol[:, 10], '-', color='g')
plt.show()

fig = plt.figure()
stars = []

for i in range(0, len(t), 1):
    star1, = plt.plot(sol[i, 0], sol[i, 2], 'o', color='b')
    star2, = plt.plot(sol[i, 4], sol[i, 6], 'o', color='r')
    star3, = plt.plot(sol[i, 8], sol[i, 10], 'o', color='g')
    stars.append([star1, star2, star3])

ani = ArtistAnimation(fig, stars, interval=50)
plt.axis('equal')
ani.save('ani.gif')
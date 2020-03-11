import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
from scipy.integrate import odeint

t = np.arange(0, 1, 0.01)


def diff_func(s, t):
    phi1, v_phi1, phi2, v_phi2 = s
    
    dphidt1 = v_phi1
    dv_phidt1 = -g*np.sin(phi2)/(l1*np.cos(phi1 - phi2)) + v_phi1*v_phi2*np.tan(phi1 - phi2) + v_phi1*np.tan(phi1- phi2)*v_phi1 - v_phi1*np.tan(phi1 - phi2)*v_phi2
    dphidt2 = v_phi2
    dv_phidt2 = (-g*m1*np.sin(phi1) - g*m2*np.sin(phi1) - l2*m2*v_phi1*v_phi2*np.sin(phi1 - phi2) + l2*m2*v_phi2*np.sin(phi1 - phi2)*v_phi1 - l2*m2*v_phi2*np.sin(phi1 - phi2)*v_phi2)/(l2*m2*np.cos(phi1 - phi2))
    return dphidt1, dv_phidt1, dphidt2, dv_phidt2

l1 = 1
l2 = 1
m1 = 2
m2 = 3
g = 9.8
v_phi10 = 0
v_phi20 = 0
phi10 = np.pi / 2
phi20 = np.pi / 2
s0 = phi10,  v_phi10, phi20,  v_phi20

sol = odeint(diff_func, s0, t)

x1 = l1 * np.sin(sol[:, 0])
y1 = - l1 * np.cos(sol[:, 0])

x2 = x1 + l2 * np.sin(sol[:, 2])
y2 = y1 - l2 * np.cos(sol[:, 2])


anim_list = []
fig = plt.figure()

for i in range(0, len(t), 1):
    tx = [0, x1[i], x2[i]]
    ty = [0, y1[i], y2[i]]
    maj, = plt.plot(tx, ty, '-o', color='b')
    anim_list.append([maj])

ani = ArtistAnimation(fig, anim_list, interval=50)

plt.axis('equal')
ani.save('ani.gif')
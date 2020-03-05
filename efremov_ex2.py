from sympy import *

L = Function('L')
phi = Function('phi')
t = Symbol('t')

l = Symbol('l')
m = Symbol('R')
R =Symbol('R')
omega = Symbol('omega')
g = Symbol('g')

v_phi = Function('v_phi')
L = m*l**2/2* v_phi(t)**2 + m*R*l*omega**2*cos(phi(t)-omega*t) + m*g*l*cos(phi(t))

diff_L_phi = diff(L, phi(t))
print(diff_L_phi)
print()

diff_L_v_phi = diff(diff(L, v_phi(t)),t)
print(diff_L_v_phi)
print()

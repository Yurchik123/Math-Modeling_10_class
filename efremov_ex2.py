#Задание 2
from math import tan, pi, sqrt, e, cos
from constants import *

H = 100
B = pi / 5
a = pi/3
v = sqrt( (g*H * (1/tan(B)**2)) / (2 * (cos(a))**2 * (1 - (1/tan(B)) * (1/tan(a)))) )
print(v, "м/с")

T = 200
E = 300
N = (2/sqrt(pi)) * (h / (k*T)**(3/2)) * (e**(((0-1) * E) / k*T)) * (e**(T/2))
print(N)
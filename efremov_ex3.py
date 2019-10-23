#Задание 3
from constants import *
from math import cos, sin
from numpy import ndarray, arange

x0 = 5
y0 = 3
v0 = 15

v0x = cos(v0)
v0y = sin(v0)

print("t        x       y")
t = arange(0, 5, 0.01)

tabl = ndarray(shape = (len(t) ,3))
for i in range(0, len(t)):
    x = x0 + v0x*t[i]
    y = y0 + v0y*t[i] - (g*(t[i]**2))/5
    
    tabl[i, 0] = t[i]
    tabl[i, 1] = x
    tabl[i, 2] = y
    
    print((tabl[i, 0]*100 // 1)/100, "  ", (tabl[i, 1]*100 // 1)/100, "  ", (tabl[i, 2]*100 // 1)/100)



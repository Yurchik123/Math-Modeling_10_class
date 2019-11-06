#Задание 2
import matplotlib.pyplot as plt
import numpy as np

def Giperbola(k=1):
    '''
    Рисование графика функции f(x) = 1/х (Гипербола)
    Отрисовка идёт по частям, сначала одна ветвь, а потом уже вторая
    '''
    x = np.arange(0.01, 10, 0.01)
    y = k/x
    plt.plot(x, y, color='g', label="f(x) = k/x")
    x = np.arange(-0.01, -10, -0.01)
    y = k/x
    plt.plot(x, y, color='g')


def Parabola(a=1, b=0, c=0):
    '''
    Рисование графика функции f(x) = ax2 + bx + c (Парабола)
    '''
    x = np.arange(-10, 10, 0.01)
    y = a*x**2 + b*x+ c
    plt.plot(x, y, color='b', label="f(x) = ax2 + bx + c")


Giperbola(1)
Parabola()

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Графики функций')
plt.grid()
plt.legend()
plt.show()
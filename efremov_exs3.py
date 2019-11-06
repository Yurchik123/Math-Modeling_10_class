#Задание 3
import matplotlib.pyplot as plt
import numpy as np

def Circle(R=1):
    '''
    Рисование гравика функции х2 + у2 = R
    (Окрудность)
    '''
    R = R**2
    x = np.arange(R * (-1) - 1, R + 1, 0.01)
    y = np.arange(R * (-1) - 1, R + 1, 0.01)
    X, Y = np.meshgrid(x, y)
    fxy = X**2 + Y**2
    plt.contour(X, Y, fxy, levels=[R])

def Elips(R=1, a=1, b=0.5):
    '''
        Рисование гравика функции х2/a2 + у2/b2 = R
        ("Элипс")
    '''
    R = R ** 2
    a = a**2
    b = b**2
    x = np.arange(R * (-1) - 1, R + 1, 0.01)
    y = np.arange(R * (-1) - 1, R + 1, 0.01)
    X, Y = np.meshgrid(x, y)
    fxy = (X ** 2)/a + (Y ** 2)/b
    plt.contour(X, Y, fxy, levels=[R])

Circle(2)
Elips(3)

plt.title('Гравики функций')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.show()
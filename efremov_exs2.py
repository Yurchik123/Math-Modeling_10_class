# Задание 2
from numpy import array
def mult(array=[0]):
    
    """
    Функция перемножает все элементы массива
    """
    
    out = 1
    for i in array:
        out *= i
    return out

a = [1, 2, 3, 4]
print(mult(array(a)))
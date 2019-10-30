# Задание 1
def leap(year=1):
    
    """
    Определение, високосный год или нет, по одному
    аргументу year
    """
    
    if (year%4 == 0) and (year%100 != 0) or (year%400 == 0):
        out = "Год високосный"
    else:
        out = "Год невисокосный"
    return out

print(leap(2000))
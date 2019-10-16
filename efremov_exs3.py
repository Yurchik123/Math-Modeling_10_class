print("-=-=-=Задание 3=-=-=-")
year = 1999
if (year%4 == 0) and (year%100 != 0) or (year%400 == 0):
    print("Год високосный")
else:
    print("Год невисокосный")
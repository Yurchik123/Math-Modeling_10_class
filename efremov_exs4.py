# Задание 4
def day(day=1, month=1, year=2000):
    
    """
    Определение дня недели по заданной дате ф вормате [D M YYYY]
    """
    
    year = year - (14 - month) // 12
    month = month + 12 * ((14 - month) // 12) - 2
    day_w = (day + (31 * month) // 12 + year + year // 4 - year // 100 + year // 400) % 7

    if day_w // 1== 0:
        out = "Воскресенье"
    elif day_w // 1== 1:
        out = "Понедельник"
    elif day_w // 1 == 2:
        out = "Вторник"
    elif day_w // 1 == 3:
        out = "Среда"
    elif day_w // 1 == 4:
        out = "Четверг"
    elif day_w // 1 == 5:
        out = "Пятница"
    elif day_w // 1 == 6:
        out = "Суббота"
        
    return out

print(day(12, 12, 2006))
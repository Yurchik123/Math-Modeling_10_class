day = 19
month = 1
year = 2004

a = (14 - month) // 12
year = year - a
month = month + 12 * a - 2
day_w = (day + (31 * month) // 12 + year + year // 4 - year // 100 + year // 400) % 7

if day_w // 1== 0:
    print("Воскресенье")
elif day_w // 1== 1:
    print("Понедельник")
elif day_w // 1 == 2:
    print("Вторник")
elif day_w // 1 == 3:
    print("Среда")
elif day_w // 1 == 4:
    print("Четверг")
elif day_w // 1 == 5:
    print("Пятница")
elif day_w // 1 == 6:
    print("Суббота")
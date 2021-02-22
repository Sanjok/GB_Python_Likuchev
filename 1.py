"""
1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
* до часа: <m> мин <s> сек;
* до суток: <h> час <m> мин <s> сек;
* *до месяца, до года, больше года: по аналогии.
"""
print(3600*24)
print(3600*24*30)

duration = int(input('Enter the time interval in seconds: '))

if duration < 60:
    print('Duration is', duration, 'seconds')
elif duration < 3600:
    duration_min = duration // 60
    print('Duration is', duration_min, 'minutes and', duration - duration_min * 60, 'seconds')
elif duration < 3600 * 24:
    duration_hour = duration // 3600
    duration_min = (duration - duration_hour * 3600) // 60
    print('Duration is', duration_hour, 'hours and', duration_min, 'minutes and',
          duration - duration_hour * 3600 - duration_min * 60, 'seconds')
elif duration < 3600 * 24 * 30:
    duration_day = duration // (3600 * 24)
    duration_hour = (duration - duration_day * 3600 * 24) // 3600
    duration_min = (duration - duration_day * 3600 * 24 - duration_hour * 3600) // 60
    print('Duration is', duration_day, 'days and', duration_hour, 'hours and', duration_min, 'minutes and',
          duration - duration_day * 3600 * 24 - duration_hour * 3600 - duration_min * 60, 'seconds')
else:
    print('Too much seconds for my code!')

# Задача 1.2.
# Дополнительно
# # Пункт D. 
# Переведите минуты и секунды в формат времени. Используйте модуль datetime
 
# Изначально непонятно, это "минуты.секунды" или "минуты.доли минут"
# проверка показывает, что в словаре [str, float]

# Если длительности песен представлены float, т.е. в виде "минуты.доли минут"
# тогда переводим так:

import datetime

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

# выводим песни и их длительности в формате часы:минуты:секунды
for song, duration in my_favorite_songs_dict.items():
    duration = datetime.timedelta(minutes=int(duration), seconds=int((duration-int(duration))*60))
    print(f'{song}: {duration}')


# Результат:
# Waste a Moment: 0:03:01
# New Salvation: 0:04:01
# Staying' Alive: 0:03:23
# Out of Touch: 0:03:01
# A Sorta Fairytale: 0:05:16
# Easy: 0:04:09
# Beautiful Day: 0:04:02
# Nowhere to Run: 0:02:34
# In This World: 0:04:01
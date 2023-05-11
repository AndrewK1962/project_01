# Задача 1.2.
# Дополнительно
# # Пункт D. 
# Переведите минуты и секунды в формат времени. Используйте модуль datetime
 
# Изначально непонятно, это "минуты.секунды" или "минуты.доли минут"
# проверка показывает, что в словаре [str, float]

# Предположим, что это всё-таки "минуты.секунды""
# тогда переводим так:

import datetime # подключаем модуль datetime 

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.45,
}


for song, duration in my_favorite_songs_dict.items():
    duration = datetime.timedelta(minutes=int(duration), seconds=int((duration-int(duration)) * 100 + 0.5))
    # минуты - это целая часть длительности
    # секунды - как бы дробная часть (сотые доли)  умноженные на 100
    # чтобы корректно округлить добавляем 0.5

    
    print(f'{song}: {duration}')
    # выводим песни и их длительности в формате часы:минуты:секунды  

# Результат:
# Waste a Moment: 0:03:03
# New Salvation: 0:04:02
# Staying' Alive: 0:03:40
# Out of Touch: 0:03:03
# A Sorta Fairytale: 0:05:28
# Easy: 0:04:15
# Beautiful Day: 0:04:04
# Nowhere to Run: 0:02:58
# In This World: 0:04:45
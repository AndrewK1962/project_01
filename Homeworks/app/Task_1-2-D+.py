# Задача 1.2.
# Дополнительно
# # Пункт D. 

# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

# Если длительности песен заданы правильно, "минуты.секунды", и дело только в формате вывода,
# то можно обойтись и без datetime

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


for song, duration in my_favorite_songs_dict.items(): # для каждой песни берём длительность
    minutes = int(duration)                     # целая часть - это минуты
    seconds = int((duration - minutes) * 60)    # дробная часть - это секунды, но это не 100-е доли, 
                                                # а 60-е, поэтому умножаем на 60 
    # Выводим песни и их длительность на консоль
    print(f'{song} - {minutes:02d}:{seconds:02d}')

# Результат:
# Waste a Moment - 03:01
# New Salvation - 04:01
# Staying' Alive - 03:23
# Out of Touch - 03:01
# A Sorta Fairytale - 05:16
# Easy - 04:09
# Beautiful Day - 04:02
# Nowhere to Run - 02:34
# In This World - 04:01
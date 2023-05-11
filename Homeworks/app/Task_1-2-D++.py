# Задача 1.2.
# Дополнительно
# # Пункт D. 

# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

# Изначально непонятно, это "минуты.секунды" или "минуты.доли минут"
# проверка показывает, что в словаре [str, float]

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

for song, duration in my_favorite_songs_dict.items():   # для каждой песни берём длительность
    minutes = int(duration)                             # целая часть - это минуты
    seconds = int((duration - minutes) * 100 + 0.5)     # дробная часть - это секунды,  100-е доли, 
                                                        # поэтому, умножаем на 100
                                                        # чтобы корректно округлить добавляем 0.5
                           
    print(f'{song} - {minutes:02d}:{seconds:02d}')
    # Выводим песни и их длительность по 2 знака

# Результат:
# Waste a Moment - 03:03
# New Salvation - 04:02
# Staying' Alive - 03:40
# Out of Touch - 03:03
# A Sorta Fairytale - 05:28
# Easy - 04:15
# Beautiful Day - 04:04
# Nowhere to Run - 02:58
# In This World - 04:02
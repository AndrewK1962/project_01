# Задача 1.2.
# Пункт A.
# Имеется плейлист песен в виде списка списков.
# Список my_favorite_songs содержит список названий и длительности каждого трека. 
# Выведите общее время звучания трех случайных песен в формате:
# Три песни звучат ХХХ минут.

# Непонятно, в каком формате заданы длительности песен
# кажется, здесь должны быть минуты:секунды, но почему-то разделитель (.)
# складывать длительности он скорее всего будет как float

import random

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

# Выбираем три случайные песни
random_songs = random.sample(my_favorite_songs, k=3)
# Выводим выбранные песни и их длительность на экран
print(f"Выбраны песни:")
for song in random_songs:
    print(song[0], song[1])

# Считаем общее время звучания 3-хвыбранных песен 
# и округляем до 2-х знаков (из-за потери точности многда получается слишком много знаков)
total_duration = round(random_songs[0][1] + random_songs[1][1] + random_songs[2][1], 2)

# Выводим результат
print(f"Общее время звучания {total_duration} минут.")

# Результат:
# Выбраны песни:
# Out of Touch 3.03
# Staying' Alive 3.4
# New Salvation 4.02
# Общее время звучания 10.45 минут.
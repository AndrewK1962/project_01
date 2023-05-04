# Задача 1.2.
# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

# Непонятно, почему длительности песен заданы как float
# кажется, здесь должны быть минуты:секунды
# складывать длительности будет как float

import random

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

# Выбираем три случайные песни
# и получаем результат уже в виде списка
random_songs = random.sample(list(my_favorite_songs_dict.items()), k=3)

# Выводим выбранные песни и их длительность на экран
print(f"Выбраны песни:")
for song in random_songs:
    print(song[0], song[1])

# Считаем общее время звучания 3-хвыбранных песен 
# и округляем до 2-х знаков (из-за потери точности многда получается слишком много знаков)
total_duration = sum([song[1] for song in random_songs])

# Выводим результат
print(f"Три песни звучат {total_duration} минут.")

# Результат:
# Выбраны песни:
# New Salvation 4.02
# A Sorta Fairytale 5.28
# Out of Touch 3.03
# Три песни звучат 12.33 минут.
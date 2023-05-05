# Задача 1.2.
# Пункт C. 
# Дополнительно для пунктов A и B
# Сгенерируйте случайные песни с помощью модуля random
# import random

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

# Результат:
# Выбраны песни:
# Waste a Moment 3.03
# In This World 4.02
# Beautiful Day 4.04
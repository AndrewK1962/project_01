# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

# ??? А "Staying\'" - это опечатка или так задумано???

# Разделяем строку на песни, разделитель - запятая с пробелом.
my_play_list = my_favorite_songs.split(', ')

# Выводим песни на экран
print(my_play_list[0])    # Первая песня
print(my_play_list[-1])   # Последняя песня
print(my_play_list[1])    # Вторая песня
print(my_play_list[-2])   # Вторая песня с конца 

# Результат:
# Waste a Moment
# New Salvation
# Staying' Alive
# Start Me Up
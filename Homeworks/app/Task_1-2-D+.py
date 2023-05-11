# Задача 1.2.
# Дополнительно
# # Пункт D. 

# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

# Изначально непонятно, это "минуты.секунды" или "минуты.доли минут"
# проверка показывает, что в словаре [str, float]

import datetime # импортируем модуль datetime.

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


# чтобы использовать функцию strftime из модуля datetime,
# она работает только с объектами datetime.datetime, а не с минутами и секундами,
# создаем функцию format_time, она принимает два аргумента: minutes и seconds
def format_time(minutes, seconds):
    time = datetime.datetime(2023, 5, 10, minute=minutes, second=seconds)
    # создаем объект time типа datetime.datetime
    # чтобы его заполнить, добавляем текущую дату: год, месяц, день
    # минуты и секунды из переданных функции аргументов
    return time.strftime('%M:%S')
    # вызываем метод strftime для объекта time с аргументом %M:%S. 
    # Этот аргумент означает, что мы хотим получить строковое представление времени,
    # где %M - заменяется на минуты, %S - на секунды.
   
for song, duration in my_favorite_songs_dict.items():   # для каждой песни берём длительность
      minutes = int(duration)                           # целая часть - это минуты
      seconds = int((duration - minutes) * 100 + 0.5)   # дробная часть - это секунды,  100-е доли, 
                                                        # поэтому, умножаем на 100
                                                        # чтобы корректно округлить добавляем 0.5
                           
      
      print(f'{song} -', (format_time(minutes, seconds)))
      # Выводим песни и их длительность используя функцию format_time

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
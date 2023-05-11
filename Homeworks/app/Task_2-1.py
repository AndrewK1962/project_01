# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

# def minimum(arr):
#     pass

# def maximum(arr):
#     pass

def minimum(arr):
    min_number = arr[0]         # предположим, что первое число в списке наименьшее
    for number in arr:          # идём по всем числам списка
        if number < min_number: # сравниваем, если очередное число меньше, 
            min_number = number # то назначаем его наименьшим
    return min_number

def maximum(arr):
    max_number = arr[0]         # предположим, что первое число в списке наибольшее
    for number in arr:          # идём по всем числам списка
        if number > max_number: # сравниваем, если очередное число больше, 
            max_number = number # то назначаем его наибольшим
    return max_number

# Например:
num = [4,6,2,1,9,63,-134,566]
print(f"max = {maximum(num)}, min = {minimum(num)}")

# Результат: 
# max = 566, min = -134

num = [-52, 56, 30, 29, -54, 0, -110]
print(f"max = {maximum(num)}, min = {minimum(num)}")
# Результат:
# max = 56, min = -110

num = [42, 54, 65, 87, 0] 
print(f"max = {maximum(num)}, min = {minimum(num)}")
# Результат:
# max = 87, min = 0

num = [5] 
print(f"max = {maximum(num)}, min = {minimum(num)}")
# Результат:
# max = 5, min = 5
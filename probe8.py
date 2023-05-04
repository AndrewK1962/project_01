# Основы python
#
# TODO задачи
#
# TODO  цикл while

#i = 0
#while i < 10:
    #i = i + 2
    #print('i =', i)
                    # i = 2
                    # i = 4
                    # i = 6
                    # i = 8
                    # i = 10
                    #

print('Здравствуйте!')
room_prices = [41, 94, 100, 7, 21, 92, 62, 49, 37, 17, ]
i = -1 # чтобы припервом проходе i = 0
while i < len(room_prices):
    i += 1
    price = room_prices[i]
    print('Проверяем ', price)
    if price == min(room_prices):
        print('Найдена минимальная цена')
        break
print('До свидания!')
# Здравствуйте!
# Проверяем  41
# Проверяем  94
# Проверяем  100
# Проверяем  7
# Найдена минимальная цена
# До свидания!
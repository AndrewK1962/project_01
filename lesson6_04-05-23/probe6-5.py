# Основы python 6
#
# TODO фнкции и параметры
# TODO модули и импорт

a, b = 179, 37

# def divine():
#     pass # иногда нужен pass чтобы функция ничего не возвращала


def divine(a, b): 
    '''функция целочисленное деление'''
    counter = -1
    temp = a
    while temp >= 0:
        temp -= b
        counter += 1
    return counter

print (divine(200, 2)) # 100
print (divine(221, 2)) # 110 

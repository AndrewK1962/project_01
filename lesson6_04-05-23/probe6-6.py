# Основы python 6
#
# TODO фнкции и параметры
# TODO модули и импорт

# a, b = 179, 37

# # def divine():
# #     pass # иногда нужен pass чтобы функция ничего не возвращала


# def divine(a, b): 
#     '''функция целочисленное деление'''
#     counter = -1
#     temp = a
#     while temp >= 0:
#         temp -= b
#         counter += 1
#     return counter

# print (divine(200, 2)) # 100
# print (divine(221, 2)) # 110 


def trapezoid_s(a, b, h):
    '''Функция для расчета площади трапеции. a - нижнее основание, b - верхнее основание, h - высота'''
    return h * (a+b) / 2
S = trapezoid_s(8, 4, 10) 
print(S) # 60.0

S = trapezoid_s(8, h=4, b=10) 
print(S) # 36.0 разные результаты потому что часть параметров именованные 
                              # а часть позиционированныt
S = trapezoid_s(a= 8, h=4, b=10)  # 36.0
print(S)
S = trapezoid_s(a= 8, b=10, h=4) # 36.0
print(S)

# лучше использовать всегда  именованные параметры
# \n означает перенос на следующую строку
print(1, 2, False, '\n')
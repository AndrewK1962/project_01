 #Основы python
#
# TODO задачи
# TODO условный оператор if
# TODO операторы цикла while и for
# TODO однострочники

# Условный оператор if
# Про эластичность

elasticity_dem = 1
if elasticity_dem == 0:
    print('Товары первой необходимости') #Вложенное условие!
    result = 0.0
elif 0 < elasticity_dem < 1:
    print('Нормальные блага')
    result = 0.5
elif elasticity_dem > 1:
    print('Роскошь')
    result = 3.0
else:
    print ('Товары низкого качества')
    result = -1.0
    if elasticity_dem == 1:
        print ('Единичная  эластичность')#Вложенное условие!
        result = 1.0
print('значение =',result)

# Альтернатива if-elif
#try:
#    x=[1,2,3][4]
#except IndexError:
#    x=[1,2,3][-1]


 # Основы python
# TODO отличие списков от кортежей
# TODO задачи
# TODO условный оператор if
# TODO операторы цикла while и for 


# Отличие списков от кортежей
# Это список list
shop_list = ['Картофель', 'Горошек', 'Рис', 'Хлеб']
# Это кортеж - неизменяемый список, в круглых скобках
rainbow = ('Red', 'Green','Blue')
# print(dir(rainbow)) # 'count', 'index' - всего два метода

# Проблема изменяемых ообъектов
new_lst = shop_list
new_lst.append('Вкусняшка')
print(new_lst)
print(shop_list)
print(id(shop_list)) 
print(id(new_lst))
print(id(shop_list) == id(new_lst))
# ['Картофель', 'Горошек', 'Рис', 'Хлеб', 'Вкусняшка']
# ['Картофель', 'Горошек', 'Рис', 'Хлеб', 'Вкусняшка']
# 2176243356992
# 2176243356992
#True
# обе переменные меняются одновременно!!! ID  совпадают

new_tpl = rainbow
new_tpl = new_tpl + ('Violet', )
print(rainbow)
print(new_tpl)
print(id(new_tpl))
print(id(rainbow)) 
print(id(rainbow) == id(new_tpl))
# ('Red', 'Green', 'Blue')
# ('Red', 'Green', 'Blue', 'Violet')
# 2176245266160
# 2176245300224
#False
# ID  не совпадают, исходник не меняется!!!
  
  # кортеж работает быстрее чем список
x, y = 1, 2
# python видит это как 2 кортежа:
(x, y) = (1, 2)
for pair in enumerate(rainbow):
    print(pair) # (0, 'Red')
                # (1, 'Green')
                # (2, 'Blue')

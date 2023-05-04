#Основы python
#
# TODO задачи
# TODO однострочники

# Задача про зарплату
# Нужно найти всех сотрудников с зарплатой от 100000 руб
employees ={'Alice' : 100000,
            'Bob' : 99817,
            'Carol' : 122908,
            'Frank' : 88123,
            'Eve' : 93121}

#print(employees['Alice'])

# Вариант 1
top_mgrs =[]
for i in employees:
    if employees[i] >= 100000:
        top_mgrs.append(i)

print(top_mgrs) # ['Alice', 'Carol']

# Вариант 2 однострочник

if employees['Alice'] >= 100000:
        print(True) #  True
# однострочник if
flag = True if employees['Alice'] >= 100000 else False
print(flag) #  True

# однострочник for
for i in employees:
     print(i)
# списковое включение
list = [i for i in employees] 
print(list)#                                      ['Alice', 'Bob', 'Carol', 'Frank', 'Eve']

print([i for i in employees])# работает одинаково ['Alice', 'Bob', 'Carol', 'Frank', 'Eve']

# список всех сотрудников
top_mgrs = [i for i in employees]

# как получить отфильтрованный список сотрудников
top_mgrs = [employees[i] >= 100000 for i in employees] 
print(top_mgrs) # [True, False, True, False, False] но это не то что нужно

# надо вот так это намного короче чем Вариант 1
top_mgrs = [i for i in employees if employees[i] >= 100000] 
print(top_mgrs) # ['Alice', 'Carol']


# что такое словари
lst =[1, 2] # списки -изменяемые массивы
tpl = (1, 2) # кортежи - неименяемые массивы
dct = {'1, 2'} # словари - хэш таблица, как ярлыки очень быстро извлекается из памяти


# словарь столиц разных стран
capitals = {'Россия' : 'Москва'}
print(capitals['Россия']) # Москва

# Добавление элементов в словарь
capitals['Франция'] = 'Париж'
capitals['Италия'] = 'Рим'
# Вывод словаря
print(capitals) #{'Россия': 'Москва', 'Франция': 'Париж', 'Италия': 'Рим'}

# Словарь – это список, элементам которого соответсвует
# произвольный идентификатор
# Основы python 6
#
# TODO фнкции и параметры
# TODO модули и импорт


# функция -это блок кода, который моржно вызывать с различными параметрами
# DRY Dont Reapete Youself


# Задача про зарплату
# Нужно найти всех сотрудников с зарплатой от 100000 руб
employees ={'Alice' : 100000,
            'Bob' : 99817,
            'Carol' : 122908,
            'Frank' : 88123,
            'Eve' : 93121}

# #print(employees['Alice'])

# Новое решение через функции
def get_top_mgrs(empl): 
    '''get_top_mgrs  возвращает список сотруников с зарплатой > 100000'''
    top_mgrs =[]
    for i in empl:
          if empl[i] >= 100000:
               top_mgrs.append(i)

    return top_mgrs


get_top_mgrs(employees) #['Alice', 'Carol']

salary = [employees[i]*2 for i in get_top_mgrs(employees)]


print(get_top_mgrs(employees)) # ['Alice', 'Carol']

print(salary) # [200000, 245816]




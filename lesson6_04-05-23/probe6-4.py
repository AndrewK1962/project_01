#$ Копия от Никиты из чата


employees = {'Alice' : 100000,
    'Bob' : 99817,
    'Carol' : 122908,
    'Frank' : 88123,
    'Eve' : 93121}
 
# Решение
def get_top_mgrs(empl: dict) -> list:
    '''get_top_mgrs принимает словарь сотрудников и возвращает список сотрудников,
    у которых зарплата больше 100000.'''
    top_mgrs = []
    for i in empl:
        if empl[i] >= 100000:
            top_mgrs.append(i)
 
    return top_mgrs
 
salary = [employees[i]*2 for i in get_top_mgrs(employees)]
print(salary)
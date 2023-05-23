# Перегрузка операторов

# Методы, которые позволяют 
# переопределить стандартные 
# возможности языка.
# Например, переопределить правила 
# сравнения или сложения двух объектов.

class Row:
    '''Строка таблицы как псевдосписок'''
    def __init__(self, *args):
        self._args = args

    def __eq__(self, other):
        return self._args == other._args
    
    def __add__(self, other):
        return self._args + other._args if isinstance(other, Row) else self._args + other
    

F = Row(1, 2, 3)
E = Row(1, 2, 3)
print(F == E)
print(F + E)
print(F + (1, 2))
print(F + (1, 'Hello'))

# вывод
# True
# (1, 2, 3, 1, 2, 3)
# (1, 2, 3, 1, 2)
# (1, 2, 3, 1, 'Hello')

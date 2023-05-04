#TODO модули и импорт


# модули - это файл с расширением  .py
# пакет - это папка в которой  лежат модули и файл __init__.py
# библиотека - набор пакетов


# импорт  вызов имени функции, класcаили перменной из другого модуля 
import my_module # импорт модуля
import my_module as mm # импорт модуля как синоним имени mm
# import numpy as np # импорт модуля как синоним имени np

from ex_module import var_2

from ex_module import foo
from my_module import foo # если одинаковые имена функций работает последнее


my_module.foo() # Как дела?
print(my_module.var_1)# Привет
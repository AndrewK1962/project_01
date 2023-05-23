# Классы машин
 
# Создание класса машины
class Car:
    # атрибуты - переменные внутри класса (характеристики)
    wheels = 4
    color = 'Black'
 
    # методы - функции внутри класса (действия)
    # связанные методы
    def sound(self):
        print('Bebeb')
    
    def start(self, check):
        self.engine_start = 'Готова к движению' if check == True else 'Не готова к движению'
        return self.engine_start
 
# Объявление экземпляра класса
toyota1 = Car()
toyota2 = Car()
toyota3 = Car()
toyota4 = Car()
 
# Измениние атрибута
print(toyota1.color)
toyota1.color = 'Red'
print(toyota1.color, toyota2.color)
 
# Вызов метода
toyota1.start(True)
print(toyota1.engine_start)
 
toyota1.sound()
 #===================================================================================================================

 # Классы
 
# Императивный стиль - обращение к компьютеру в виде инструкций
# ООП - представляем программу в виде взаимодействующих объектов
 
# Пользователь.опубликовать_пост -> Пост
# 2 / 2 -> 1.0
 
# Создание класса
class Cell:
    '''Ячейка'''
    # атрибуты - переменные внутри класса
    content = 1
    content_type = int()
 
    def set_value(self, val):
        '''Поменять значение ячейки'''
        self.content = val
        self.content_type = type(val)
    
# Создание экземпляра класса (instance)
F13 = Cell()
print(F13.content)
F13.set_value(100)
print(F13.content)
 
 
# Магия Python - встроенные методы и атрибуты, которые определены для каждого класса
 
class Bucket:
    '''Хранилише объектов для статического сайта'''
 
    def __init__(self, tutorial=None):
        '''Инициализация бакета без описания по-умолчанию'''
        self.content = []
        if tutorial is not None:
            self.content.append(tutorial)
 
    def __str__(self):
        return 'Содержимое: ' + ', '.join(self.content)
    
    def __bool__(self):
        return self.content != []
 
    def add(self, obj):
        '''Поместить объект в хранилище'''
        self.content.append(obj)
 
    def inspect(self):
        '''Проверка содержимого бакета'''
        print('Содержание бакета:')
        for item in self.content:
            print('  ', item)
 
# website = Bucket(tutorial='README.md')
# website.add('index.html')
# website.inspect()
 
# print(website)
# print(bool(website))
 
# empty_bucket = Bucket()
# print(bool(empty_bucket))
 
 
# Перегрузка операторов - изменения стандартного поведения объектов в Python
class Row:
    '''Строка таблицы, как псевдосписок'''
    def __init__(self, *args) -> None:
        self._args = args
 
    def __eq__(self, other):
        return self._args == other._args
    
    def __add__(self, other):
        return self._args + other._args if isinstance(other, Row) else self._args + other
    
F = Row(1, 2, 3)
E = Row(1, 2, 3)
 
print(F == E)
 
# res = E + F
res = E + (1, 'Hello')
print(res)
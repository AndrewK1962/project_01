# Классы

# Создание класса
class Cell:
    '''ячейка'''
    # атрибуты  - переменные внутри класса
    content = 1
    content_type = int()

    def set_value(self, val):
        '''поменять значение ячейки'''
        self.content =val
        self.content_type= type(val)

# Создание экземпляра класса (instance)
F13 = Cell()
print(F13.content)
# вывод 1
print(F13.content_type)
# вывод 0
F13.set_value(100)
print(F13.content)
# вывод 100



# Магия Python, что это такое?
# это - встроенные методы и атрибуты, которые определены для каждого класса
# Методы, которые обрамлены в два 
# нижних подчерка (например, __init__), 
# позволяют выполнять особые команды, 
# встроенные в интерпретатор: создание, 
# удаление, преобразование, сравнение и 
# другие.

class Bucket: # 
    '''Хранилище объектов для
        статического сайта'''
    def __init__(self, tuturial = None):
        '''Инициализация бакета без описания по умолчанию'''
        self.content = []
        if tuturial is not None:
            self.content.append(tuturial)

    def __str__(self):
        return 'Содержимое: ' + ','.join(self.content)

            
    def add(self, obj):
        '''поместить объект в хранилище(бакет) '''
        self.content.append(obj)
    
    def inspect(self):
        '''Проверка содержимого'''
        print('Текущее содержимое бакета')

        for item in self.content:
            print('   ', item)


website = Bucket()

print(type(website.content))
#  вывод 
# <class 'list'>
print(bool(website.content))
#  вывод 
# False

website = Bucket(tuturial="Reeadme.md")
print(website.content)
#  вывод 
# ['Reeadme.md']

website.add('index.html')
website.inspect()
# Текущее содержимое бакета
#     Reeadme.md
#     index.html

print(website) 
#  вывод 
# <__main__.Bucket object at 0x0000019ADE938810>  

# После переопределения метода __str__
#  вывод 
# Содержимое: Reeadme.md,index.html









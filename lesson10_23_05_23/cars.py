# Классы машин

# Создание класса машины
class Car:
    # атрибуты - переменные внутри класса (характеристики)
    weeels = 4
    color = 'Black'

    # методы  - функции внутри класса (действия)
    # связанные методы
    def sound(self):
        print('Beeep')

    def start(self, check):
        self.engine_start = 'готова к движению' if check == True else 'не готова к движению'
        return  self.engine_start

# Объявление экземпляра класса
toyota1 = Car()
toyota2 = Car()
toyota3 = Car()
toyota4 = Car()
# изменение атрибутов
print(toyota1.color)
toyota1.color = 'Red'
print(toyota1.color, toyota2.color)
# вывод
# Black
# Red Black

# вызов метода
print(toyota1.start(True))
# вывод
# готова к движению
# а  была Ошибка ! TypeError: Car.start() takes 1 positional argument but 2 were given
toyota1.sound()  
# вывод 
# Beeep
print(toyota1.engine_start)
# вывод
# готова к движению
print(toyota2.engine_start)
# Ошибка !AttributeError: 'Car' object has no attribute 'engine_start'




    

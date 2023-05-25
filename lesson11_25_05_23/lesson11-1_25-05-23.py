# ООП
# 
 # Этап создания класса
class Car:
    def __init__(self):
        self.engine = False
        self.wheels = 4
 
    def sound(self):
        print('Bee')
 
    def start(self, start_engine):
        self.engine = True if start_engine=='Ключ' else False
        return self.engine
 # наследование
class Van(Car):
    
    def move_cargo(self, truck):
        self.cargo = truck
 
# Этап создания экземпляра класса
toyota1 = Car()
toyota2 = Car()
Kamaz = Van()
 
toyota1.start('Ключ')
print(toyota1.engine)
 
Kamaz.move_cargo('Прицеп')
print(Kamaz.cargo)
Kamaz.sound()


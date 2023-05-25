# Этап создания класса
# Родительский класс
 
class User(object):
    '''Модель пользователя'''
 
    # Инкапсуляция
    __token = 'very_secret_token'
 
    def __init__(self, name=None):
        self.name = name
        self.active = True
        self.gid = 1000
        self.get_permission('700')
    
    def __str__(self):
        return f"id({self.gid}), {'Active' if self.active is True else 'Dead'}"
    
    def get_permission(self, args):
        self.u, self.g, self.o = args
        return self.u, self.g, self.o
    
    def check_permission(self):
        print(f'Права: {self.u, self.g, self.o}')
 
class RemoteDesktop:
    '''Группа пользователей удаленного рабочего стола'''
 
    def __str__(self):
        return 'Подключение к удаленному рабочему столу'
    
    def connection(self):
        return 'Гость подключился'
    
# Дочерний класс
class Guest(RemoteDesktop, User):
    '''Гость'''
 
# Дочерний класс
class Admin(User):
    '''Администратор'''
 
    def __init__(self, name=None):
        super().__init__(name)
        self.get_permission('770')
 
class Root(User):
 
    def __init__(self, name=None):
        super().__init__(name)
        self.gid = 0
        self.active = False
        self.get_permission('777')
    
    def get_token(self):
        print(self.__token)
 
 
# Экземпляры пользователей
user1 = Guest('Радж')
user2 = Admin('Сэм')
user0 = Root()
 
print(user1, user2, user0, sep='\n')
user1.check_permission()
user2.check_permission()
user0.check_permission()
 
# user0.get_token()
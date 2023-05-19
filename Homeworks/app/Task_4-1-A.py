# Задача 4.1. A
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

#==============================================================================================

# По смыслу базы School_Id не может быть Primary key, 
# тогда в базе может быть только 1 ученик из каждой школы
# Primary key должен быть Student_Id

import sqlite3 # подключаем модуль sqlite3

# Создаем подключение к базе данных teachers.db
conn = sqlite3.connect(r'C:\Users\Andrew.Kalashnikov\Desktop\project_01\Homeworks\app\teachers.db')

# В базе данных teachers.db Создаем таблицу Students
conn.execute('''CREATE TABLE IF NOT EXISTS Students
             (Student_Id INTEGER PRIMARY KEY,
             Student_Name TEXT,
             School_Id INTEGER);''')

# Заполняем таблицу Students данными по списку
students_data = [
    (201, 'Иван', 1),
    (202, 'Петр', 2),
    (203, 'Анастасия', 3),
    (204, 'Игорь', 4),
    (205, 'Семён', 4)
]
conn.executemany("INSERT INTO Students VALUES (?, ?, ?)", students_data)

# Сохраняем изменения в базе teachers.db
conn.commit()
# Закрываем соединение с базой данных
conn.close()



# Задача 4.1. B
# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:
#===================================================================================================

import sqlite3 # подключаем модуль sqlite3

# Создаем подключение к базе данных teachers.db
conn = sqlite3.connect(r'C:\Users\Andrew.Kalashnikov\Desktop\project_01\Homeworks\app\teachers.db')

# # Функция для получения информации о студенте по ID
def get_student_info(student_id):
    # Получаем данные из таблицы Students и School
    cursor = conn.execute("""
        SELECT s.Student_Id, s.Student_Name, s.School_Id, sc.School_Name
        FROM Students s
        JOIN School sc ON s.School_Id = sc.School_Id
        WHERE s.Student_Id = ?
    """, (student_id,))
    
    # Если студент с таким ID найден, выводим информацию о нем и его школе
    student_data = cursor.fetchone()
    if student_data:
        print("ID Студента:", student_data[0])
        print("Имя студента:", student_data[1])
        print("ID школы:", student_data[2])
        print("Название школы:", student_data[3],'\n')
    else:
        print("Студент не найден.")
        
# Например:
get_student_info(202)
get_student_info(203)
get_student_info(777)  # несуществующий ID

# Закрываем соединение с базой данных
conn.close()

# ID Студента: 202
# Имя студента: Петр
# ID школы: 2
# Название школы: Преспектива

# ID Студента: 203
# Имя студента: Анастасия
# ID школы: 3
# Название школы: Спектр

# Студент не найден.

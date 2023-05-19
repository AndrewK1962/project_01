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

# Функция для получения информации о студенте по ID
def get_student_info(student_id):
    cursor = conn.execute("SELECT Student_Id, Student_Name, School_Id FROM Students WHERE Student_Id = ?", (student_id,))
    student = cursor.fetchone()
    
    if student is None:
        return "Студент не найден"
    
    school_id = student[2]
    cursor = conn.execute("SELECT School_Id, School_Name FROM School WHERE School_Id = ?", (school_id,))
    school = cursor.fetchone()
    
    return f"ID Студента: {student[0]}\nИмя студента: {student[1]}\nID школы: {school[0]}\nНазвание школы: {school[1]}"

# Например:
print(get_student_info(201),'\n')
print(get_student_info(205),'\n')
print(get_student_info(777),'\n')  # несуществующий ID

# Закрываем соединение с базой данных
conn.close()

# Результат:

# ID Студента: 201
# Имя студента: Иван
# ID школы: 1
# Название школы: Протон

# ID Студента: 205
# Имя студента: Семён
# ID школы: 4
# Название школы: Содружество

# Студент не найден



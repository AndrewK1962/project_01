# Задача 8
import sqlite3
import pandas as pd
con1 = sqlite3.connect("Students.db")
con2 = sqlite3.connect("Schools.db")

df1 = pd.read_sql('SELECT * FROM Students', con1)
df1.to_sql("Students", con2, if_exists="append", index = False)

df2 = pd.read_sql('SELECT Students.Student_name, Students.School_id, School.School_name FROM Students JOIN School ON Students.School_id = School.School_id', con2)
print(df2)
df2.to_excel('Task8.xlsx', index = False)
# Вывод:
# Student_name  School_id  School_Name
# 0           Иван          1       Протон
# 1           Петр          2  Преспектива
# 2      Анастасия          3       Спектр
# 3          Игорь          4  Содружество
# 4           Влад          1       Протон
# ..           ...        ...          ...
# 156    Анастасия          3       Спектр
# 157        Игорь          4  Содружество
# 158         Влад          1       Протон
# 159        Ольга          2  Преспектива
# 160      Алексей          3       Спектр

# [161 rows x 3 columns]
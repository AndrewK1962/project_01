# Задача 7
import sqlite3
import pandas as pd
con = sqlite3.connect("Schools.db")

df = pd.DataFrame({'School_id': [7,8,9],
                           'School_name': ['Ромашка', 'Василёл', 'Победитель'],
                           'Place_count': [200,300,400]})

df.to_sql("School", con, if_exists="append", index = False)
df2 = pd.read_sql('SELECT * FROM School', con)
print(df2)
df2.to_excel('Task7.xlsx', index = False)

#Вывод
# School_Id  School_Name  Place_Count
# 0          1       Протон          200
# 1          2  Преспектива          300
# 2          3       Спектр          400
# 3          4  Содружество          500
# 4          7      Ромашка          200
# 5          8      Василёл          300
# 6          9   Победитель          400
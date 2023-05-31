# Задача 8
import sqlite3
import pandas as pd
con1 = sqlite3.connect("Students.db")
con2 = sqlite3.connect("Schools.db")

df1 = pd.read_sql('SELECT * FROM Students', con1)
df1.to_sql("Students", con2, if_exists="append", index = False)

df2 = pd.read_sql('SELECT Students.Student_name, Students.School_id, School.School_name FROM Students JOIN School ON Students.School_id = School.School_id', con2)
print(df2)
#df2.to_excel('Task8.xlsx', index = False)
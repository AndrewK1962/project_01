import sqlite3
import pandas as pd

con = sqlite3.connect("Students.db")
query = "SELECT * FROM Students"
df = pd.read_sql(query,con)
print (df)

con2 = sqlite3.connect("teachers.db")
df.to_sql("Students",con2, index = False)
print ("ok")

# Student_id Student_name  School_id
# 0         201         Иван          1
# 1         202         Петр          2
# 2         203    Анастасия          3
# 3         204        Игорь          4
# ok
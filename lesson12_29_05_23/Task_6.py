# Задача 6
import sqlite3
import pandas as pd

con = sqlite3.connect("Students.db")

cars = pd.DataFrame({'Car': ['Жигули','Волга','Ока'],
                     'Student_id': [205,206,207]})
cars.to_sql("Cars", con, if_exists="append", index = False)

df = pd.read_sql('SELECT Students.Student_name, Cars.Car FROM Students JOIN Cars ON Students.Student_id=Cars.Student_id', con)
print (df)
df.to_excel('Task6.xlsx', index = False)
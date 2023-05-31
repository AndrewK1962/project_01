# Задача 3

import pandas as pd

df = pd.read_excel("data.xlsx", sheet_name='Sheet1')
df1 = df[df['volume'] > 15]
print (df1)
df2 = df1[df1['volume'] < 50]
df2.to_excel("task3.xlsx", index = False)

import sqlite3
import pandas as pd

con = sqlite3.connect("Students.db")
df = pd.read_sql('SELECT * FROM Students', con)
df.to_excel("task5.xlsx", index = False)

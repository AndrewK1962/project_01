# Задача 4
import sqlite3
import pandas as pd

con = sqlite3.connect("Students.db")

dfnewstuds = pd.DataFrame({'Student_id': [205,206,207],
                           'Student_name': ['Влад', 'Ольга', 'Алексей'],
                           'School_id': [1,2,3]})
dfnewstuds.to_sql("Students",con,if_exists="append", index = False)
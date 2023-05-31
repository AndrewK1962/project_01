# Задача 5
import sqlite3
import pandas as pd

con = sqlite3.connect("Students.db")

df = pd.DataFrame({'School_id': [1,2,3],
                   'City': ['МСК', 'СПБ', 'ЕКБ']})

df.to_sql("Cities",con, if_exists="append", index = False)
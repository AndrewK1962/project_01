
# import sqlite3
# import pandas as pd

# con = sqlite3.connect("Students.db")
# query = "SELECT * FROM Students"
# df = pd.read_sql(query,con)
# print (df)

# con2 = sqlite3.connect("teachers.db")
# df.to_sql("Students",con2, index = False)
# print ("ok")



# import sqlite3

# con = sqlite3.connect("teachers.db")
# cursor = con.cursor()

# cursor.execute("SELECT * FROM sqlite_master WHERE type = 'table'")
# tables = cursor.fetchall()
# con.close()
# # print (tables)
# for table in tables:
#   print (table) # Инфа по таблице
#   #print (table[1]) # Название таблицы

# import sqlite3

# con = sqlite3.connect("teachers.db")
# cursor = con.cursor()

# cursor.execute("SELECT * FROM Teatcher")
# columnname = cursor.description
# con.close()
# #print (columnname)
# for col in columnname:
#   print(col[0])

# import sqlite3


# def get_student_detail(student_id):
#   con = sqlite3.connect("teachers.db")
#   cursor = con.cursor()
#   query = """SELECT * FROM School JOIN Students ON School.School_Id = Students.School_Id WHERE Students.Student_id = ?"""
#   cursor.execute(query,(student_id,))
#   records = cursor.fetchall()
#   print (records)


# get_student_detail(201)

# import sqlite3

# def get_school(school_id):
#   con = sqlite3.connect("Schools.db")
#   cursor = con.cursor()
#   query = "SELECT * FROM School WHERE School_Id = ?"
#   cursor.execute(query,(school_id,))
#   record = cursor.fetchone()
#   #print (record)
#   con.close()
#   return record[1]

# def get_student(student_id):
#   con = sqlite3.connect("Students.db")
#   cursor = con.cursor()
#   query = "SELECT * FROM Students WHERE Student_Id = ?"
#   cursor.execute(query,(student_id,))
#   record = cursor.fetchall()
#   #print (record)
#   con.close()
  
#   for raw in record:
#     print (raw[0])
#     school_id = raw[2]
#     school_name = get_school(school_id)
#     print (school_name)
    

# get_student(201)

# import pandas as pd

# df = pd.DataFrame({'A': [0,1,2,3,4],
#                    'B': [5,6,7,8,9],
#                    'C': ['test1', 'test2', 'test3','test4', 'test5']})

# df.to_json("test1.json")

# import pandas as pd

# df = pd.read_excel("data.xlsx", sheet_name='Sheet1')

# print (df)

#Задача 1
import pandas as pd

df = pd.read_excel("data.xlsx", sheet_name='Sheet1')
kapusta = df[df['sku'] == "Капуста"]
kapusta.to_excel("task1.xlsx", index = False)

# Задача 2

import pandas as pd

df = pd.read_excel("data.xlsx", sheet_name='Sheet1')

kivi = df[df['sku'] == "Киви"]
kivi1 = kivi[kivi['priceoforder'] > 1000]
kivi1.to_excel("task2.xlsx", index = False)

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

# Задача 4
import sqlite3
import pandas as pd

con = sqlite3.connect("Students.db")

dfnewstuds = pd.DataFrame({'Student_id': [205,206,207],
                           'Student_name': ['Влад', 'Ольга', 'Алексей'],
                           'School_id': [1,2,3]})
dfnewstuds.to_sql("Students",con,if_exists="append", index = False)

# Задача 5
import sqlite3
import pandas as pd

con = sqlite3.connect("Students.db")

df = pd.DataFrame({'School_id': [1,2,3],
                   'City': ['МСК', 'СПБ', 'ЕКБ']})

df.to_sql("Cities",con, if_exists="append", index = False)

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

# Задача 7
import pandas as pd
import requests

link = ''
token = ''

request = f'{link}/rtpi_rosstat_weight?select=rosstat_id,rosstat_name'
myheaders = {'Authorization': f'Bearer {token}',
             'Content-Type': 'application/json',
             'Range-Unit': 'items'}

response = requests.get(request,headers = myheaders)

response.json()

df = pd.DataFrame(response.json())
df.to_excel("testdata1.xlsx", index = False)
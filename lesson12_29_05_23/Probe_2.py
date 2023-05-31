import sqlite3

con = sqlite3.connect("teachers.db")
cursor = con.cursor()

cursor.execute("SELECT * FROM sqlite_master WHERE type = 'table'")
tables = cursor.fetchall()
con.close()
# print (tables)
for table in tables:
  print (table) # Инфа по таблице
  #print (table[1]) # Название таблицы

#   ('table', 'School', 'School', 2, 'CREATE TABLE School (\nSchool_Id INTEGER NOT NULL PRIMARY KEY,\nSchool_Name TEXT NOT NULL,\nPlace_Count INTEGER NOT NULL\n)')
# ('table', 'Teatcher', 'Teatcher', 3, 'CREATE TABLE Teatcher (\nTeatcher_Id INTEGER NOT NULL PRIMARY KEY,\nTeatcher_Name TEXT NOT NULL,\nSchool_Id INTEGER NOT NULL,\nJoining_Date TEXT NOT NULL,\nSpeciality TEXT NOT NULL,\nSalary INTEGER NOT NULL,\nExperience INTEGER\n)')
# ('table', 'Students', 'Students', 4, 'CREATE TABLE "Students" (\n"Student_id" INTEGER,\n  "Student_name" TEXT,\n  "School_id" INTEGER\n)')
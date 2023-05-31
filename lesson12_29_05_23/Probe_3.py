import sqlite3

con = sqlite3.connect("teachers.db")
cursor = con.cursor()

cursor.execute("SELECT * FROM Teatcher")
columnname = cursor.description
con.close()
#print (columnname)
for col in columnname:
  print(col[0])

# Teatcher_Id
# Teatcher_Name
# School_Id
# Joining_Date
# Speciality
# Salary
# Experience
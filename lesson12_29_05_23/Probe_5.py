import sqlite3

def get_school(school_id):
  con = sqlite3.connect("Schools.db")
  cursor = con.cursor()
  query = "SELECT * FROM School WHERE School_Id = ?"
  cursor.execute(query,(school_id,))
  record = cursor.fetchone()
  #print (record)
  con.close()
  return record[1]

def get_student(student_id):
  con = sqlite3.connect("Students.db")
  cursor = con.cursor()
  query = "SELECT * FROM Students WHERE Student_Id = ?"
  cursor.execute(query,(student_id,))
  record = cursor.fetchall()
  #print (record)
  con.close()
  
  for raw in record:
    print (raw[0])
    school_id = raw[2]
    school_name = get_school(school_id)
    print (school_name)
    

get_student(201)

# 201
# Протон
import sqlite3


def get_student_detail(student_id):
  con = sqlite3.connect("teachers.db")
  cursor = con.cursor()
  query = """SELECT * FROM School JOIN Students ON School.School_Id = Students.School_Id WHERE Students.Student_id = ?"""
  cursor.execute(query,(student_id,))
  records = cursor.fetchall()
  print (records)


get_student_detail(201)

# [(1, 'Протон', 200, 201, 'Иван', 1)]
# -*- coding: utf-8 -*-
"""15052023_3potok.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nDXi85Dci-XcCxVAkdMY8T1LYg5B4gP5
"""

# Создание таблицы
import sqlite3

connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
sqlquery ="""INSERT INTO Teatcher (Teatcher_Id , Teatcher_Name, School_Id, Joining_Date, Speciality, Salary, Experience)
VALUES
('101', 'Галина', '1', '2021 2 10', ' Физик', '40000', NULL),
('102', 'Мария', '1', '2018 07 23', ' Химик', '20000', NULL),
('103', 'Ольга', '2', '2022 05 19', 'Информатик', '25000', NULL),
('104', 'Полина', '2', '2017 12 28', 'Физик', '28000', NULL),
('105', 'Лидия', '3', '2015 06 04', 'Информатик', '42000',NULL),
('106', 'Анастасия', '3', '2019 09 11', 'Учитель трудов', '30000', NULL),
('107', 'Ирина', '4', '2020 08 21', 'Информатик', '32000', NULL),
('108', 'Виктория', '4', '2017 10 17', 'Географ', '30000', NULL);
"""

cursor.execute(sqlquery)
connection.commit()
connection.close()

# Задача 2. Подключиться к БД и вывести ее версию
import sqlite3

def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def read_dbversion():
  try:
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT sqlite_version();")
    db_version = cursor.fetchone()
    print ("Вы подключились к SQLite версии: ", db_version)
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print("Ошибка в получении данных ", error)

read_dbversion()

# Задача 3 . Проставить опыт работы всем учителям

import sqlite3

def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def update_exp():
  try:
    connection = get_connection()
    cursor = connection.cursor()
    sqlquery = """UPDATE Teatcher SET Speciality = 'Физик' WHERE Teatcher_Id = 101"""
    cursor.execute(sqlquery)
    connection.commit()
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print("Ошибка в получении данных ", error)

update_exp()

# Задача 4. Вывести данные о школе и учителе, используя идентификатор школы и идентификатор учителя
import sqlite3

def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_school_data(school_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    sqlquery = "SELECT * FROM School WHERE School_Id = ?"
    cursor.execute(sqlquery,(school_id,))
    records = cursor.fetchall()
    print ("Данные по школе")
    for row in records:
      print ("ID школы: ", row[0])
      print ("Название школы: ", row[1])
      print ("Количество мест: ", row[2])
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print("Ошибка в получении данных ", error)


def get_teacher_data(teacher_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    sqlquery = "SELECT * FROM Teatcher WHERE Teatcher_Id = ?"
    cursor.execute(sqlquery,(teacher_id,))
    records = cursor.fetchall()
    print(records)
    print ("Данные по учителю")
    for row in records:
      print ("ID Учителя: ", row[0])
      print ("Имя учителя: ", row[1])
      print ("ID школы: ", row[2])
      print ("Дата начала работы:: ", row[3])
      print ("Специализация: ", row[4])
      print ("Зарплата: ", row[5])
      print ("Опыт работы: ", row[6])
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print("Ошибка в получении данных ", error)


get_teacher_data(101)

# Задача 5 . Вывести список учителей по заданной специальности и зарплате
import sqlite3

def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_techer_speciality(speciality, salary):
  connection = get_connection()
  cursor = connection.cursor()
  sqlquery = "SELECT * FROM Teatcher WHERE Speciality = ? AND Salary > ?"
  cursor.execute(sqlquery,(speciality, salary))
  records = cursor.fetchall()
  print ("Учителя со спекой", speciality, "и зарплатой больше чем ", salary, "\n")
  for row in records:
      print ("ID Учителя: ", row[0])
      print ("Имя учителя: ", row[1])
      print ("ID школы: ", row[2])
      print ("Дата начала работы:: ", row[3])
      print ("Специализация: ", row[4])
      print ("Зарплата: ", row[5])
      print ("Опыт работы: ", row[6], "\n")
  close_connection(connection)


get_techer_speciality("Физик",15000)

# Задача 6. Вывести список учителей по ID школы

import sqlite3

def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_school_name(school_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    sqlquery = "SELECT * FROM School WHERE School_Id = ?"
    cursor.execute(sqlquery,(school_id,))
    record = cursor.fetchone()
    close_connection(connection)
    return record[1]
  except (Exception, sqlite3.Error) as error:
    print("Ошибка в получении данных ", error)


def get_teacher_detail(school_id):
  try:
    school_name = get_school_name(school_id)
    connection = get_connection()
    cursor = connection.cursor()
    sqlquery = "SELECT * FROM Teatcher WHERE School_Id = ?"
    cursor.execute(sqlquery,(school_id,))
    records = cursor.fetchall()
    for row in records:
      print ("ID Учителя: ", row[0])
      print ("Имя учителя: ", row[1])
      print ("ID школы: ", row[2])
      print ("Название школы: ", school_name)
      print ("Дата начала работы:: ", row[3])
      print ("Специализация: ", row[4])
      print ("Зарплата: ", row[5])
      print ("Опыт работы: ", row[6], "\n")
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print("Ошибка в получении данных ", error)

get_teacher_detail(3)
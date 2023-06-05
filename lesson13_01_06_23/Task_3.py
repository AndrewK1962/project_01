# Задача 3
# ⮚Создайте матрицу размером 7 на 7
# ⮚Диапазон значений от 50 до 100
# ⮚Посчитайте суму элементов по столбцам
# ⮚Посчитайте суму элементов по строкам
# ⮚Посчитайте общую сумму элементов
# ⮚Запишите результат в файл task3.csv
import csv
import numpy as np
matrix = np.arange(51,100).reshape((7, 7))

print("Матрица:")
print(matrix)

Total_Sum = np.sum(matrix)
print("Сумма всех элементов:")
print(np.sum(matrix))

Col_Sum =np.sum(matrix, axis=0)
print("Cумма элементов по столбцам:") 
print(Col_Sum) 

Row_Sum = np.sum(matrix, axis=1)
print("Сумма элементов по строкам:")
print(Row_Sum)

# Записываем результаты в файл task3.csv
with open('task3.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, escapechar=',')
    #writer.writerow("Матрица:")
    writer.writerows(matrix)

    #writer.writerow("Cумма элементов по строкам:")
    writer.writerow(Row_Sum)

    #writer.writerow("Сумма элементов по столбцам:")
    writer.writerow(Col_Sum)

    #writer.writerow("Сумма всех элементов:")
    writer.writerow([Total_Sum])
# Вывод:
#     Матрица:
# [[51 52 53 54 55 56 57]
#  [58 59 60 61 62 63 64]
#  [65 66 67 68 69 70 71]
#  [72 73 74 75 76 77 78]
#  [79 80 81 82 83 84 85]
#  [86 87 88 89 90 91 92]
#  [93 94 95 96 97 98 99]]
# Сумма всех элементов:
# 3675
# Cумма элементов по столбцам:
# [504 511 518 525 532 539 546]
# Сумма элементов по строкам:
# [378 427 476 525 574 623 672]
    
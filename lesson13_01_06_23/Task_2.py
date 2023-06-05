# Задача 2

# ⮚Создайте матрицу размером 7 на 7
# ⮚Диапазон значений от 50 до 100
# ⮚Запишите результат в файл task2.csv

import numpy as np
a = np.arange(51,100).reshape((7, 7))
print(a)
np.savetxt('task2.csv', a,
delimiter=',', fmt='%s')

# Задача 1
# ⮚Создайте матрицу с диагональными значениями
# 16, 5, 8, 10, 9, 1
# ⮚Все остальные значения должны равняться 0
# ⮚Запишите результат в файл task1.csv

import numpy as np
x = np.diag([16, 5, 8, 10, 9, 1])
print(x)
np.savetxt('task1.csv', x,
delimiter=',', fmt='%s')
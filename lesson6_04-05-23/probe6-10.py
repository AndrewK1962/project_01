#TODO модули и импорт


# модули - это файл с расширением  .py
# пакет - это папка в которой  лежат модули и файл __init__.py
# библиотека - набор пакетов

import random 
ids = range(1000, 9999)
print(random.choices(ids, k=5))
print(random.sample(ids, k=5))
print(random.randint(0, len(ids)))
# [2765, 8498, 3483, 3556, 8159]
# [2533, 1405, 7970, 9452, 3773]
# 8131
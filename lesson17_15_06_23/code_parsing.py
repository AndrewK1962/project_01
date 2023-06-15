# Задача
# Собрать данные (аббревиатуру, коды и рассшифровку) из таблицы статьи ISO 4217 
# https://en.wikipedia.org/wiki/ISO_4217

# Документация bs4
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start

# Импорты
from bs4 import BeautifulSoup
from requests import get
from pprint import pprint
from pandas import DataFrame

# Функции
def clean_tags(arr: list) -> list:
    """Функция возвращает список строк, очищенных от лишних тегов"""
    
    clean_arr = []
    for tag in arr:
        if 'title' in str(tag):
            clean_arr.append(str(tag).split('">')[1].split('<')[0])
        else:
            clean_arr.append(str(tag).split('>')[1].split('<')[0])

    return clean_arr


url = 'https://en.wikipedia.org/wiki/ISO_4217'

# стягиваем страницу с помощью requests.get
page = get(url).text

# создаем о бъект BeautifulSoup, чтобы искать по тегам
soup = BeautifulSoup(page, 'html.parser')

# таблица с данными о валютах
table = soup.find('table', {'class': 'wikitable'})

# списки данных из таблицы
curr_codes = table.find_all('td')[0::5]
code_numbers = table.find_all('td')[1::5]
titles = table.find_all('td')[3::5]

# Создаем таблицу из полученных списков
df = DataFrame({
   'Code': clean_tags(curr_codes),
   'Num': clean_tags(code_numbers),
   'Currency': clean_tags(titles),
})

# сохраняем в csv-файл
df.to_csv('коды валют.csv', index=False)

# Для excel
# df.to_csv('коды валют.csv', index=False, sep=';')


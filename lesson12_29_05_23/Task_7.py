# Задача 7
import pandas as pd
import requests

link = ''
token = ''

request = f'{link}/rtpi_rosstat_weight?select=rosstat_id,rosstat_name'
myheaders = {'Authorization': f'Bearer {token}',
             'Content-Type': 'application/json',
             'Range-Unit': 'items'}

response = requests.get(request,headers = myheaders)

response.json()

df = pd.DataFrame(response.json())
df.to_excel("testdata1.xlsx", index = False)
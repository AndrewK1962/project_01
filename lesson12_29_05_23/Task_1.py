#Задача 1
import pandas as pd

df = pd.read_excel("data.xlsx", sheet_name='Sheet1')
kapusta = df[df['sku'] == "Капуста"]
kapusta.to_excel("task1.xlsx", index = False)
import pandas as pd

df = pd.DataFrame({'A': [0,1,2,3,4],
                   'B': [5,6,7,8,9],
                   'C': ['test1', 'test2', 'test3','test4', 'test5']})

df.to_json("test1.json")

import pandas as pd

df = pd.read_excel("data.xlsx", sheet_name='Sheet1')

print (df)

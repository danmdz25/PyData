import pandas as pd

json = 'data.json'

df= pd.read_json(json)
# print(df.to_string()) # Entire json data
print(df) # the headers and the last 5 rows
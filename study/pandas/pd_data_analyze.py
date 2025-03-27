import pandas as pd

csv= 'data.csv'

df= pd.read_csv(csv)
print(df.head(10)) # return the first 10 rows
# print(df.head()) # return the first 05 rows
# print(df.tail()) # return the last 05 rows
# print(df.info()) 
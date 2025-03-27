import pandas as pd
csv=pd.read_csv('data.csv')
big_csv=pd.read_csv('big_data.csv')

# # print(csv.to_string())
# print(big_csv.to_string()) #entire table
# print(big_csv)#first 5 rows and last 5 rows
print(pd.options.display.max_rows) 
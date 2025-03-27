import pandas as pd
csv= 'datalab.csv'

df = pd.read_csv(csv)

df['Date'] = pd.to_datetime(df['Date'], format='mixed', errors='coerce') # transform data out of format to date time and if has no data return NaT
df.dropna(subset=['Date'], inplace=True)#Remove null/NaT rows from Date column


print(df.to_string())
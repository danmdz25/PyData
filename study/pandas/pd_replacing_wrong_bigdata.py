import pandas as pd

csv='datalab.csv'
df=pd.read_csv(csv)

for x in df.index:
    if df.loc[x,'Duration']>120:
        df.loc[x,'Duration']=120

print(df.to_string())
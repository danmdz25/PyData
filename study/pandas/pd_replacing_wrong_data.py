import pandas as pd
csv='datalab.csv'

df = pd.read_csv(csv)
print(df.loc[7,'Duration'])
df.loc[7,'Duration']=45
print(df.loc[7,'Duration'])